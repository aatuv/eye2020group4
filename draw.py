import matplotlib.pyplot as plt
import numpy as np

def drawPointsAndFixations(points, fixations):
    x  = []
    y = []
    i = 0
    for point in points:
        if i > 0:
            x.append(point[0])
            y.append(point[1])
        i += 1

    figure, axes = plt.subplots()
    
    circles = []
    for centroid in fixations[1]:
        circles.append(plt.Circle(centroid, 80, fill=False))
    plt.plot(x, y, 'ro-', linewidth=0.1, markersize=0.5)
    for circle in circles:
        plt.gcf().gca().add_artist(circle)
    plt.show()