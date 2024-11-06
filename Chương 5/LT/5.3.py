import numpy as np
import cv2

# Bước 1: Tạo ma trận ảnh
I = np.array([
    [1, 4, 1, 1, 2, 3, 2, 3],
    [3, 2, 4, 2, 5, 2, 6, 2],
    [2, 1, 8, 2, 5, 2, 5, 6],
    [2, 5, 2, 4, 7, 9, 1, 4],
    [2, 2, 3, 0, 0, 1, 2, 1],
    [1, 5, 7, 1, 2, 4, 5, 6]
], dtype=np.uint8)

# Bước 2: Tính ngưỡng Otsu
# Hàm cv2.threshold sẽ tự động tính ngưỡng Otsu cho ảnh
_, otsu_threshold = cv2.threshold(I, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Kết quả ngưỡng Otsu
print("Ngưỡng Otsu:", _)
print("Ảnh sau khi áp dụng ngưỡng:")
print(otsu_threshold)
