import cv2 #OpenCV package
import numpy as np #Numerical python to perform operations on arrays
import matplotlib.pyplot as pl #graphic viz

data_folder="/home/kodda/Dropbox/p2pflab/kaku/GSS/parisparis/"
im_path=data_folder+"photos_satellite_Paris.jpg"
im=cv2.imread(im_path) 

Ms=np.max(im,axis=(0,1)).astype(np.float) 
im_Norm=im/Ms
L=im_Norm.sum(axis=2)
green_idx=3*im_Norm[:,:,1]/L-1