def otsu_threshold(image):
    pixel_values = [pixel for row in image for pixel in row]
    total_pixels = len(pixel_values)
    histogram = [0] * 256
    for pixel in pixel_values:
        histogram[pixel] += 1

    current_max, threshold = 0, 0
    total_sum = sum(i * histogram[i] for i in range(256))
    weight_background = 0
    sum_background = 0

    for t in range(256):
        weight_background += histogram[t]
        if weight_background == 0:
            continue

        weight_foreground = total_pixels - weight_background
        if weight_foreground == 0:
            break

        sum_background += t * histogram[t]
        sum_foreground = total_sum - sum_background

        mean_background = sum_background / weight_background
        mean_foreground = sum_foreground / weight_foreground

        between_class_variance = weight_background * weight_foreground * (mean_background - mean_foreground) ** 2

        if between_class_variance > current_max:
            current_max = between_class_variance
            threshold = t

    return threshold

blank = input()
n = int(input().strip())
image = [list(map(int, input().strip().split())) for _ in range(n)]

threshold_value = otsu_threshold(image)
print(f"Otsu threshold = {threshold_value}")

# 5
# 100 120 110 95 105
# 90 100 115 105 98
# 105 110 105 98 100
# 80 85 95 100 110
# 120 125 130 125 120
