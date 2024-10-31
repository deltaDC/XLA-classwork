def isodata_threshold(image, epsilon=0.001):
    # Flatten the image to calculate the histogram
    pixel_values = [pixel for row in image for pixel in row]
    total_pixels = len(pixel_values)

    # Calculate the histogram
    histogram = [0] * 256
    for pixel in pixel_values:
        histogram[pixel] += 1

    # Normalize the histogram
    normalized_histogram = [count / total_pixels for count in histogram]

    # Initialize the threshold t0 as the weighted mean of the histogram
    t0 = sum(i * normalized_histogram[i] for i in range(256))

    while True:
        # Calculate the weights of the two classes
        class1 = normalized_histogram[:int(t0) + 1]
        class2 = normalized_histogram[int(t0) + 1:]

        # Compute the means of the two classes
        weight1 = sum(class1)
        weight2 = sum(class2)

        if weight1 > 0:
            mean_below = sum(i * class1[i] for i in range(len(class1))) / weight1  # Mean of class1
        else:
            mean_below = 0

        if weight2 > 0:
            mean_above = sum((i + int(t0) + 1) * class2[i] for i in range(len(class2))) / weight2  # Mean of class2
        else:
            mean_above = 0

        # Calculate new threshold
        new_t0 = (mean_below + mean_above) / 2

        # Check for convergence
        if abs(new_t0 - t0) < epsilon:
            break
        
        t0 = new_t0

    return round(t0)  # Round to nearest integer

# Read input
n = int(input().strip())
image = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    image.append(row)

# Calculate the Isodata threshold
threshold_value = isodata_threshold(image)

# Output the result
print(f"Isodata threshold = {threshold_value}")

# 5
# 100 120 110 95 105
# 90 100 115 105 98
# 105 110 105 98 100
# 80 85 95 100 110
# 120 125 130 125 120  