import cv2

image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully!")

    pt1 = (50,100)
    pt2 = (300,100)
    color = (0,0,255)
    thickness = 4

    cv2.line(image, pt1, pt2, color,thickness)

    cv2.imshow("Line_Drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    