# Giá trị mức xám và xác suất tương ứng
from numpy.ma.core import floor


# Hàm tính trung bình mức xám với xác suất
def mean_gray_level(values, probabilities):
    weighted_sum = sum(v * p for v, p in zip(values, probabilities))
    total_probability = sum(probabilities)
    return weighted_sum / total_probability if total_probability != 0 else 0

r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p_r = [0.09, 0.2, 0.1, 0.06, 0.06, 0.08, 0.35, 0.04, 0.01, 0.01]

# Ngưỡng khởi đầu
T = 5

# Thuật toán đẳng liệu
while True:
    # Bước 1: Chia ảnh thành hai nhóm dựa trên ngưỡng hiện tại
    low_gray_levels = []
    low_probabilities = []
    high_gray_levels = []
    high_probabilities = []

    for i in range(len(r)):
        if r[i] <= T:
            low_gray_levels.append(r[i])
            low_probabilities.append(p_r[i])
        else:
            high_gray_levels.append(r[i])
            high_probabilities.append(p_r[i])

    # Bước 2: Tính trung bình mức xám cho từng nhóm
    mean_low = mean_gray_level(low_gray_levels, low_probabilities)
    mean_high = mean_gray_level(high_gray_levels, high_probabilities)

    # Bước 3: Tính ngưỡng mới
    new_threshold = (mean_low + mean_high) / 2

    # Bước 4: Kiểm tra điều kiện dừng
    if abs(new_threshold - T) < 1e-5:
        break  # Dừng nếu ngưỡng không thay đổi đáng kể

    # Cập nhật ngưỡng cho lần lặp tiếp theo
    T = new_threshold

optimal_threshold = int(T)
print("Ngưỡng tối ưu:", optimal_threshold)
