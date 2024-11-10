import numpy as np

# 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2
# 2 2 15 15 15 2 2
# 2 2 13 12 16 2 2
# 2 2 15 15 15 2 2
# 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2

# Nhập ma trận I
I_height, I_width = map(int, input("Nhập kích thước ma trận I (h w): ").split())
print("Nhập các phần tử của ma trận I:")
I = []
for _ in range(I_height):
    row = list(map(int, input().split()))
    I.append(row)
I = np.array(I)

# Nhập ma trận Hx
Hx_height, Hx_width = map(int, input("Nhập kích thước ma trận Hx (h w): ").split())
print("Nhập các phần tử của ma trận Hx:")
Hx = []
for _ in range(Hx_height):
    row = list(map(int, input().split()))
    Hx.append(row)
Hx = np.array(Hx)

# Nhập ma trận Hy
Hy_height, Hy_width = map(int, input("Nhập kích thước ma trận Hy (h w): ").split())
print("Nhập các phần tử của ma trận Hy:")
Hy = []
for _ in range(Hy_height):
    row = list(map(int, input().split()))
    Hy.append(row)
Hy = np.array(Hy)


# Khởi tạo ma trận kết quả
I1 = np.zeros((I_height - Hx_height + 1, I_width - Hx_width + 1))

# Thực hiện nhân chập với Hx
for i in range(I_height - Hx_height + 1):
    for j in range(I_width - Hx_width + 1):
        I1[i, j] = np.sum(I[i:i + Hx_height, j:j + Hx_width] * Hx)

# Thực hiện nhân chập với Hy và cộng vào I1
for i in range(I_height - Hy_height + 1):
    for j in range(I_width - Hy_width + 1):
        I1[i, j] += np.sum(I[i:i + Hy_height, j:j + Hy_width] * Hy)

print(I1)
