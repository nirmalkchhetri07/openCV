import cv2

image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully!")

    pt1 = (50,50) #top,right
    pt2 = (250,250) #bottom, left
    color = (0,0,255)
    thickness = 4

# Drawing Rectangle
    cv2.rectangle(image,pt1,pt2,color,thickness)

#display
    cv2.imshow("Drawing Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()