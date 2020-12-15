import matplotlib.patches as mpatches
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
    
    circles = []
    for centroid in fixations[1]:
        circles.append(plt.Circle(centroid, 25, fc='blue', fill=True))
    plt.ylim([-1400, 1400])
    plt.xlim([-1400, 1400])
    plt.plot(x, y, 'ro', linewidth=0.1, markersize=0.5)
    for circle in circles:
        plt.gcf().gca().add_artist(circle)
    raw_patch = mpatches.Patch(color='red', label='Raw gaze data')
    fix_patch = mpatches.Patch(color='blue', label='Center of detected fixation')
    plt.legend(handles=[fix_patch, raw_patch])
    plt.show()