def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

blank = input()
n, m = map(int, input().split())  # Nhập n hàng và m cột

image = []
for _ in range(n):
    row = list(map(int, input().split()))
    image.append(row)

# Khởi tạo ma trận output với kích thước n hàng và m cột
output = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        old_pixel = image[i][j]
        new_pixel = 255 if old_pixel > 127 else 0
        output[i][j] = new_pixel
        error = old_pixel - new_pixel

        # Truyền lỗi sang các pixel bên cạnh trong cùng hàng
        if j + 1 < m:
            image[i][j + 1] += error

print_matrix(output)
