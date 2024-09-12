import numpy as np


def apply_mean_filter(matrix):
    # Convert the input matrix to a NumPy array
    matrix = np.array(matrix)
    rows, cols = matrix.shape

    # Prepare an empty list to store the output matrix
    filtered_matrix = []

    # Iterate over the matrix excluding the border elements
    for i in range(1, rows - 1):
        row = []
        for j in range(1, cols - 1):
            # Extract the 3x3 neighborhood
            neighborhood = matrix[i - 1:i + 2, j - 1:j + 2]
            # Compute the mean of the 3x3 neighborhood with 1/9 weight for each
            mean_value = np.sum(neighborhood) / 9
            row.append(int(mean_value))
        filtered_matrix.append(row)

    return np.array(filtered_matrix)


# Input for Case 1
n = 4  # Size of the square matrix
input_matrix = [
    [50, 150, 200, 50],
    [75, 180, 30, 220],
    [160, 40, 90, 120],
    [210, 70, 250, 25]
]

# Apply the mean filter
output_matrix = apply_mean_filter(input_matrix)

# Display the result
for row in output_matrix:
    print(*row)
