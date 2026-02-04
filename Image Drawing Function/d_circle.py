import cv2
from django.template.defaultfilters import center

image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully!")

    cv2.circle(image,(200,200), 50, (255,0,0),-1)

    cv2.imshow("Drawing Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()