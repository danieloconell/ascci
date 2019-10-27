from PIL import Image
import time

filename = input("Which file to use: ")

before = time.time()

CHARACTERS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
N_CHARACTERS = len(CHARACTERS) - 1

image = Image.open(filename)
png = filename.endswith(".png")

for y in range(image.height):
    for x in range(image.width):
        rgb = image.getpixel((x, y))
        if png:
            *rgb, a = rgb
        brightness = sum(rgb) / 3
        if brightness == 0:
            print(" ", end="")
            continue
        print(CHARACTERS[round(N_CHARACTERS / 255 * brightness)], end="")
    print("")

after = time.time()
print(f"Took {after - before:.2}s")
