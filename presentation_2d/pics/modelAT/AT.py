import numpy as np
import matplotlib.pyplot as pl
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection

def IIA(w,h):
   fig=pl.figure(figsize=(5,17))
   ax = fig.add_subplot(1,1,1)
   Is=[0,h]   

   patches=[]   

   r1=Rectangle((-w/2., 1.1*Is[0]), w, h, facecolor=[.2,.65,.4])
   patches.append(r1)   

   r2=Rectangle((-w/2., 1.1*Is[1]), w, h, facecolor=[.2,.65,.4])
   patches.append(r2)   

   c=Circle((0,Is[-1]+h),.3, facecolor=[.8,.36,.36])
   patches.append(c)   

   for p in patches: ax.add_patch(p)
   pl.xlim([-.5,.5])
   pl.ylim([-.2,2])
   pl.axis("equal")
   pl.axis("off")
   pl.savefig("IIA.png",bbox_inches="tight")
   pl.show()

def IIAA(w,h):
   fig=pl.figure(figsize=(5,17))
   ax = fig.add_subplot(1,1,1)
   Is=[0,h]   

   patches=[]   

   r1=Rectangle((-w/2., 1.1*Is[0]), w, h, facecolor=[.2,.65,.4])
   patches.append(r1)   

   r2=Rectangle((-w/2., 1.1*Is[1]), w, h, facecolor=[.2,.65,.4])
   patches.append(r2)   

   r3=Rectangle((w/2., 1.2*Is[1]), w, h, angle=-45, facecolor=[.2,.65,.4])
   patches.append(r3)   

   c=Circle((0,Is[-1]+h),.3, facecolor=[.8,.36,.36])
   patches.append(c)   

   c1=Circle((w+.5*h,h*1.7),.3, facecolor=[.8,.36,.36])
   patches.append(c1)   

   for p in patches: ax.add_patch(p)
   pl.xlim([-.5,.5])
   pl.ylim([-.2,2])
   pl.axis("equal")
   pl.axis("off")
   pl.savefig("IIAA.png",bbox_inches="tight")
   pl.show()


def IA(w,h):
   fig=pl.figure(figsize=(5,11))
   ax = fig.add_subplot(1,1,1)
   Is=[0]   

   patches=[]   

   r1=Rectangle((-w/2., 1.1*Is[0]), w, h, facecolor=[.2,.65,.4])
   patches.append(r1)   

   c=Circle((0,Is[-1]+h),.3, facecolor=[.8,.36,.36])
   patches.append(c)   

   for p in patches: ax.add_patch(p)
   pl.xlim([-.5,.5])
   pl.ylim([-.2,2])
   pl.axis("equal")
   pl.axis("off")
   pl.savefig("IA.png",bbox_inches="tight")
   pl.show()

def IF(w,h):
   fig=pl.figure(figsize=(2,6*N))
   ax = fig.add_subplot(1,1,1)
   Is=[0]   
   wf=1.5*w
   hf=.75*h
   patches=[]   

   r1=Rectangle((-w/2., 1.1*Is[0]), w, h, facecolor=[.2,.65,.4])
   patches.append(r1)   

   f=Rectangle((-wf/2.,1.1*Is[-1]+h), wf, hf, facecolor=[.94,.94,.85])#, edgecolor=[.2,.2,.2])
   patches.append(f)

   for p in patches: ax.add_patch(p)
   pl.xlim([-.5,.5])
   pl.ylim([-.2,2])
   pl.axis("equal")
   pl.axis("off")
   pl.savefig("IF.png",bbox_inches="tight")
   pl.show()

def AT(w, h, N):
   fig=pl.figure(figsize=(5,17))
   ax = fig.add_subplot(1,1,1)

   wf=1.5*w
   hf=.75*h

   Is=[0,h,2*h]   

   patches=[]   

   r1=Rectangle((-w/2., 1.1*Is[0]), w, h, facecolor=[.2,.65,.4])
   patches.append(r1)   
   ht=1.1*h
   for i in range(N):
    s=1-2*(i%2)
    r2=Rectangle((-w/2., ht+.1*h), w, h, facecolor=[.2,.65,.4])
    patches.append(r2)

    if not(i%2):
       r3=Rectangle((-w/2., .2*h+ht), w, h, angle=-45, facecolor=[.2,.65,.4])
       patches.append(r3)   
       f1=Rectangle((.13, .5*h+ht), wf, hf, angle=-45, facecolor=[.94,.94,.85])
       patches.append(f1)   
    else:
       r5=Rectangle((-w/2., .2*h+ht), w, h, angle=45, facecolor=[.2,.65,.4])
       patches.append(r5)   
       f2=Rectangle((-.08-2*w, .5*h+ht), wf, hf, angle=45, facecolor=[.94,.94,.85])
       patches.append(f2)   
    ht+=1.1*h   

   #rf=Rectangle((-w/2., 1.1*h+ht), w, h, facecolor=[.2,.65,.4])
   #patches.append(rf)   

   c=Circle((0,ht),.3, facecolor=[.8,.36,.36])
   patches.append(c)   

   for p in patches: ax.add_patch(p)
   pl.xlim([-.5,.5])
   pl.ylim([-.2,2])
   pl.axis("equal")
   pl.axis("off")
   pl.savefig("AT_%03d.png"%N,bbox_inches="tight")
   #pl.show()
   pl.clf()


h=1
w=.2

#IA(w,h)
#IIA(w,h)
#IF(w,h)
#IIAA(w,h)
for k in range(30): AT(w, h, k)