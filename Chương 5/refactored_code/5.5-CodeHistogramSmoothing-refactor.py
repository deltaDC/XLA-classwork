def smooth_histogram(histogram, window_size):
    smoothed = []
    n = len(histogram)
    half_window = window_size // 2

    for i in range(n):
        start = max(0, i - half_window)
        end = min(n, i + half_window + 1)

        window = histogram[start:end]
        smoothed_value = round(sum(window) / len(window))
        smoothed.append(smoothed_value)

    return smoothed


blank = input()
n = int(input().strip())
levels = list(map(int, input().strip().split()))
histogram = list(map(int, input().strip().split()))

smoothed_w3 = smooth_histogram(histogram, window_size=3)
smoothed_w5 = smooth_histogram(histogram, window_size=5)

print("Smoothed Histogram w=3")
print(" ".join(map(str, levels)))
print(" ".join(map(str, smoothed_w3)))

print("Smoothed Histogram w=5")
print(" ".join(map(str, levels)))
print(" ".join(map(str, smoothed_w5)))
