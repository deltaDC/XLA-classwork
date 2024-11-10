import numpy as np
import cv2

# Nhập kích thước của ma trận I
I_height, I_width = map(int, input("Nhập kích thước ma trận I (h w): ").split())

# Nhập các phần tử của ma trận I
print("Nhập các phần tử của ma trận I:")
I = []
for _ in range(I_height):
    row = list(map(int, input().split()))
    I.append(row)
I = np.array(I, dtype=np.uint8)

# Tính ngưỡng Otsu
_, otsu_threshold = cv2.threshold(I, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# In kết quả ngưỡng Otsu và ảnh sau khi áp dụng ngưỡng
print("Ngưỡng Otsu:", _)
print("Ảnh sau khi áp dụng ngưỡng:")
print(otsu_threshold)
