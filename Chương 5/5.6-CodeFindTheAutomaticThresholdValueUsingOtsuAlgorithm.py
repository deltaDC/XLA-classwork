import numpy as np

def otsu_threshold(image):
    # Flatten the image to calculate the histogram
    pixel_values = image.flatten()
    total_pixels = pixel_values.size

    # Calculate the histogram
    histogram, _ = np.histogram(pixel_values, bins=256, range=(0, 256))

    # Initialize variables for Otsu's algorithm
    current_max, threshold = 0, 0
    total_sum = np.sum(np.arange(256) * histogram)
    weight_background = 0
    weight_foreground = 0
    sum_background = 0
    sum_foreground = 0

    # Iterate over all possible threshold values
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
        
        # Calculate the between-class variance
        between_class_variance = weight_background * weight_foreground * (mean_background - mean_foreground) ** 2
        
        # Check if this is the best threshold
        if between_class_variance > current_max:
            current_max = between_class_variance
            threshold = t

    return threshold

# Read input
blank = input()
n = int(input().strip())
image = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    image.append(row)

image = np.array(image)

# Calculate the Otsu threshold
threshold_value = otsu_threshold(image)

# Output the result
print(f"Otsu threshold = {threshold_value}")


# 5
# 100 120 110 95 105
# 90 100 115 105 98
# 105 110 105 98 100
# 80 85 95 100 110
# 120 125 130 125 120