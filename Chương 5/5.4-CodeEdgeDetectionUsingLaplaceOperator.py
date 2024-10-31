import numpy as np

def laplace_operator(image):
    # Laplace kernel
    laplace_kernel = np.array([[0, -1, 0],
                                [-1, 4, -1],
                                [0, -1, 0]])
    
    # Image dimensions
    n = len(image)
    output = np.zeros((n, n), dtype=int)
    
    # Apply the Laplace operator (3x3 window) to each pixel, excluding borders
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            # Calculate the response of the Laplace operator
            laplace_response = np.sum(laplace_kernel * image[i-1:i+2, j-1:j+2])
            # Store the absolute value in the output matrix
            output[i][j] = abs(laplace_response)
    
    return output

# Read input
blank = input()
n = int(input().strip())
image = np.array([list(map(int, input().strip().split())) for _ in range(n)])

# Process the image with the Laplace operator
gradient_image = laplace_operator(image)

# Print output
for row in gradient_image:
    print(" ".join(map(str, row)))