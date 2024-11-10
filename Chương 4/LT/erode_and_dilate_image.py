import numpy as np


# Hàm dilate và erode từ mã bạn đã cung cấp
def dilate(image, se):
    image_height, image_width = image.shape
    se_height, se_width = se.shape

    pad_height = se_height // 2
    pad_width = se_width // 2

    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    dilated_image = np.zeros_like(image)

    for i in range(image_height):
        for j in range(image_width):
            if np.any(padded_image[i:i + se_height, j:j + se_width] & se):
                dilated_image[i, j] = 1

    return dilated_image


def erode(image, se):
    image_height, image_width = image.shape
    se_height, se_width = se.shape

    pad_height = se_height // 2
    pad_width = se_width // 2

    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    eroded_image = np.zeros_like(image)

    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i + se_height, j:j + se_width]
            if np.all((region & se) == se):
                eroded_image[i, j] = 1

    return eroded_image

# Nhập ma trận X và B
n, m = map(int, input().split())
X = []
for _ in range(n):
    row = list(map(int, input().split()))
    X.append(row)
X = np.array(X)

p, q = map(int, input().split())
B = []
for _ in range(p):
    row = list(map(int, input().split()))
    B.append(row)
B = np.array(B)

# Thực hiện phép dãn và co trên X với B
X1 = dilate(X, B)
X2 = erode(X, B)

# Hiển thị kết quả
print("Ma trận sau khi co (X2):")
for row in X2:
    print(" ".join(map(str, row)))

print("Ma trận sau khi dãn (X1):")
for row in X1:
    print(" ".join(map(str, row)))


# 8 8
# 0 1 1 0 0 1 0 0
# 1 1 0 0 0 1 1 0
# 0 1 1 0 1 1 1 1
# 1 1 0 1 1 1 1 1
# 1 0 1 1 1 1 0 0
# 1 0 0 1 0 1 1 1
# 1 0 1 1 1 0 1 0
# 1 0 0 0 1 1 1 1
# 3 3
# 0 1 0
# 1 1 1
# 0 1 0