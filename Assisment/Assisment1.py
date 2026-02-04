import cv2

image = cv2.imread("bike.png")

if image is not None:
    # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show the image
    cv2.imshow("BIKE IMAGE", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Ask user for filename
    filename = input("Enter filename to save (without extension): ")

    #Save the image
    save_img = cv2.imwrite(f"{filename}.png",gray)
    if save_img:
        print(f"Image saved successfully as {filename}.png")
    else:
        print("Failed to save image")
else:
    print("Image load failed")

