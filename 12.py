from PIL import Image, ImageFilter

filename = input("Enter image filename: ")

try:
    image = Image.open(filename)
    print("Image size:", image.size)
    print("Image format:", image.format)

    print("\n1. Grayscale")
    print("2. Black and white")
    print("3. Blur")

    choice = input("Select filter: ")

    if choice == "1":
        result = image.convert("L")

    elif choice == "2":
        gray = image.convert("L")
        result = gray.point(
            lambda pixel: 255 if pixel >= 128 else 0
        )

    elif choice == "3":
        result = image.filter(ImageFilter.BLUR)

    else:
        print("Invalid choice.")
        raise SystemExit

    result.save("processed_image.png")
    print("Processed image saved as processed_image.png")

except FileNotFoundError:
    print("Image file not found.")
except OSError as e:
    print("Unable to process image:", e)