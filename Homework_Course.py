# Simple Student Management

"""
Pseudo code:
1.get name and surname from student
2.ask to student rightly write "Welcome"
3.tryCount = 3
4.get input
5.check, is it equals "Welcome"
    6.yes => print("Login is successful") and go to step  X
    7.no => tryCount -=1 and check tryCount > 0
            8.yes => go to step 4
            9.no => print("Please try again later") and exit.
10.print screen courses.
11.ask to how many courses taken ?
12.this number between 3 and 5 ?
    13.yes =>go to step
    14.no => print("You failed in class") an goto step 11
15.loop selectedCourseCount
16.ask which one ? get course Id
17.selected course check =>  Is there the same course in  list ?
    18.yes => print("You already select this course. Please select another course.") and go to step 13
    19. no => selectedCourseCount -= 1 and check selectedCourseCount == 0
        20.yes => goto step 22
        21.no =>  goto step 16
22.Ask to choose one of the students courses
23.Add the grades from this course.
24.Select random 3 grades number between 0-100. Keep these grades in dictionary.(midterm, final, project)
25.Calculate grades.(midterm %30 , final %50, project %20)
26.Calculated grade is ;
    27. x > 90 , the student get AA
    28. 70 < x < 90  BB
    29. 50 < x < 70 CC
    28. 30 < x < 50 DD
    29. x < 30 FF
30. the student has received FF, print("Sorry, you didn't pass the exam")
31. stop.

"""

import random


class StudentSystem:

    def __init__(self):
        self.students = []
        self.password = "Welcome"
        self.passTryCount = 0
        self.run = True
        self.courses = {0: "Math", 1: "Computer Science", 2: "Physics", 3: "Psychology", 4: "Chemistry"}
        self.onlineStudent = Student()

    def initial(self):
        print('\n' * 10)
        print("************** Welcome to Student Management System **************")
        self.passTryCount = 3
        student = self.newStudent()
        print("Hello " + student.name + " " + student.surname)
        self.getPassword(student)
        self.takeCourseCount()
        self.checkCourseCount()
        self.selectCourse()
        self.chooseExam()
        self.studentGrades()

    def newStudent(self):
        student = Student()
        student.name = input("Please enter a name: ")
        student.surname = input("Please enter a surname: ")
        return student

    def getPassword(self, student):
        print("Please enter the password to login to the system.")
        while self.passTryCount > 0:
            password = input("Password: ")
            if password == self.password:
                print("Right! Login is successful.")
                self.onlineStudent.name = student.name
                self.onlineStudent.surname = student.surname
                break
            else:
                self.passError()
                newCount = self.passTryCount - 1

                if newCount == 0:
                    print("Please try again later")
                    self.initial()
                else:
                    self.passTryCount -= 1

    def passError(self):
        print("Wrong password! Try Again")

    def takeCourseCount(self):
        print('\n' * 3)
        print("You must select course ! \n")
        while True:
            courseCount = input("Please enter the number of course you want to take: ")

            try:
                self.onlineStudent.courseCount = int(courseCount)
                break
            except ValueError:
                print("Please enter number !")

    def checkCourseCount(self):
        while True:
            if 3 <= self.onlineStudent.courseCount <= 5:
                print("Your request has been received.")
                break
            else:
                print("Your failed in class.")
                self.takeCourseCount()

    def selectCourse(self):

        counter = self.onlineStudent.courseCount
        courseListId = []

        for i in range(len(self.courses)):
            courseListId.append(i)

        print("list", courseListId)
        self.printCourseList()
        i = 0
        while i < counter:
            choice = input(f"{i+1}. selection : ")
            if self.checkNumber(choice):
                if int(choice) in courseListId:
                    if int(choice) in self.onlineStudent.courses:
                        print("This course already selected.")
                    else:
                        self.onlineStudent.courses.append(int(choice))
                        i += 1
                else:
                    print("There is no such course!")
            else:
                print("Invalid Value")

    def checkNumber(self, number):

        try:
            int(number)
            return True

        except ValueError:
            return False

    def printCourseList(self):
        print('\n' * 3)
        print("Please enter the course Id you want to take")
        for i in range(len(self.courses)):
            print(f"       *{self.courses.get(i)} => {i}")

    def chooseExam(self):
        print("\nYour courses :")
        for i in self.onlineStudent.courses:
            print(f" {self.courses.get(i)} => {i}")

        while True:
            choice = input("\nChoose the exam you want to take: ")
            if self.checkNumber(choice):
                if int(choice) in self.onlineStudent.courses:
                    self.onlineStudent.selectedExam = int(choice)
                    break
            else:
                print("Invalid Value")

    def studentGrades(self):
        midterm = self.randomGrades()
        final = self.randomGrades()
        project = self.randomGrades()

        grades = {"midterm": midterm, "final": final, "project": project}
        print(grades)
        result = self.calculatorResult(midterm, final, project)
        if result == "FF":
            print(f"{self.onlineStudent.name} {self.onlineStudent.surname} failed {self.courses[self.onlineStudent.selectedExam]} course. ")
        else:
            print(f"Your got a {result} from {self.courses[self.onlineStudent.selectedExam]} course. ")

    def randomGrades(self):
         return random.randrange(0, 100, 1)

    def calculatorResult(self, midterm, final, project):
        point = (midterm*0.3)+(final*0.5)+(project*0.2)
        if point > 90:
            return "AA"
        elif 70 < point < 90:
            return "BB"
        elif 50 < point < 70:
            return "CC"
        elif 30 < point < 50:
            return "DD"
        elif point < 30:
            return "FF"

class Student:

    def __init__(self):
        self.name = ""
        self.surname = ""
        self.courseCount = 0
        self.courses = []
        self.selectedExam = -1


ssm = StudentSystem()
ssm.initial()
