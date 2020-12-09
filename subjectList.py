class SubjectList:
    items = []  # list of Subject objects

    def __init__(self):
        print('new SubjectList')

    def add(self, subject):
        self.items.append(subject)

    def remove(self):
        self.items.pop(len(SubjectList.items) - 1)

    def getSubject(self, name):
        return self.items[self.getSubjectIndex(name)]

    def contains(self, name):
        for item in self.items:
            if name == item.getName():
                return True
        return False

    def getSubjectIndex(self, name):
        i = 0
        for item in self.items:
            if name == item.getName():
                return i
            i += 1
        return False  # if subject was not found