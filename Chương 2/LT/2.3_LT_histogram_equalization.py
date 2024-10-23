import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../assets/Fig0310(b)(washed_out_pollen_image)100kb.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Không thể đọc ảnh.")
else:
    equalized_image = cv2.equalizeHist(image)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Output Image')
    plt.axis('off')

    plt.show()
