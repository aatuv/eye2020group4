import csv
from subjectList import SubjectList
from subject import Subject
from fixation_detection import isOurSubject, parseSample, i_dt
from draw import drawPointsAndFixations

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
        
    # test the algorithm:
    # 1. take one of the subjects
    # 2. run one of the subject's samples through the algorithm. NOTE: try to play around with different settings
    # 3. print results

    test = dataset.getSubject('s6')
    samples = test.getSamples()
    result = i_dt(samples[0], 1, 100)

    print(f'Subject: {test.name}')
    print(f'Recognized image: {result[0]}')
    print(f'Fixation centroids (x, y): {result[1]}')
    print(f'Fixation durations (ms): {result[2]}')

    print('drawing data...')
    drawPointsAndFixations(samples[0], result)