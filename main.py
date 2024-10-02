import cv2

def to_ascii(n):
    alpha = "^\”,:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    asciiIndex = int((len(alpha) - 1) * (n / 255.0))
    return alpha[asciiIndex]    


img = cv2.imread("./s.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (img.shape.x // 3, img.shape.y // 3))

x, y = img.shape

for i in range(x):
    
    for j in range(y):
        
        color_number = img[i][j]
        print(to_ascii(color_number), end=" ")
    
    print()
