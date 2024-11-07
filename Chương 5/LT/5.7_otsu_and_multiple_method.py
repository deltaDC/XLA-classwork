import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('noisy_image.png', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Không tìm thấy tệp ảnh 'noisy_image.png'. Vui lòng kiểm tra đường dẫn và tên tệp.")

# Tính histogram (b) của ảnh
hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])

# Bước 1: Tính gradient magnitude và tạo mặt nạ (c)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Ngưỡng hóa tại mức phân vị 99.7%
threshold_value = np.percentile(gradient_magnitude, 99.7)
_, mask = cv2.threshold(gradient_magnitude, threshold_value, 255, cv2.THRESH_BINARY)
mask = mask.astype(np.uint8)

# Tạo ảnh (d) bằng cách nhân ảnh nhiễu (a) với mặt nạ (c)
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Tính histogram (e) của các pixel khác không trong ảnh (d)
nonzero_pixels = masked_image[masked_image > 0]
hist_masked = cv2.calcHist([nonzero_pixels], [0], None, [256], [0, 256])

# Áp dụng ngưỡng Otsu trên ảnh (d) để tìm ngưỡng tối ưu
# Xác định ngưỡng thủ công từ histogram (e)
otsu_threshold_value = 134

# Áp dụng ngưỡng Otsu trên ảnh (d)
_, otsu_thresholded_image = cv2.threshold(masked_image, otsu_threshold_value, 255, cv2.THRESH_BINARY)

# Hiển thị kết quả
fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# ảnh (a), histogram (b), và ảnh (c)
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Noisy Image (a)')
axs[0, 0].axis('off')

axs[0, 1].plot(hist_full, color='black')
axs[0, 1].set_title('Histogram of (a) (b)')
axs[0, 1].set_xlim([0, 256])
axs[0, 1].set_xlabel('Gray Level')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_xticks(range(0, 257, 32))

axs[0, 2].imshow(mask, cmap='gray')
axs[0, 2].set_title('Mask Image (c)')
axs[0, 2].axis('off')

# ảnh (d), histogram (e), và ảnh (f)
axs[1, 0].imshow(masked_image, cmap='gray')
axs[1, 0].set_title('Image (d) = (a) * (c)')
axs[1, 0].axis('off')

axs[1, 1].plot(hist_masked, color='black')
axs[1, 1].set_title('Histogram of nonzero pixels in (d) (e)')
axs[1, 1].set_xlim([0, 256])
axs[1, 1].set_xlabel('Gray Level')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_xticks(range(0, 257, 32))

axs[1, 2].imshow(otsu_thresholded_image, cmap='gray')
axs[1, 2].set_title('Segmented Image with Otsu Threshold (f)')
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()
