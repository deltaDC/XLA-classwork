import numpy as np

def smooth_histogram(histogram, W):
    smoothed = []
    n = len(histogram)
    for i in range(n):
        # Xác định phạm vi lân cận
        start = - (W - 1) // 2 + i
        end = (W - 1) // 2 + i
        # Tính trung bình các giá trị trong phạm vi và làm tròn lên
        hs = 0

        for j in range(start, end + 1):
            if 0 <= j < n:
                hs += histogram[j]
            else:
                hs += 0  # Add zero if index is out of bounds
        hs /= W
        smoothed.append(round(hs))

    return smoothed


# Ảnh I dưới dạng ma trận numpy
I = np.array([
    [1, 2, 1, 3, 2, 1],
    [4, 4, 3, 2, 4, 0],
    [6, 9, 2, 3, 2, 1],
    [6, 2, 0, 5, 3, 0],
    [3, 4, 0, 5, 1, 5],
    [5, 6, 8, 9, 3, 6]
])

# Tính biểu đồ tần suất
histogram, _ = np.histogram(I, bins=range(11))

print(histogram)
print(_)

# Làm trơn biểu đồ tần suất với W = 3 và W = 5, sau đó làm tròn lên
smoothed_histogram_w3_rounded = smooth_histogram(histogram, 3)
smoothed_histogram_w5_rounded = smooth_histogram(histogram, 5)


print(smoothed_histogram_w3_rounded)
print(smoothed_histogram_w5_rounded)
