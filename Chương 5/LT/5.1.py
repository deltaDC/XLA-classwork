import numpy as np

# Khởi tạo ma trận I, Hx và Hy
I = np.array([
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 15, 15, 15, 2, 2],
    [2, 2, 13, 12, 16, 2, 2],
    [2, 2, 15, 15, 15, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
])

Hx = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
])

Hy = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1],
])

# Kích thước của ma trận I và ma trận bộ lọc
I_height, I_width = I.shape
Hx_height, Hx_width = Hx.shape
Hy_height, Hy_width = Hy.shape

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
