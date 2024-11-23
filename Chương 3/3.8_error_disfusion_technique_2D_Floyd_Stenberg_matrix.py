def error_diffusion(image):
    height = len(image)
    width = len(image[0])
    output_image = [[0] * width for _ in range(height)]

    threshold = 127

    for y in range(height):
        for x in range(width):
            old_pixel = image[y][x]

            new_pixel = 255 if old_pixel > threshold else 0

            output_image[y][x] = new_pixel

            error = old_pixel - new_pixel

            if x + 1 < width:
                image[y][x + 1] += error * 7 / 16
            if y + 1 < height:
                image[y + 1][x] += error * 5 / 16
                if x + 1 < width:
                    image[y + 1][x + 1] += error * 1 / 16
            if y + 1 < height and x - 1 >= 0:
                image[y + 1][x - 1] += error * 3 / 16

            image[y][x] = max(0, min(255, image[y][x]))

    return output_image

    
blank = input()

image_size = int(input().strip())
image = []

for _ in range(image_size):
    row = list(map(int, input().strip().split()))
    image.append(row)

result = error_diffusion(image)

for row in result:
    print(*row)

# 4
# 50 150 200 50
# 75 180 30 220
# 160 40 90 120
# 210 70 250 25
