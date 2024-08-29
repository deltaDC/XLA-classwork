import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance_image(image):
    L = 256
    r1, s1 = 3 * L // 8, L // 8
    r2, s2 = 5 * L // 8, 7 * L // 8

    T = np.zeros(L, dtype=np.uint8)
    for r in range(L):
        if r < r1:
            T[r] = int((s1 / r1) * r)
        elif r < r2:
            T[r] = int(((s2 - s1) / (r2 - r1)) * (r - r1) + s1)
        else:
            T[r] = int(((L - 1 - s2) / (L - 1 - r2)) * (r - r2) + s2)

    enhanced_image = cv2.LUT(image, T)
    return enhanced_image

input_image = cv2.imread('D:\Workspace\Python\XLA-classwork\Anh_mau.png', cv2.IMREAD_GRAYSCALE)

# enhance image
output_image = enhance_image(input_image)

# show input image and enhance image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Ảnh Đầu Vào')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(output_image, cmap='gray')
plt.title('Ảnh Tăng Cường')
plt.axis('off')

plt.show()
