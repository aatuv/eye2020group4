from subjectList import SubjectList
# tl;dr: a Subject object has a name or id (i.e. s4 or s8) and all its samples (a list of lists).
# a sample is a row from the train.csv file, but without the subject identifier.
class Subject(SubjectList):
    name = ''
    samples = []

    def __init__(self, name):
        self.name = name

    def addSample(self, sample):
        self.samples.append(sample)

    def getName(self):
        return self.name

    def getSamples(self):
        return self.samples