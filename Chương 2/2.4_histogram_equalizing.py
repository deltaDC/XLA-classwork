import math

blank_line = input()
m, n = map(int, input().split())

levels = int(input()) - 1

histogram = []

for _ in range(m):
    row = list(map(int, input().split()))
    histogram.append(row)

max_num = max(max(row) for row in histogram)

cnt = [0] * (max_num + 1)

for row in histogram:
    for ele in row:
        cnt[ele] += 1

p = []

for i in range(max_num + 1):
    p.append(cnt[i] / (m * n))

s = []

for i in range(max_num + 1):
    s.append(sum(p[:i + 1]) * levels)

s = [math.ceil(value) if (value - math.floor(value)) >= 0.5 else math.floor(value) for value in s]

for i in range(m):
    for j in range(n):
        print(s[histogram[i][j]], end=' ')
    print()

# 5 4
# 8
# 1 2 0 4
# 1 0 0 7
# 2 2 1 0
# 4 1 2 1
# 2 0 1 1

# 5 5
# 8
# 0 5 0 5 5
# 1 7 6 6 7
# 5 5 6 2 7
# 6 6 7 5 6
# 0 1 5 0 2