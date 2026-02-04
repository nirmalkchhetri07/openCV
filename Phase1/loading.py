import cv2

image = cv2.imread("Phase1/python-image.png")

if image is not None:
    cv2.imshow("Window Title", image) #open the window
    cv2.waitKey(0) #Wait for a key
    cv2.destroyAllWindows() #close the window

else:
    print("Could not load the image!")


