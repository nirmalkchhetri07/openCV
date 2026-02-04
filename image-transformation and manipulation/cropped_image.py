import cv2

image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is not None:
    cropped = image[100:300, 40:200]

    cv2.imshow("Original-Image", image)
    cv2.imshow("Cropped-Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("success")
else:
    print("Could not load image")