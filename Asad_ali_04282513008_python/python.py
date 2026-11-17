# x=2
# y=3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x//y)


# s = "asad"
# u = "ali"
# t = "rajput"
# print(s+u+t)

# x= input("enter the string: ")
# print(x)
# print(x[0:4])
# print(x.endswith('asd'))




# print('Asad')
# print("Asad")
# print("""Asad""")

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# num3 = input("Enter the third number: ")
# if (num1 > num2) and (num1 > num3):
#         max = num1
# elif (num2 > num1) and (num2 > num3):
#     max = num2
# else:
#     max = num3
# print ("maximum is: ",max)
# if (num1 < num2) and (num1 < num3):
#         min = num1
# elif (num2 < num1) and (num2 < num3):
#     min = num2
# else:
#     min = num3
# print ("minimum is: ",min)


# x='asad'
# x = x.upper() #makes all letters uppercase
# y= x.capitalize() #makes the first letter uppercase and the rest lowercase
# print(x)
# print(y)


# str = input("Enter a string: ")
# target = input("enter the target char: ")
# index = str.find(target)
# print("The index of the target character is:", index)

# ra=range(1,9)
# print (ra)
# for i in ra:
#     print(i)


# print(list(range(1, 9)))


# while (True):
    # num = int(input("Enter a number: "))
    # if num < 0:
    #     break
    # print("You entered:", num)


# x = 'i am asad rajput'
# print(x[0:-1])

# class student:
#     def __init__(self, ID, NAM):
#         self.ID=ID
#         self.name=NAM

#     def display(self):
#         print(self.ID,self.name)

# std1 =student(123,'asad')
# print("The values through parameterized constructor are: ")
# std1.display()


# class Student:
#     def __init__(self, name, age, roll_no, department):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#         self.department = department

#     def display_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Roll No:", self.roll_no)
#         print("Department:", self.department)


# Creating student objects
# student1 = Student("Ali", 20, 101, "Bioinformatics")


# Display information
# student1.display_info()
# print()


# for i in range (1,6):
#     print(i)

# for i in range (1,20,2):
#     print(i)

# for i in range (100,1,-10):
#     print(i)

# for i in range (-100,0,10):
#     print(i)



# x = input("Enter a value: ") #enter the number and the type will be string
# print(type(x)) 

# x = int(input("Enter a value: ")) #enter the number and the type will be integer
# print(type(x))


# import array as arr
# a = arr.array('d', [1.02, 2.32, 3.45, 3.65, 2.34])
# print(a[0])
# print(a.typecode)
# print(a.index(2.32)) #gives the index of the values 1st occurance
# print(a.pop())
# print(a.pop(1)) #removes the value at index 1
# print(a)

# for i in range(100): #from 0 to 99
#     print(i)

# class employee:
#     name = "Asad"
#     age = 23
# print(employee.name)
# print(employee.age)

# class employee:
#     def __init__(self, Full_Name, ID, Caste, Salary,):
#         self.name = Full_Name
#         self.ID = ID
#         self.Caste = Caste
#         self.Salary = Salary

# e1 =employee('Asad Ali', 213, 'Rajput', 230000000)
# print(e1.name, e1.ID, e1.Salary, e1.Caste)


# x = input('enter the number') #it will only cause the concatenation
# y = input('enter the number')
# print(x+y)

# x = int(input('enter the number')) #it will cause the the addition
# y = int(input('enter the number'))
# print(x+y)

# x=2.0
# y=2
# print(type(x/y)) #float

# x=2
# y=2.0
# print(type(x/y)) #float

# x=2
# y=2
# print(type(x/y)) #float

# x=2.0
# y=2
# print(type(x*y)) #float

# x=2.0
# y=2
# print(type(x/y)) #float

# y= 2*2
# print(type(y)) #int

# import math
# x=math.floor(-98.87)
# print(x)

# d=[1,2,4]
# for i in d:
#     print(i)
#     print(d)

#x=100
#while(x>=0):
    #print(x)
    #x-=1

# str='welcome everyone'
# x=str[:8]+'python'
# print(x)

# str='welcome everyone python'
# str1='python'
# print(str.find(str1,0))

# str='welcome everyone python  python'
# str1='python'
# print(str.rfind(str1,0))#gives the index of the last occurance of the value in the string


# str='welcome everyone python  python'
# str1='python'
# print(str.find(str1,0))#gives the index of the first occurance of the value in the string  

# import array
# arr=array.array('i',[1,2,3]) 

# for num in arr:
    # print(num)


