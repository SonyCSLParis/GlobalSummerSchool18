import cv2
import matplotlib.pyplot as pl
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import numpy as np

def filter_matches(p1, p2, matches, ratio = 0.75):
    mp1, mp2 = [], [] 
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
          
            mp1.append( p1[m[0].queryIdx] )
            mp2.append( p2[m[0].trainIdx] )
    p1 = np.float32([p.pt for p in mp1])
    p2 = np.float32([p.pt for p in mp2])
    p_pairs = zip(p1, p2)
    return list(p_pairs)

def draw_matches(im1, im2, ms,imname, lwidth=5,r=8):
    im = np.hstack((im1,im2))
    cols = np.random.randint(0,256,[len(ms),3])
    for j,m in enumerate(ms):
       p1 = tuple(np.round(m[0]).astype(int))
       p2 = tuple(np.round(m[1]).astype(int) + np.array([im1.shape[1], 0]))
       cv2.line(im, p1, p2, cols[j].tolist(), lwidth)
       cv2.circle(im, p1, r, cols[j].tolist(), lwidth)
       cv2.circle(im, p2, r, cols[j], lwidth)
    cv2.imwrite(imname,im)   

"""
image=cv2.imread("crop.jpg")

detector = cv2.xfeatures2d.SIFT_create()
norm = cv2.NORM_L2
#detector = cv2.AKAZE_create() #Alternative if xfeature2d not available
#norm = cv2.NORM_HAMMING
matcher = cv2.BFMatcher(norm)
points, desccriptor = detector.detectAndCompute(image, None)

im_points=image.copy()
cv2.drawKeypoints(image, points,im_points)
#pl.imshow(im_points[1480:1840,1200:1450])
"""


im1=cv2.imread("12a.jpg")
im2=cv2.imread("12b.jpg")

im1=cv2.pyrDown(im1)
im2=cv2.pyrDown(im2)

#detector = cv2.xfeatures2d.SIFT_create()
detector = cv2.AKAZE_create() #Alternative if xfeature2d not available

p1, d1 = detector.detectAndCompute(im1, None)
p2, d2 = detector.detectAndCompute(im2, None)

norm = cv2.NORM_L2
matcher = cv2.BFMatcher(norm)
raw_matches = matcher.knnMatch(d1, trainDescriptors = d2, k = 2) 

#match_pairs=filter_matches(p1, p2, raw_matches, ratio = 0.65)
#draw_matches(im1, im2, ms,imname, lwidth=5,r=8)
ratio=.75
mp1, mp2 = [], [] 
for m in raw_matches:
    if len(m) == 2 and m[0].distance < m[1].distance * ratio:      
        mp1.append( p1[m[0].queryIdx] )
        mp2.append( p2[m[0].trainIdx] )
pt1 = np.float32([p.pt for p in mp1])
pt2 = np.float32([p.pt for p in mp2])
match_pairs = list(zip(pt1, pt2))

im = np.hstack((im1,im2))
cols = np.random.randint(0,256,[len(match_pairs),3])
for j,m in enumerate(match_pairs):
   p1 = tuple(np.round(m[0]).astype(int))
   p2 = tuple(np.round(m[1]).astype(int) + np.array([im1.shape[1], 0]))
   cv2.line(im, p1, p2, cols[j].tolist(), 5)
   cv2.circle(im, p1, 10, cols[j].tolist(), 5)
   cv2.circle(im, p2, 10, cols[j].tolist(), 5)

#tr_rigid = cv2.estimateRigidTransform(pt1, pt2, True)
#h=np.vstack([tr_rigid,[0,0,1]]) 

h,_=cv2.findHomography(pt1, pt2, cv2.RANSAC, 1.0)

corners = np.array([[[0,0]],[[0,im1.shape[0]]],[[im1.shape[1],0]],[[im1.shape[1],im1.shape[0]]]], dtype=np.float32)
cornersTrans = cv2.perspectiveTransform(corners,h)

mins = np.amin(cornersTrans, axis=0).astype(np.int)
maxs = np.amax(cornersTrans, axis=0).astype(np.int)

cornersAll=np.concatenate((cornersTrans,corners))

allmins = np.amin(cornersAll, axis=0).astype(np.int)
allmaxs = np.amax(cornersAll, axis=0).astype(np.int)

tH=np.dot([[1, 0, -1 * allmins[0][0]], [0, 1, -1 * allmins[0][1]], [0, 0, 1]],h)

warped_image = cv2.warpPerspective(im1, tH, (allmaxs[0][0] - allmins[0][0], allmaxs[0][1] - allmins[0][1])) 

point = np.array([-allmins[0][0],  -allmins[0][1]]).astype(np.int)

output_image=np.zeros_like(warped_image)
output_image[point[1]:point[1] + im2.shape[0],point[0]:point[0] + im2.shape[1]] = im2

int_corners=[[max(cornersTrans[0][0,0],cornersTrans[1][0,0]),max(0,cornersTrans[0][0,1]-allmins[0][1],cornersTrans[2][0,1]-allmins[0][1])], [im1.shape[1],max(cornersTrans[1][0,1],cornersTrans[3][0,1])]]            

int1=output_image[int(int_corners[0][1]):int(int_corners[1][1]),int(int_corners[0][0]):int(int_corners[1][0])]
int2=warped_image[int(int_corners[0][1]):int(int_corners[1][1]), int(int_corners[0][0]):int(int_corners[1][0])]

fx=np.arange(int1.shape[1])/(1.*int1.shape[1])
f1=int1*(1-fx[:,np.newaxis])
f2=int2*fx[:,np.newaxis]
res=(f1+f2)

output_image+=warped_image
output_image[int(int_corners[0][1]):int(int_corners[1][1]),int(int_corners[0][0]):int(int_corners[1][0])]=res.astype(np.uint8)

"""
circles=[]
for p in points: 
	if p.size: circles.append(Circle((p.pt[1],p.pt[0]),p.size))

ax=pl.subplot(111)
pl.imshow(image[1480:1840,1200:1450,::-1])
p = PatchCollection(circles, alpha=0.4)
ax.add_collection(p)
"""