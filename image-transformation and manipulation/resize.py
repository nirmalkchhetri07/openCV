import cv2


image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is None:
    print("Image is not found")
else:
    print("Image load successfully")

    resized = cv2.resize(image, (300,300)) #width,height

    cv2.imshow("Original Image",image)
    cv2.imshow("image-transformation and manipulation/Resized Image",resized)

    cv2.imwrite("resized_output.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

