def find_average(list):
    return sum(list) / len(list)

blank_line = input()
n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

avg_matrix = []
for row in range(1, n - 1):
    avg_row = []
    for col in range(1, n - 1):
            neighborhood = []
            for j in range(row - 1, row + 2):
                for k in range(col - 1, col + 2):
                    neighborhood.append(matrix[j][k])
            avg_row.append(round(find_average(neighborhood)))
    avg_matrix.append(avg_row)

for row in avg_matrix:
    print(*row)

# 4
# 50 150 200 50
# 75 180 30 220
# 160 40 90 120
# 210 70 250 25

# 4
# 2 7 3 0
# 3 1 6 3
# 0 1 3 5
# 3 6 7 1