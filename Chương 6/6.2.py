import numpy as np
import matplotlib.pyplot as plt

def calculate_signature(x, y):
    dx = np.gradient(x)
    dy = np.gradient(y)
    angles = np.arctan2(dy, dx)
    return np.unwrap(angles)

def plot_signature(shape, angles, arc_length):
    plt.figure(figsize=(8, 4))
    plt.plot(arc_length, angles, label=f"Signature of {shape}")
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.title(f"Shape Signature: {shape}")
    plt.xlabel("Boundary Position (Arc Length)")
    plt.ylabel("Tangent Angle (Radians)")
    plt.legend()
    plt.grid()
    plt.show()

triangle_x = [0, 1, 0.5, 0]
triangle_y = [0, 0, np.sqrt(3)/2, 0]
arc_triangle = np.linspace(0, len(triangle_x)-1, len(triangle_x))
angles_triangle = calculate_signature(triangle_x, triangle_y)
plot_signature("Equilateral Triangle", angles_triangle, arc_triangle)

rectangle_x = [0, 2, 2, 0, 0]
rectangle_y = [0, 0, 1, 1, 0]
arc_rectangle = np.linspace(0, len(rectangle_x)-1, len(rectangle_x))
angles_rectangle = calculate_signature(rectangle_x, rectangle_y)
plot_signature("Rectangle", angles_rectangle, arc_rectangle)

t = np.linspace(0, 2 * np.pi, 100)
a, b = 2, 1
ellipse_x = a * np.cos(t)
ellipse_y = b * np.sin(t)
arc_ellipse = np.linspace(0, len(ellipse_x)-1, len(ellipse_x))
angles_ellipse = calculate_signature(ellipse_x, ellipse_y)
plot_signature("Ellipse", angles_ellipse, arc_ellipse)
