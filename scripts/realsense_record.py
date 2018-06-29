import pyrealsense2 as rs
import numpy as np
import tifffile

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 6)
config.enable_stream(rs.stream.infrared, 1, 1280, 720, rs.format.y8, 6)
config.enable_stream(rs.stream.infrared, 2, 1280, 720, rs.format.y8, 6)

# Start streaming
pipeline.start(config)
k = 0

try:
    while True:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        infrared_frame_1 = frames.get_infrared_frame(1)
        infrared_frame_2 = frames.get_infrared_frame(2)
        if not depth_frame or not color_frame or not infrared_frame_1 or not infrared_frame_2:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        infrared_image_1 = np.asanyarray(infrared_frame_1.get_data())
        infrared_image_2 = np.asanyarray(infrared_frame_2.get_data())

        tifffile.imsave("color_" + str(k).zfill(5) + ".tiff", color_image)
        tifffile.imsave("depth_" + str(k).zfill(5) + ".tiff", depth_image)
        tifffile.imsave("infrared_1_" + str(k).zfill(5) + ".tiff", infrared_image_1)
        tifffile.imsave("infrared_2_" + str(k).zfill(5) + ".tiff", infrared_image_2)
        k += 1
        print("recording frame " + str(k))

finally:

    # Stop streaming
    pipeline.stop()
