import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_lookup_table(L, r1, s1, r2, s2):
    T = np.zeros(L, dtype=np.uint8)
    for r in range(L):
        if r < r1:
            T[r] = int((s1 / r1) * r)
        elif r < r2:
            T[r] = int(((s2 - s1) / (r2 - r1)) * (r - r1) + s1)
        else:
            T[r] = int(((L - 1 - s2) / (L - 1 - r2)) * (r - r2) + s2)
    return T

def enhance_image(image):
    L = 256
    r1, s1 = 3 * L // 8, L // 8
    r2, s2 = 5 * L // 8, 7 * L // 8
    T = create_lookup_table(L, r1, s1, r2, s2)
    return cv2.LUT(image, T)

def display_images(input_img, output_img):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(input_img, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(output_img, cmap='gray')
    plt.title('Enhanced Image')
    plt.axis('off')

    plt.show()

input_image = cv2.imread('./assets/dot_operator_example.png', cv2.IMREAD_GRAYSCALE)
output_image = enhance_image(input_image)
display_images(input_image, output_image)