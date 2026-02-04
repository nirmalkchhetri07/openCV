import cv2

image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully!")

    cv2.putText(image,"Hello nameste", (50,300),cv2.FONT_HERSHEY_SIMPLEX,
                1.2,(0,255,0),2)
#display
    cv2.imshow("Adding text over the image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()