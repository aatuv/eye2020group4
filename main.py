import csv, time
from subjectList import SubjectList
from subject import Subject
from fixation_detection import isOurSubject, parseSample, i_dt
from draw import drawPointsAndFixations
from write_results import writeResult
from calculate_values import calculateMFL_MSA
# main code block
our_subjects = ['s4', 's6', 's12', 's18', 's20',
            's26', 's32', 's34']  # group 4 subjects
dataset = SubjectList()
subject = globals()["Subject"]
with open('train.csv') as data:
    csv_reader = csv.reader(data, delimiter=",")
    i = 0
    for row in csv_reader:
        if isOurSubject(our_subjects, row[0]):
            if dataset.contains(row[0]):
                sample = parseSample(row)
                subjectIndex = dataset.getSubjectIndex(row[0])
                dataset.items[subjectIndex].addSample(sample)
            else:
                sample = parseSample(row)
                dataset.add(Subject(row[0], [sample]))

        i += 1
        
    # write results as csv
    dis_threshold = 1 # for the i-dt algorithm
    dur_threshold = 200 # for the i-dt algorithm
    current_time_ms = int(round(time.time() * 1000)) # for naming the csv file for the calculations
    filename = f'calculations_{current_time_ms}'
    for subject in dataset.items:
        samples = subject.getSamples()
        results = []
        for sample in samples:
            results.append(i_dt(sample, dis_threshold, dur_threshold))
        #writeResult(subject.name, results)
        calculateMFL_MSA(filename, subject.name[1:], results)

""" 
s_26 = dataset.getSubject('s26')
s_26_samples = s_26.getSamples()
s_26_result = i_dt(s_26_samples[6], 1, 100)
drawPointsAndFixations(s_26_samples[6], s_26_result) """