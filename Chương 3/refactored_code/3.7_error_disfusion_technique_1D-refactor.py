def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

blank = input()
n = int(input())

image = []
for _ in range(n):
    row = list(map(int, input().split()))
    image.append(row)

output = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        old_pixel = image[i][j]
        new_pixel = 255 if old_pixel > 127 else 0
        output[i][j] = new_pixel
        error = old_pixel - new_pixel

        if j + 1 < n:
            image[i][j + 1] += error

print_matrix(output)
