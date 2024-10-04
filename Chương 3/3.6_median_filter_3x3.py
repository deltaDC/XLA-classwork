def find_median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:  # Even number of elements
        mid1 = sorted_list[(n // 2) - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

blank_line = input()
n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

median_matrix = []
for row in range(1, n - 1):
    median_row = []
    for col in range(1, n - 1):
            neighborhood = []
            for j in range(row - 1, row + 2):
                for k in range(col - 1, col + 2):
                    neighborhood.append(matrix[j][k])
            median_row.append(find_median(neighborhood))
    median_matrix.append(median_row)

for row in median_matrix:
    print(*row)

# 4
# 50 150 200 50
# 75 180 30 220
# 160 40 90 120
# 210 70 250 25
