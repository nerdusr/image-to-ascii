import cv2

# fucntion for convert 0-255 number to ascii
def to_ascii(n):
    alpha = "^\”,:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    asciiIndex = int((len(alpha) - 1) * (n / 255.0))
    return alpha[asciiIndex]

# open image file
img = cv2.imread("./s.png", cv2.IMREAD_GRAYSCALE)

# get image width, height
x, y = img.shape

# resize image to smaller
img = cv2.resize(img, (x // 6, y // 6))

#get new image width, height after resizing
x, y = img.shape

# loop on image pixel and convert color number to ascii
for i in range(x):
    for j in range(y):
        color_number = img[i][j]
        print(to_ascii(color_number), end=" ")

    print()
