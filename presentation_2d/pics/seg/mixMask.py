import cv2
import numpy as np

ds=["04_14"]
ds=["04_14","04_20", "04_25", "05_02", "05_15", "04_19", "04_21","04_27_2", "05_05", "04_20_2", "04_25_2", "04_27", "05_12"] 

"""
for d in ds:
   print d	
   im=cv2.imread("weeding/%s.jpg"%d)
   l=cv2.imread("weeding/labels_svm_%s.png"%d)
   h, w, _=im.shape
   x,y=np.meshgrid(np.arange(w),np.arange(h))  
   m=(h*x<y*w).astype(np.uint8)[:,::-1]
   m3=np.array([m,m,m]).transpose([1,2,0])
   res=(1-m3)*im+m3*(l*np.array([100,168,53]).astype(np.uint8)+(1-l)*np.array([56,70,84]).astype(np.uint8))
   #res=im.copy()
   #res[-h/2:]=l[-h/2:]*np.array([50,168,53]).astype(np.uint8)+(1-l[-h/2.])*np.array([56,70,84]).astype(np.uint8)
 
   #for i in range(h):
   	#for j in range(w):
   	#	if (h-i)>(w-j*h/w):
   	#		res[i,j]=l[i,j,0]*np.array([50,168,53]).astype(np.uint8)+(1-l[i,j,0])*np.array([56,70,84]).astype(np.uint8)
   cv2.imwrite("mixMask_%s.jpg"%d,res)
"""

im=cv2.imread("../cropbed.png")
l=cv2.imread("../labels_svm_cropbed.png")

idxs=np.where(l[:,:,0]==0)
idxs1=np.where(l[:,:,0]>0)
#im[idxs1]=[100,168,53]
im[idxs]=[56,70,84]
cv2.imwrite("cropbed_style2.png",im)