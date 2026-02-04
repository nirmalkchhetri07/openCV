import cv2
from django.template.defaultfilters import center

image = cv2.imread("image-transformation and manipulation/python-image.png")

if image is not None:
    (h,w) = image.shape[:2]

    center = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center, 90,1.0)
    rotated = cv2.warpAffine(image,M, (w,h))

    cv2.imshow("Original_image",image)
    cv2.imshow("Rotated 90 degree_image",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not found image")
