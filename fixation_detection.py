import csv
from math import atan2, degrees
from subjectList import SubjectList
from subject import Subject

# return data from sample row without subject id
# sample is formatted as: [boolean, (x1, y1), (x2, y2),...,(xi, yi)]
def parseSample(row):
    i = 1
    sample = []
    while i < (len(row) - 1):
        if i > 1:  # create point (tuple), add it to the sample list
            x = float(row[i])
            y = float(row[i + 1])
            point = (x, y)
            sample.append(point)
            i += 2
        else:
            # first add the boolean value to the sample list
            sample.append(row[i])
            i += 1
    return sample

# check if current subject is one of the subjects assigned to us (group 4)
def isOurSubject(subjects, subject_id):
    for sub in subjects:
        if (subject_id == sub):
            return True
    return False

# I-DT
# -------------------------------------------------
# PARAMETERS:
# data: a recorded sample of gaze data
# dispersion_threshold: the dispersion threshold in visual degrees
# duration_threshold: the duration threshold in milliseconds
# -------------------------------------------------
# RETURN:
# known-value (decision of the subject concerning the observed image (true = recognized imaged, false = did not recognize))
# a list of fixation centroids for the detected fixations
# a list of fixation durations for the detected fixations
# -------------------------------------------------
def i_dt(data, dispersion_threshold, duration_threshold):
    fix_centroids = []
    fix_durations = []
    known = data[0] #decision of the subject concerning the observed image (true = recognized imaged, false = did not recognize).
    points = data.copy()
    points.pop(0) # pop out the boolean value from the processed data as we don't need it here
    pointer = 0
    while pointer < len(points) and (pointer + duration_threshold) < len(points): # while there still are points
        # initialize window covering duration threshold
        window = points[pointer:(pointer + duration_threshold)]
            
        dispersion = unitsToVisualDegrees(getDispersion(window))
    
        if dispersion <= dispersion_threshold:
            pointer += duration_threshold
            while dispersion <= dispersion_threshold and pointer < len(points):
                window.append(points[pointer])
                dispersion = unitsToVisualDegrees(getDispersion(window))
                pointer += 1
            # dispersion threshold exceeded, note fixation at the centroid of the window points
            centroid = (averageX(window), averageY(window))
            fix_centroids.append(centroid)
            fix_durations.append(len(window))
        else:
            pointer += 1
    return (known, fix_centroids, fix_durations)

def unitsToVisualDegrees(size_in_units):
    height = 11.3  # monitor height in centimeters
    distance = 45.0  # distance between monitor and subject in centimeters
    resolution = 1400  # vertical resolution in units
    
    deg_per_unit = degrees(atan2(.5*height, distance)) / (.5*resolution)

    size_in_deg = size_in_units * deg_per_unit
    return size_in_deg

#Dispersion is defined as dispersion D = [max(x) – min(x)] +[max(y) – min(y)], where (x, y) represent the samples inside the window
def getDispersion(window):
    dispersion = (maxX(window) - minX(window)) + (maxY(window) - minY(window))
    return dispersion

def maxX(window):
    max_x = window[0][0]
    for point in window:
        if point[0] > max_x:
            max_x = point[0]
    return max_x

def minX(window):
    min_x = window[0][0]
    for point in window:
        if point[0] < min_x:
            min_x = point[0]
    return min_x

def maxY(window):
    max_y = window[0][1]
    for point in window:
        if point[1] > max_y:
            max_y = point[1]
    return max_y

def minY(window):
    min_y = window[0][1]
    for point in window:
        if point[1] > min_y:
            min_y = point[1]
    return min_y

def averageX(points):
    total = 0
    for point in points:
        total += point[0]
    return total / len(points)

def averageY(points):
    total = 0
    for point in points:
        total += point[1]
    return total / len(points)
