blank_line = input()
n = int(input())

image = []

for _ in range(n):
    row = list(map(int, input().split()))
    image.append(row)

negative_image = [[255 - pixel for pixel in row] for row in image]

for row in negative_image:
    print(*row)
