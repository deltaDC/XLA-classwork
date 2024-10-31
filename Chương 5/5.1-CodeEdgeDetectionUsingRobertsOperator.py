import numpy as np

def roberts_operator(image):
    # Roberts Cross operator kernels
    Gx_kernel = np.array([[1, 0], [0, -1]])
    Gy_kernel = np.array([[0, 1], [-1, 0]])
    
    # Image dimensions
    n = len(image)
    output = np.zeros((n, n), dtype=int)
    
    # Apply Roberts operator by correctly centering the 2x2 window
    for i in range(1, n - 1):  # Start from 1 and go up to n-2 to avoid borders
        for j in range(1, n - 1):
            # Calculate Gx and Gy using Roberts kernels on a 2x2 window
            Gx = (image[i][j] * Gx_kernel[0][0] +
                  image[i][j + 1] * Gx_kernel[0][1] +
                  image[i + 1][j] * Gx_kernel[1][0] +
                  image[i + 1][j + 1] * Gx_kernel[1][1])
            
            Gy = (image[i][j] * Gy_kernel[0][0] +
                  image[i][j + 1] * Gy_kernel[0][1] +
                  image[i + 1][j] * Gy_kernel[1][0] +
                  image[i + 1][j + 1] * Gy_kernel[1][1])
            
            # Calculate gradient magnitude and place it in the center of the 2x2 window
            output[i][j] = int(np.sqrt(Gx**2 + Gy**2))
    
    # Reverse the matrix vertically and horizontally
    reversed_output = np.flipud(np.fliplr(output))
    
    return reversed_output

# Read input
blank = input()
n = int(input().strip())
image = [list(map(int, input().strip().split())) for _ in range(n)]

# Process the image with the Roberts operator
gradient_image = roberts_operator(image)

# Print output
for row in gradient_image:
    print(" ".join(map(str, row)))