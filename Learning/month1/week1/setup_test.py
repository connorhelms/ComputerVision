# test_setup.py
import cv2
import numpy as np
import matplotlib

print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)
print("Matplotlib version:", matplotlib.__version__)

# Create a simple blank NumPy array (like a tiny black image)
# 30x30 pixels, 3 color channels (for BGR by default in OpenCV)
# uint8 means unsigned 8-bit integer (0-255)
blank_image = np.zeros((30, 30, 3), dtype=np.uint8)
print("Successfully created a NumPy array for an image.")
print("Shape of array:", blank_image.shape)

print("\nSetup seems OK! You're ready for Week 2.")