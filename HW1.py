
# DAY0 Homework

# take 5 values from user and write a program that prints the values you get on the screen.
# old
value0 = input("Please enter value: ")
value1 = input("Please enter value: ")
value2 = input("Please enter value: ")
value3 = input("Please enter value: ")
value4 = input("Please enter value: ")

# new 
list = []

for i in range(5):
    list.append(input("Please enter value: "))
    
print(list)

# print the type of values you received in this program on the screen.

data0 = 5
data1 = 3.9
data2 = [3, 5, 7]

#old

print(type(data0))
print(type(data1))
print(type(data2))

# new
list = [data0, data1, data2]
for i in list:
    print(type(i))


# when using print functions, do not forget to use f-string and format usage in your program.

# f-string
print(f'Data0  : {data0}')

# .format
print("Data1 : {}".format(data1))

