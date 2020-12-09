import csv
from subjectList import SubjectList
from subject import Subject
from fixation_detection import isOurSubject, parseSample, i_dt

# main code block
our_subjects = ['s4', 's6', 's12', 's18', 's20',
            's26', 's32', 's34']  # group 4 subjects
dataset = SubjectList()
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
                newSubject = Subject(row[0])
                newSubject.addSample(sample)
                dataset.add(newSubject)

        i += 1
    print(dataset.items[0].samples[0][1])
    print(dataset.items[1].samples[0][1])
"""     test = dataset.getSubject('s4')
    samples = test.getSamples()
    print(test.name)
    print(test.samples[0][2])
    print(i_dt(samples[1], 1, 100)) """