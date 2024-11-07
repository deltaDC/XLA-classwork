# Giá trị mức xám và tần suất tương ứng
g = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
h_g = [2, 3, 4, 5, 7, 8, 12, 47, 10, 2]


# Hàm tính ngưỡng đối xứng nền
def find_symmetric_threshold(g, h_g):
    total_pixels = sum(h_g)  # Tổng số điểm ảnh
    left_sum = 0  # Tổng tần suất ở phía bên trái
    right_sum = total_pixels  # Tổng tần suất từ ngưỡng trở đi

    # Duyệt qua từng mức xám để tìm ngưỡng
    for i in range(len(g)):
        left_sum += h_g[i]  # Cộng thêm tần suất của mức xám hiện tại vào bên trái
        right_sum -= h_g[i]  # Trừ tần suất của mức xám hiện tại khỏi bên phải

        print("Ngưỡng:", g[i], "Tổng tần suất bên trái:", left_sum, "Tổng tần suất bên phải:", right_sum)

        # Nếu tổng tần suất hai bên gần bằng nhau, thì đây là ngưỡng
        if left_sum >= right_sum:
            return g[i]  # Trả về ngưỡng tìm được


# Tìm ngưỡng
optimal_threshold = find_symmetric_threshold(g, h_g)
print("Ngưỡng tối ưu theo thuật toán đối xứng nền:", optimal_threshold)
