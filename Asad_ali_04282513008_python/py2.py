list = [3,5,88,90,12,45]
for i in range(len(list)):
    list.pop(0)
    print(list)

#array
from array import array
#array_input = [int(x) for x in input("enter array elements:").strip().split(' ')]
#print()
#print("the input list is:" ,array_input)
#print()
#array2 = array('i',array_input)
#print(array2)
#print()
my_array = array ('i',[2,3,5,5,6,77])
print('display the array: ', my_array)
print()
print('elements of array :', end=" ")
print()
for i in my_array:
    print(i, end = " ")
for i in range(0,4):
    print(my_array[i], end = " ")
print()
#insertion 
my_array.insert(3,100)
print("array after insertion :", my_array)

print("accessing elements of array:", my_array[0])
first =my_array.index(5)
print("first occurence :", first)
second = my_array.index(5, first +1)
print("second occurrence:", second) 
my_array[3] = 1000
print("after update array is :", my_array)

my_array.pop(0)
print("array after popping:", my_array)

my_array.remove(77)
print("array after removing is :", my_array)

print("sliced array:", my_array[0:2])


#list
List = []
print("Blank List: ")
print(List)
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

List = [1, 2, 'python', 4, 'for', 6, 'DataScence']
print("\nList with Mixed Values: ")
print(List)

print("the final list:", List)

#accessing 
print(List[2])

#negative idx
print(List[-1],List[-3])

#append
List.append(1000)
print("list after append" , List)

List.append((7,45,66))
print("list after 2nd append" , List)

List.append([2,44,66,77])
print("list after 3rd append" , List)

#insert
List.insert(8,'laraib')

#extend
List.extend([3,'DSA','bioinformatics'])
print("list after extend" , List)
List.extend([3,56,90])
print("list after extend" , List)

List.remove('bioinformatics')
List.remove(1000)
print("\nList after Removal of two elements: ")
print(List)

List.pop()
print("\nList after pop(): ")
print(List)

List.pop(3)
print("\nList after pop(): ")
print(List)

Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)
Sliced_List = List[5:]
print("\nElements sliced from 5th element till the end: ")
print(Sliced_List)

Sliced_List = List[::-1]
print("Reverse List: ")
print(Sliced_List)