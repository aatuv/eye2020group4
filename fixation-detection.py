import csv

class SubjectList:
    items = [] # list of Subject objects

    def __init__(self):
        print('new SubjectList')

    def add(self, subject):
        SubjectList.items.append(subject)

    def remove(self):
        SubjectList.items.pop(len(SubjectList.items) - 1)
    
    def getSubject(self, name):
        return SubjectList.items[self.getSubjectIndex(name)]

    def contains(self, name):
        for item in SubjectList.items:
            if name == item.getName:
                return True
        return False

    def getSubjectIndex(self, name):
        i = 0
        for item in SubjectList.items:
            if name == item.getName:
                return i
            i += 1
        return False # if subject was not found

# tl;dr: a Subject object has a name or id (i.e. s4 or s8) and all it's samples (a list of lists).
# a sample is a row from the train.csv file, but without the subject identifier. 
class Subject(SubjectList):
    name = ''
    samples = []

    def __init__(self, name):
        self.name = name
    
    def addSample(self, sample):
        Subject.samples.append(sample)
    
    def getName(self):
        return Subject.name

    def getSamples(self):
        return Subject.samples

# return data from sample row without subject id
def parseSample(row):
    i = 0
    sample = []
    for column in row:
        if i > 0:
            sample.append(column)
        i += 1
    return sample

# check if current subject is one of the subjects assigned to us (group 4)
def isOurSubject(subject):
    for sub in subjects:
        if (subject == sub):
            return True
    return False

# main code block
subjects = ['s4', 's6', 's12', 's18', 's20', 's26', 's32', 's34'] # group 4 subjects
dataset = SubjectList()
with open('train.csv') as data:
        csv_reader = csv.reader(data, delimiter=",")
        i = 0
        for row in csv_reader:
            if isOurSubject(row[0]):
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


def i_dt(data, dispersion_threshold, duration_threshold):
    # TODO: implement the I-DT algorithm
    window = []