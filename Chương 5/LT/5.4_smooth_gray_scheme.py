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

# Nhập kích thước của ma trận I
I_height, I_width = map(int, input("Nhập kích thước ma trận I (h w): ").split())

# Nhập các phần tử của ma trận I
print("Nhập các phần tử của ma trận I:")
I = []
for _ in range(I_height):
    row = list(map(int, input().split()))
    I.append(row)
I = np.array(I)

# Tính biểu đồ tần suất
histogram, _ = np.histogram(I, bins=range(11))

print("Biểu đồ tần suất:", histogram)

# Làm trơn biểu đồ tần suất với W = 3 và W = 5, sau đó làm tròn lên
smoothed_histogram_w3_rounded = smooth_histogram(histogram, 3)
smoothed_histogram_w5_rounded = smooth_histogram(histogram, 5)

print("Biểu đồ tần suất sau khi làm trơn với W=3:", smoothed_histogram_w3_rounded)
print("Biểu đồ tần suất sau khi làm trơn với W=5:", smoothed_histogram_w5_rounded)
