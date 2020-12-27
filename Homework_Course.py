
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
    28. 70 > x > 90  BB
    29. 50 > x > 70 CC
    28. 30 > x > 50 DD
    29. x <30 FF
30. the student has received FF, print("Sorry, you didn't pass the exam")
31. stop.

"""
