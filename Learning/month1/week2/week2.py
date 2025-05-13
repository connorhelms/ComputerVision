import cv2
import sys
import matplotlib.pyplot as plt
import os
#1. Loading Images with OpenCV

#"C:\Users\17yam\Desktop\Pfps""C:/Users/17yam/Desktop/Pfps/1.jpg"


image_path = "C:/Users/17yam/Desktop/Pfps/mob_2.png"
#Load in color to load in color image from {image_path}
print(f"Attempting to load image from {image_path}")
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

#Check if the image was loaded successfully
if img_color is None:
    print("Error: Could not read the image file at {image_path}")
    print("Make sure the file exists and the path is correct")
    sys.exit()
else:
    print(f"Image loaded successfully: {image_path}")

#Load in grayscale
img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#Check if the grayscale image was loaded successfully
if img_gray is None:
    print("Error: Could not read the image file at {image_path}")
    print("Make sure the file exists and the path is correct")
    sys.exit()
else:
    print(f"Grayscale image loaded successfully: {image_path}")

#2. Accessing Image Properties

#Properties of the color image
h, w, c = img_color.shape
print(f"Dimensions (HxWxChannels): {h}x{w}x{c}")
print(f"Total number of elements (pixels * channels): {img_color.size}")
print(f"Data type of the pixels: {img_color.dtype}")

if h > 50 and w > 100:
    (b, g, r) = img_color[50, 100]
    print(f"Pixel at (50, 100) - BGR: {b}, {g}, {r}")
else:
    print("Image is too small to access pixel values")

#Grayscale image

print("\n--- Grayscale Image Properties ---")
h_gray, w_gray = img_gray.shape
print(f"Dimensions (Height x Width): {h_gray} x {w_gray}")
print(f"Data type of pixels: {img_gray.dtype}")

if h > 50 and w > 100:
    gray_value = img_gray[50, 100]
    print(f"Pixel at (50, 100) - Grayscale: {gray_value}")
else:
    print("Image is too small to access pixel values")
print("---"*30)

#3. Displaying Images

#Method 1: Using OpenCV (cv2.imshow)

print("Displaying Color Image with OpenCV")
#Color image
cv2.imshow("My color image", img_color)
print("Press any key to close the window")
cv2.waitKey(0)
print("---"*30)

#Grayscale image
cv2.imshow("Grayscale image", img_gray)
print("Press any key to close the window")
cv2.waitKey(0)
print("---"*30)

#Clean Up
cv2.destroyAllWindows()
print("All OpenCV windows closed")
print("---"*30)

#Method 2: Using Matplotlib (plt.imshow)

print("Displaying images using matplotlib")

#Color image
img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 6))
plt.imshow(img_rgb)
plt.title("Color Image")
plt.axis("off")

#Grayscale image
plt.figure(figsize=(8, 6))
plt.imshow(img_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

plt.show()
print("---"*30)

#4. Saving Images

output_path = "C:/Users/17yam/Desktop/ComputerVision/Learning/month1/week2/output"
if not os.path.exists(output_path):
    os.makedirs(output_path)

#Save color image
color_output_path = os.path.join(output_path, "color_image.jpg")
success_color = cv2.imwrite(color_output_path, img_color)
if success_color:
    print(f"Color image saved to {color_output_path}")
else:
    print(f"Failed to save color image to {color_output_path}")

#Save grayscale image
gray_output_path = os.path.join(output_path, "gray_image.jpg")
success_gray = cv2.imwrite(gray_output_path, img_gray)
if success_gray:
    print(f"Grayscale image saved to {gray_output_path}")
else:
    print(f"Failed to save grayscale image to {gray_output_path}")


