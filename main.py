import csv
from subjectList import SubjectList
from subject import Subject
from fixation_detection import isOurSubject, parseSample, i_dt
from draw import drawPointsAndFixations
from write_results import writeResult

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
    

    for subject in dataset.items:
        print(f'{subject.name}: {subject.numberOfSamples()} samples')
        
    # write fixation detection results to a csv file for each subject
    for subject in dataset.items:
        samples = subject.getSamples()
        results = []
        for sample in samples:
            results.append(i_dt(sample, 1, 100))
        writeResult(subject.name, results)
    #drawPointsAndFixations(samples[0], results[0])