def isodata_threshold(image, epsilon=0.001):
    pixel_values = [pixel for row in image for pixel in row]
    total_pixels = len(pixel_values)

    histogram = [0] * 256
    for pixel in pixel_values:
        histogram[pixel] += 1

    normalized_histogram = [count / total_pixels for count in histogram]
    t0 = sum(i * normalized_histogram[i] for i in range(256))

    while True:
        lower_class = range(int(t0) + 1)
        upper_class = range(int(t0) + 1, 256)

        sum_lower = sum(normalized_histogram[i] for i in lower_class)
        mean_below = sum(i * normalized_histogram[i] for i in lower_class) / sum_lower if sum_lower > 0 else 0

        sum_upper = sum(normalized_histogram[i] for i in upper_class)
        mean_above = sum(i * normalized_histogram[i] for i in upper_class) / sum_upper if sum_upper > 0 else 0

        new_t0 = (mean_below + mean_above) / 2
        if abs(new_t0 - t0) < epsilon:
            break
        t0 = new_t0

    return round(t0)

n = int(input().strip())
image = [list(map(int, input().strip().split())) for _ in range(n)]
print("Isodata threshold =", isodata_threshold(image))


# 5
# 100 120 110 95 105
# 90 100 115 105 98
# 105 110 105 98 100
# 80 85 95 100 110
# 120 125 130 125 120