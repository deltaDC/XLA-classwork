def error_diffusion(image):
    n = len(image)
    threshold = 127

    for i in range(n):
        for j in range(n):
            old_value = image[i][j]
            new_value = 255 if old_value > threshold else 0
            error = old_value - new_value

            image[i][j] = new_value

            if j + 1 < n:
                image[i][j + 1] += error * 7 / 16
            if i + 1 < n:
                if j - 1 >= 0:
                    image[i + 1][j - 1] += error * 3 / 16
                image[i + 1][j] += error * 5 / 16
                if j + 1 < n:
                    image[i + 1][j + 1] += error * 1 / 16

            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(n, j + 2)):
                    image[x][y] = max(0, min(255, image[x][y]))

    return image

n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = error_diffusion(matrix)

for row in result:
    print(*row)

# 4
# 50 150 200 50
# 75 180 30 220
# 160 40 90 120
# 210 70 250 25
