# Khởi tạo ma trận I và Hz
I = [
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 15, 15, 15, 2, 2],
    [2, 2, 13, 12, 16, 2, 2],
    [2, 2, 15, 15, 15, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
]

Hz = [
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0],
]

# Kích thước của ma trận I và ma trận bộ lọc
I_height = len(I)
I_width = len(I[0])
Hz_height = len(Hz)
Hz_width = len(Hz[0])

# Khởi tạo ma trận kết quả
I2_height = I_height - Hz_height + 1
I2_width = I_width - Hz_width + 1
I2 = [[0 for _ in range(I2_width)] for _ in range(I2_height)]

# Thực hiện nhân chập với Hz
for i in range(I2_height):
    for j in range(I2_width):
        # Tính giá trị cho từng phần tử của ma trận I2
        sum_value = 0
        for m in range(Hz_height):
            for n in range(Hz_width):
                sum_value += I[i + m][j + n] * Hz[m][n]
        I2[i][j] = sum_value

# In kết quả
for row in I2:
    print(row)
