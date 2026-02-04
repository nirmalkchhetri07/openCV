import cv2

image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is not None:
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)

    cv2.imshow("Original",image)
    cv2.imshow("flipped_horizontal",flipped_horizontal)
    cv2.imshow("flipped_vertical",flipped_vertical)
    cv2.imshow("flipped_both",flipped_both)
    print("Success")

else:
    print("Could not found image")
