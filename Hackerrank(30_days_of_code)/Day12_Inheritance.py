# defining the base class
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    # defining the derived class with init and passing the input to the the base class Person and storing
    #the extra variable in scores(data type array)
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    #defining calculate function with self argument and returning the grades

    def calculate(self):
        x = int((sum(self.scores) / len(self.scores)))
        if x in range(90, 101):
            return ("O")
        elif x in range(80, 90):
            return ("E")
        elif x in range(70, 80):
            return ("A")
        elif x in range(50, 70):
            return ("P")
        elif x in range(40, 55):
            return ("D")
        else:
            return ("T")


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())