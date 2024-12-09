import numpy as np
import matplotlib.pyplot as plt


square_boundary = [
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 1),
    (0, 0)
]


x, y = zip(*square_boundary)


angles = []
for i in range(len(square_boundary) - 1):
    dx = x[i + 1] - x[i]
    dy = y[i + 1] - y[i]
    angle = np.arctan2(dy, dx)
    angles.append(np.degrees(angle))


arc_length = np.arange(len(angles) + 1)


angles.append(angles[0])


plt.figure(figsize=(8, 4))
plt.plot(arc_length, angles, marker='o', label="Tangent Angle")
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.title("Signature of a Square Boundary")
plt.xlabel("Boundary Position (Arc Length)")
plt.ylabel("Tangent Angle (Degrees)")
plt.xticks(arc_length)
plt.legend()
plt.grid()
plt.show()
