#https://www.hackerrank.com/challenges/30-inheritance

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scroes):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scroes

    def calculate(self):
        a = sum(self.scores) / len(self.scores)

        if 100 >= a and 90 <= a:
            return 'O'
        elif 90 > a and 80 <= a:
            return 'E'
        elif 80 > a and 70 <= a:
            return 'A'
        elif 70 > a and 55 <= a:
            return 'P'
        elif 55 > a and 40 <= a:
            return 'D'
        elif 40 > a:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())