def prewitt_operator(image):
    Gx_kernel = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    Gy_kernel = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
    n = len(image)
    output = [[0] * n for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            Gx = sum(Gx_kernel[x][y] * image[i + x - 1][j + y - 1] for x in range(3) for y in range(3))
            Gy = sum(Gy_kernel[x][y] * image[i + x - 1][j + y - 1] for x in range(3) for y in range(3))
            output[i][j] = int((Gx**2 + Gy**2) ** 0.5)

    return output

blank = input()
n = int(input().strip())
image = [list(map(int, input().strip().split())) for _ in range(n)]
gradient_image = prewitt_operator(image)

for row in gradient_image:
    print(*row)
