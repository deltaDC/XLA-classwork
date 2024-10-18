import numpy as np

def erode(image, se):
    image_height, image_width = image.shape
    se_height, se_width = se.shape

    pad_height = se_height // 2
    pad_width = se_width // 2

    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)

    eroded_image = np.zeros_like(image)  

    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i + se_height, j:j + se_width]
            if np.all((region & se) == se):
                eroded_image[i, j] = 1  

    return eroded_image

def boundary_extraction(image, se):
    eroded_image = erode(image, se)
    boundary_image = image - eroded_image
    boundary_image[boundary_image < 0] = 0  
    return boundary_image

def main():
    blank = input()

    se_size = int(input().strip())
    se = np.zeros((se_size, se_size), dtype=int)
    
    for i in range(se_size):
        se[i] = list(map(int, input().strip().split()))

    image_size = int(input().strip())
    image = np.zeros((image_size, image_size), dtype=int)
    
    for i in range(image_size):
        image[i] = list(map(int, input().strip().split()))

    result = boundary_extraction(image, se)

    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
