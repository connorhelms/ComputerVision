# For an 8-bit image, this value ranges from 0 (black) to 255 (white).
# NumPy Representation: A 2D array (height x width).

# For a 16-bit image, this value ranges from 0 (black) to 65535 (white).
# NumPy Representation: A 2D array (height x width).

# For a 32-bit image, this value ranges from 0 (black) to 16777215 (white).
# NumPy Representation: A 2D array (height x width).

# For a 64-bit image, this value ranges from 0 (black) to 18446744073709551615 (white).
# NumPy Representation: A 2D array (height x width).
import numpy as np



# 8-bit image 3x3 grayscale image (values 0-255)
grayscale_image_data_8bit = np.array([
    [50, 100, 150],
    [200, 220, 25],
    [0, 75, 125]
], dtype=np.uint8)

print('8-bit image data: ', grayscale_image_data_8bit)
print("Shape of 8-bit image: ", grayscale_image_data_8bit.shape)
print("Value of pixel at (0, 0): ", grayscale_image_data_8bit[0, 0])
print('---'*50)



# 16-bit image 3x3 grayscale image (values 0-65535)
grayscale_image_data_16bit = np.array([
    [1000, 2000, 3000],
    [4000, 5000, 6000],
    [7000, 8000, 9000]
], dtype=np.uint16)

print('16-bit image data: ', grayscale_image_data_16bit)
print("Shape of 16-bit image: ", grayscale_image_data_16bit.shape)
print("Value of pixel at (0, 0): ", grayscale_image_data_16bit[0, 0])
print('---'*50)



# 32-bit image 3x3 grayscale image (values 0-16777215)
grayscale_image_data_32bit = np.array([
    [100000, 200000, 300000],
    [400000, 500000, 600000],
    [700000, 800000, 900000]
], dtype=np.uint32)

print('32-bit image data: ', grayscale_image_data_32bit)
print("Shape of 32-bit image: ", grayscale_image_data_32bit.shape)
print("Value of pixel at (0, 0): ", grayscale_image_data_32bit[0, 0])
print('---'*50)



# RGB (Red, Green, Blue): Each pixel has three values, one for the intensity of Red, one for Green, and one for Blue. Combining these gives the full color.
# For an 8-bit per channel image, each R, G, B value is 0-255.
# NumPy Representation: A 3D array (height x width x 3). The third dimension represents the color channels (R, G, B).

# 8-bit RGB image 3x3 (values 0-255)
rgb_image_data = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
], dtype=np.uint8)

print('RGB image data: ', rgb_image_data)
print("Shape of RGB image: ", rgb_image_data.shape)
print("Value of pixel at (0, 0): ", rgb_image_data[0, 0])
print('---'*50)



# HSV (Hue, Saturation, Value) / HSL (Hue, Saturation, Lightness):
# Hue: The actual color (e.g., red, green, purple). Typically ranges from 0-179 or 0-360.
# Saturation: The "purity" or intensity of the color (0 = gray, max value = pure color).
# Value/Lightness: The brightness of the color (0 = black, max value = bright color).
# Often more intuitive for color-based segmentation because it separates color (Hue) from intensity (Value). OpenCV typically uses H: 0-179, S: 0-255, V: 0-255.
# Image Depth / Bit Depth:
# Number of bits used per pixel (or per channel in a color image).
# 8-bit (np.uint8): Values 0-255. Most common for standard images.
# 16-bit (np.uint16): Values 0-65535. More precision, used in medical imaging, HDR.

