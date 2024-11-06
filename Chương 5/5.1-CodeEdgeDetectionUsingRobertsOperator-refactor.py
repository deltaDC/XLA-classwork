def roberts_operator(image):
    Gx_kernel = [[1, 0], [0, -1]]
    Gy_kernel = [[0, 1], [-1, 0]]
    n = len(image)
    output = [[0] * n for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            Gx = (image[i][j] * Gx_kernel[0][0] +
                  image[i][j + 1] * Gx_kernel[0][1] +
                  image[i + 1][j] * Gx_kernel[1][0] +
                  image[i + 1][j + 1] * Gx_kernel[1][1])

            Gy = (image[i][j] * Gy_kernel[0][0] +
                  image[i][j + 1] * Gy_kernel[0][1] +
                  image[i + 1][j] * Gy_kernel[1][0] +
                  image[i + 1][j + 1] * Gy_kernel[1][1])

            output[i][j] = int((Gx ** 2 + Gy ** 2) ** 0.5)

    reversed_output = [row[::-1] for row in output[::-1]]
    return reversed_output


blank = input()
n = int(input().strip())
image = [list(map(int, input().strip().split())) for _ in range(n)]
gradient_image = roberts_operator(image)

for row in gradient_image:
    print(*row)