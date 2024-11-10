import numpy as np

def isodata_threshold(image, epsilon=0.001):
    pixels = image.flatten()
    
    hist, bins = np.histogram(pixels, bins=256, range=(0, 255))
    
    p = hist / np.sum(hist)
    
    t0 = np.sum(np.arange(256) * p)
    
    while True:
        group1 = p[:int(t0)]  
        group2 = p[int(t0):] 
        
        mean1 = np.sum(np.arange(int(t0)) * group1) / np.sum(group1) if np.sum(group1) != 0 else 0
        mean2 = np.sum(np.arange(int(t0), 256) * group2) / np.sum(group2) if np.sum(group2) != 0 else 0
        
        t_new = (mean1 + mean2) / 2
        
        if abs(t_new - t0) < epsilon:
            break
        
        t0 = t_new
    
    return int(t_new)

blank = input()
n = int(input())

image = []
for i in range(n):
    row = list(map(int, input().split()))
    image.append(row)

image = np.array(image)

threshold = isodata_threshold(image)

print(threshold)
