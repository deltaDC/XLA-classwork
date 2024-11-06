def laplace_operator(image):
    laplace_kernel = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    n = len(image)
    output = [[0] * n for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            laplace_response = sum(laplace_kernel[x][y] * image[i + x - 1][j + y - 1] for x in range(3) for y in range(3))
            output[i][j] = abs(laplace_response)

    return output

blank = input()
n = int(input().strip())
image = [list(map(int, input().strip().split())) for _ in range(n)]
gradient_image = laplace_operator(image)

for row in gradient_image:
    print(*row)
