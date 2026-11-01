# list comprehension is elegant way to define and create the lists in python. It is a concise way to create lists by applying an expression to each item in an 
# iterable (like a list, tuple, or string) and optionally filtering the items based on a condition. List comprehensions are often more readable and efficient than 
# using traditional loops for creating lists.

# syntax : [expression for item in list if condition]

# create list containing 0 to 100 . 

l = []

for num in range(0,101):
    l.append(num)
print(l)


l = [num for num in range(0,101)] # print numbers from 0 to 100
print (l)


l = [num for num in range(0,101) if num < 50]  # print only those numbers which are less than 50
print (l)

name = "Khushal"

name_list = [ch for ch in name]

print(name_list) # print each character of the string in list