import numpy as np

def smooth_histogram(histogram, window_size):
    # Create an array to hold the smoothed values
    smoothed = []
    n = len(histogram)

    # Calculate half of the window size
    half_window = window_size // 2

    # Smooth the histogram using the moving average
    for i in range(n):
        # Determine the start and end of the window
        start = max(0, i - half_window)
        end = min(n, i + half_window + 1)  # +1 because the end index is exclusive

        # Extract the window
        window = histogram[start:end]

        # Calculate the mean of the window
        smoothed_value = int(np.round(np.mean(window)))  # Round to the nearest integer
        smoothed.append(smoothed_value)

    return smoothed

# Read input
blank = input()
n = int(input().strip())
levels = list(map(int, input().strip().split()))
histogram = list(map(int, input().strip().split()))

# Smooth the histogram for window sizes 3 and 5
smoothed_w3 = smooth_histogram(histogram, window_size=3)
smoothed_w5 = smooth_histogram(histogram, window_size=5)

# Print results
print("Smoothed Histogram w=3")
print(" ".join(map(str, levels)))
print(" ".join(map(str, smoothed_w3)))

print("Smoothed Histogram w=5")
print(" ".join(map(str, levels)))
print(" ".join(map(str, smoothed_w5)))


# 20
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# 10 20 35 25 15 5 3 2 1 0 0 0 0 0 0 0 0 0 0 0