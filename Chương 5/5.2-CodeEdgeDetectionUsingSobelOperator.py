import numpy as np

def sobel_operator(image):
    # Sobel kernels
    Gx_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy_kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    
    # Image dimensions
    n = len(image)
    output = np.zeros((n, n), dtype=int)
    
    # Apply the Sobel operator (3x3 window) to each pixel, excluding borders
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            # Calculate Gx and Gy by applying the Sobel kernels
            Gx = np.sum(Gx_kernel * image[i-1:i+2, j-1:j+2])
            Gy = np.sum(Gy_kernel * image[i-1:i+2, j-1:j+2])
            
            # Calculate the gradient magnitude
            output[i][j] = int(np.sqrt(Gx**2 + Gy**2))
    
    return output

# Read input
blank = input()
n = int(input().strip())
image = np.array([list(map(int, input().strip().split())) for _ in range(n)])

# Process the image with the Sobel operator
gradient_image = sobel_operator(image)

# Print output
for row in gradient_image:
    print(" ".join(map(str, row)))
