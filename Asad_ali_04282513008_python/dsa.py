# print(abs(6))   
# print(abs(-6)) #changes negative to positive



# print(str1.replace("is", "was")) #replaces the first string with second string
# print(str1.replace("21", "was"))

# print(str2.find("3")) #finds the index of the first occurrence of the specified value

# print(str2[2:5]) #slices the string from index 2 to 4

# """type casting( changing the data type of a variable (implicit termed as coercion and explicit, 
#  often referred to as casting))"""""
# print(type(4)) #prints the type of the variable

# # implicit type casting( automatically converting one data type to another)
# x = 5
# y = 2.0
# z = x / y
# print(type(z)) 

# # explicit type casting( manually converting one data type to another( user-defined))
# x= 5
# y = "Asad"
# # z= s+y gives type error because we cannot add int and str
# z = str(x) + y
# print(type(z))

# """Python is a high level programming language which is:

# 1.Interpreted 
# a language in which code is executed by an interpreter.
# - Python uses an interpreter to execute your code.
# - It generally executes instructions at runtime.
# - You don't normally need to compile the entire program manually before running it.

# 2.Interactive
# allows you to write and execute code directly, one instruction at a time, and see the result immediately.
# - You don't need to write a complete program.
# - You can test small pieces of code.
# - Python provides an interactive shell (Python REPL).

# 3.Object-Oriented
# is a programming approach based on classes and objects.
# - A class is a blueprint or template.
# - An object is an instance of a class.
# - Objects can contain data and functions.

# 4.Dynamic programming language (meaning that the data types are checked at runtime)

# 5.Open source model (meaning that the source code is freely available and can be modified and distributed by anyone)"""

# #variables (are immutable)

# x,y,z =1,2,3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y) #gives float value
# print(x//y) #gives integer value( uses floor division)
# print(x%y)

# # The ceil() function returns the smallest integer that is greater than or equal to the given number.
# # In simple words, it rounds a number upward to the nearest integer.

# import math
# print(math.ceil(4.277)) #returns 5
# print(math.ceil(-4.277)) #returns -4

# # The exp() function calculates the exponential value of a number.
# print(math.exp(1)) #returns e (Euler's number) 

# # Floating Absolute Value
# # The fabs() function also returns the absolute value of a number, just like abs().
# # However, fabs() always returns the result as a floating-point number (decimal form).
# print(math.fabs(-4.277)) #returns 4.277
# print(math.fabs(-4)) #returns 4.0

# # The floor() function returns the largest integer that is not greater than the given number.
# # In simple words, it rounds a number downward to the nearest integer.
# print(math.floor(98.87)) # returns 98
# print(math.floor(-98.87)) # returns -99

# # The log() function returns the natural logarithm of a number.
# # Natural logarithm means logarithm with base e, where e is approximately 2.71828.
# print(math.log(2.71828)) # returns 1.0

# # The log10() function returns the logarithm of a number with base 10.
# print(math.log10(100)) # returns 2.0

# print(max(1, 2, 3, 4, 5)) #returns the maximum value
# print(min(1, 2, 3, 4, 5)) #returns the minimum value

# # conditional statements
# s=int(input("enter the number: ")) 
# if (s>3):
#     print("s is greater than 3")
# elif(s==3):
#     print("s is equal to 3")
# else:
#     print("s is less than 3")

# # for statements
# s= [1,2,3,4,5]
# for num in s:
#     print(num) #prints all the numbers in the list
#     print(s) #prints the whole list 5 times because the print(s) is inside the for loop

# for num in s: #gives the number in the list
#     if (num%2==0):
#         print(num,"is even")
#     else:
#         print(num,"is odd")

# for i in range(len(s)): # gives the postion of the number in the list
#     if (s[i]%2==0):
#         print(i,"postion is even")
#     else:
#         print(i, "postion is odd")

# print(list(range(0,10))) #gives the range of numbers from 0 to 9
# print(list(range(0,10,2))) #gives the range of numbers from 0 to 9 with a step of 2

# # While loop is used to iterate over a block of code as long as the test expression(condition) is true.
# s=5
# while (s>0):
#     print(s)
#     s-=1 #decreases the value of s by 1

# s="AhSAD ALI"  #break statement ends the program as then doesn't move onward if the condition becomes true
# i =len(s)-1
# while (i>=0):   #print the string in reverse order
#     if(s[i]=="h"):
#         break
#     else:
#         print(s[i])
#     i-=1

# for x in s: #prints the string in forward order
#     if(x=='h'):
#         break
#     else:
#         print(x)

# for x in s:
#     if(x=='h'):
#         continue
#     else:
#         print(x) #skips the letter h and prints the rest of the string

# #The pass statement is a null operation (nothing happens when it executes).
# #It creates minimal classes( empty classes with no methods or attributes)
# for x in s:
#     if(x=='h'):
#         pass
#     else:
#         print(x) #skips the letter h and prints the rest of the string

# # Trying to access a character in a string out of the index range will raise an IndexError( : is slicing operator) if index is float then type error
# str ="strictly"
# print(str[0:3]) #prints the first 3 letters of the string
# print(str[3:]) #prints the string from index 3 to the end
# print(str[:3]) #prints the first 3 letters of the string
# print(str[:]) #prints the whole string
# print(str[0:-1])
# print(str[-2:-1])
# print(str[-1]) #prints the last letter of the string
# print(str[0:-1:2]) #prints the string from index 0 to the second last letter with a step of 2

# we can delete a total string but can not change or delete a character in it because strings are immutable we can also update a string 
# del str
# str = "ASAD ALI AD"
# str1 ="asad Ali"
# newstr = (str[:5] + "RAJPUT") 
# print(newstr)

# print(str.find("AD",0,1)) #gives -1 because the string "AD" is not found in the range of index 0 to 1
# print(str.find("AD",0,5))
# print(str.rfind("AD",0)) #finds the last occurrence of the specified value 9

# if (str.startswith("AS")):
#     print("true")
# if (str.endswith("AD")):
#     print("true")
# if (str.isupper()): #these check whether the string is in upper case or lower case for all the letters in string
#     print("true")
# if (str1.islower()):
#     print("true")
# else:
#     print("false")

# print(str.capitalize()) #makes first letter capital just
# print(str.upper()) #makes all letters capital
# print(str.lower()) #makes all letters lowercase
# print(str.swapcase()) #makes all letters uppercase to lowercase and vice versa
# print(str.title()) #make 1st letter of each word capital
# print(str.count("A")) #counts the number of occurrences of the specified value
# print(str.count("A",0,5)) #counts the number of occurrences of the specified value in the range of index 0 to 5
# print(str.center(22,'-')) #centers the string in a field of 22 characters wide and fills the rest with the specified character
# print(str.rjust(22,'-')) #right justifies the string in a field of 22 characters wide and fills the rest with the specified character
# print(str.ljust(22,'-')) #left justifies the string in a field of 22 characters wide and fills the rest with the specified character

# str = "ASAD ALI"
# str1= "is21"
# str2 = "1234567"
# str3 = "asadali"
# str4 = "    "
# print(str1.isdigit()) #checks if string is digit or not gives false because the string contains letters and numbers
# print(str2.isdigit())
# print(str.isalpha()) #checks if string have just alphabets not numbers or special characters or spaces
# print(str3.isalpha())
# print(str1.isalnum()) #checks if string have just alphabets and numbers not special characters or spaces
# print(str3.isalnum())
# print(str4.isspace()) #checks if string have just spaces not alphabets or numbers or special characters
# print(str.isspace())
# print(str4.join(str)) #joins the string with the specified string
# #A    S    A    D         A    L    I
# print(str.max()) #finds the maximum character in the string(based on ASCII value)
# print(str.min())

# str= "--ASAD ALI--"
# print(str.strip('-'))
# print(str.lstrip('-'))
# print(str.rstrip('-'))

"""ARRAYS ,[]-> is an index operator and index must be integer
collection of homogeneous elements in contiguous memory locations( Contiguous memory means
that a program or process is stored in one continuous block of memory locations.
In simple words, all the required memory locations are placed next to each other without gaps).
A user can treat lists as arrays. However, user cannot constraint the type of elements stored in a list. 
If you create arrays using the array module, all elements of the array must be of the same type"""

import array as arr
# array1 =arr.array('d',[1.2,2.9,3.6,4.5,5.9])
# array2 =arr.array('i',[1,2,3,4,5])
# print(array2)
# for i in array2:
#     print(i) #prints the elements of the array
# print(array2)
# array1.insert(2, 6.7) #inserts the element at the specified index
# print(array1)
# array1.append(8.9) #adds element at the end of the array
# print(array1)

# x=arr.array('i',[])
# print(x)
# for i in range(6):
#     x.append(int(input("Enter the number: "))) #adds the elements to the array
# print(x)

# x =arr.array('i',[])
# z = True
# while (z==True):
#     num = int(input("Enter the number: "))
#     z = input("Do you want to add more numbers? (y/n): ")
#     x.append(num)
#     if (z.lower()=='n'):
#         z=False
#     else:
#         z=True
# print(x)


a =arr.array('i',[1,2,3,4,5,6])
print(a.index(3)) #gives the index of the specified value in its 1st occurrence


