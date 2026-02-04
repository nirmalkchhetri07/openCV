import cv2

image = cv2.imread("Phase1/python-image.png")

if image is not None:
    success =  cv2.imwrite("output-python.png",image)
    if success:
        print("Image save successfully as output_python.png")
    else:
        print("Failed to save an image")
else:
    print("ERROR: could not load image")