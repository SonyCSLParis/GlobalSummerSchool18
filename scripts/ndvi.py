import open3d
import numpy as np
from matplotlib import cm

pc_ir = open3d.read_point_cloud("pc_ir.ply")
pc_rgb = open3d.read_point_cloud("pc_rgb.ply")
pc_ir = open3d.crop_point_cloud(pc_ir, [-0.5, -0.5, 0], [0.5, 0.5, 1.5])
pc_rgb = open3d.crop_point_cloud(pc_rgb, [-0.5, -0.5, 0], [0.5, 0.5, 1.5])

rgb = np.asarray(pc_rgb.colors)
rgb_ir = np.asarray(pc_ir.colors).sum(axis=1)
grey = rgb.sum(axis=1) 

lam = np.min(rgb_ir/grey)

nir = rgb_ir - 0.6*grey
nir = np.maximum(nir, 0)
ndvi = (nir - rgb[:,0]) / (nir + rgb[:, 0])
ndvi_color = np.zeros_like(rgb)
for i in range(3):
    ndvi_color[:, i] = ndvi

# ndvi = (ndvi + 2.0)/(np.max(ndvi) + 2.0)
ndvi = ndvi + 0.5
cmap = cm.PRGn


pc_ndvi = open3d.PointCloud(pc_ir)
pc_ndvi.colors = open3d.Vector3dVector(cmap(ndvi)[:,0:3])

pts = np.asarray(pc_ndvi.points)
# pts[:, :] = pts[:, :] / pts[:, 2][:, np.newaxis]

open3d.draw_geometries([pc_ndvi])
