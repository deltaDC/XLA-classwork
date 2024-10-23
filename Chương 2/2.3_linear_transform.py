blank_line = input()
a = float(input())
b = float(input())

n = int(input())

image = []

for _ in range(n):
    row = list(map(int, input().split()))
    image.append(row)

tranformed_image = [
    [min(255, max(0, int(a * pixel + b))) for pixel in row] for row in image
]

for row in tranformed_image:
    print(*row)
