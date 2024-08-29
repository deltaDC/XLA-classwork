blank_line = input()
threshold = int(input())

n = int(input())

image = []

for _ in range(n):
    row = list(map(int, input().split()))
    image.append(row)

threshold_image = [[255 if pixel > threshold else 0 for pixel in row] for row in image]

for row in threshold_image:
    print(*row)
