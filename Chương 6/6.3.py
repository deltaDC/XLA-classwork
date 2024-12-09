import matplotlib.pyplot as plt
import numpy as np

def draw_circle_medial_axis():
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), 1, color='blue', fill=False)
    ax.add_artist(circle)
    ax.plot([0], [0], 'ro')  # Medial axis
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    plt.title("Medial Axis of a Circle")
    plt.show()

def draw_square_medial_axis():
    fig, ax = plt.subplots()
    square = plt.Polygon([[-1, -1], [1, -1], [1, 1], [-1, 1]], color='blue', fill=False)
    ax.add_artist(square)
    ax.plot([0, 0], [-1, 1], 'r--')  # Vertical medial axis
    ax.plot([-1, 1], [0, 0], 'r--')  # Horizontal medial axis
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    plt.title("Medial Axis of a Square")
    plt.show()

def draw_rectangle_medial_axis():
    fig, ax = plt.subplots()
    rectangle = plt.Polygon([[-2, -1], [2, -1], [2, 1], [-2, 1]], color='blue', fill=False)
    ax.add_artist(rectangle)
    ax.plot([0, 0], [-1, 1], 'r--')  # Vertical medial axis
    ax.plot([-2, 2], [0, 0], 'r--')  # Horizontal medial axis
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    plt.title("Medial Axis of a Rectangle")
    plt.show()

def draw_triangle_medial_axis():
    fig, ax = plt.subplots()
    triangle = plt.Polygon([[0, np.sqrt(3)], [-1, 0], [1, 0]], color='blue', fill=False)
    ax.add_artist(triangle)
    ax.plot([0, -0.5], [np.sqrt(3)/2, 0], 'r--')  # Medial axis to left corner
    ax.plot([0, 0.5], [np.sqrt(3)/2, 0], 'r--')  # Medial axis to right corner
    ax.plot([0, 0], [np.sqrt(3)/2, np.sqrt(3)/2], 'ro')  # Apex of medial axes
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 2)
    ax.set_aspect('equal')
    plt.title("Medial Axis of an Equilateral Triangle")
    plt.show()

draw_circle_medial_axis()
draw_square_medial_axis()
draw_rectangle_medial_axis()
draw_triangle_medial_axis()
