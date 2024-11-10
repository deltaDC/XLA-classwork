# Nhập ma trận I
I_height, I_width = map(int, input("Nhập kích thước ma trận I (h w): ").split())
print("Nhập các phần tử của ma trận I:")
I = []
for _ in range(I_height):
    row = list(map(int, input().split()))
    I.append(row)

# Nhập ma trận Hz
Hz_height, Hz_width = map(int, input("Nhập kích thước ma trận Hz (h w): ").split())
print("Nhập các phần tử của ma trận Hz:")
Hz = []
for _ in range(Hz_height):
    row = list(map(int, input().split()))
    Hz.append(row)

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
