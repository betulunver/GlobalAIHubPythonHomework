# User Identification Program

# The user will be defined. Get the data of this user by input method. Obtain information from user as follow :

# First Name
# Last Name
# Age
# Date of birth (just year)

# Pass the user's information to the list and displays the screen using the for loop. Print all user information on the screen.

# If he is under18, print "You can't go out because it's too dangerous" the screen.

# If he is over 18, print "You can go out to the street." on the screen.

user = []
firstname = input("Please enter your firstname: ")
user.append(firstname)
lastname = input("Please enter your lastname: ")
user.append(lastname)
while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except:
        print("It is not a number.!")

user.append(age)

while True:
    try:
        birthYear = int(input("Please enter your date of birth (just year): "))
        break
    except:
        print("It is not a year.!")
user.append(birthYear)

for i in user:
    print(i)

if user[2] < 18:
    print("You cant go out because is too dangerous.")
elif user[2] > 18:
    print("You can go out to the street.")
else:
    print("Invalid value")
