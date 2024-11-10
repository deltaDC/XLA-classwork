blank = input()

se_size = int(input().strip())

se = []
for i in range(se_size):
    se.append(list(map(int, input().strip().split())))

image_size = int(input().strip())

image = []
for i in range(image_size):
    image.append(list(map(int, input().strip().split())))

image_height = len(image)
image_width = len(image[0])
se_height = len(se)
se_width = len(se[0])

pad_height = se_height // 2
pad_width = se_width // 2

padded_image = [[0] * (image_width + 2 * pad_width) for _ in range(image_height + 2 * pad_height)]
for i in range(image_height):
    for j in range(image_width):
        padded_image[i + pad_height][j + pad_width] = image[i][j]

eroded_image = [[0] * image_width for _ in range(image_height)]

for i in range(image_height):
    for j in range(image_width):
        match_found = True
        for m in range(se_height):
            for n in range(se_width):
                if se[m][n] == 1 and padded_image[i + m][j + n] != 1:
                    match_found = False
                    break
            if not match_found:
                break
        if match_found:
            eroded_image[i][j] = 1

boundary_image = [[0] * image_width for _ in range(image_height)]
for i in range(image_height):
    for j in range(image_width):
        boundary_image[i][j] = image[i][j] - eroded_image[i][j]
        if boundary_image[i][j] < 0:
            boundary_image[i][j] = 0

for row in boundary_image:
    print(*row)
