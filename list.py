# list is built-in data structure in python which is used to store multiple items in a single variable. It is one of the most commonly used data structures in python. Lists are mutable, meaning that their elements can be changed after they are created. They can contain elements of different data types, including other lists.

list = [1, 2, 3, 4, 5]  # Creating a list with integer elements

# print(type(list))  # Output: <class 'list'>

# print("List:", list)  # Output: List: [1, 2, 3, 4, 5]

# print("Length of the list:", len(list))  # Output: Length of the list: 5


# print("First element of the list:", list[0])  # Output: First element of the list: 1

# print("Last element of the list:", list[-1])  # Output: Last element of the list: 5


# print("Slicing the list from index 1 to 3:", list[1:4])  # Output: Slicing the list from index 1 to 3: [2, 3, 4] #[start_index:end_index]


# print("Slicing the list from index 0 to 4 with step 2:", list[0::2])  # Output: Slicing the list from index 0 to 4 with step 2: [1, 3, 5]  # [start_index:end_index:step]

# print("Reverse the list:", list[-1::-1])  # Output: Reverse the list: [5, 4, 3, 2, 1]  # [start_index:end_index:step]



# list iteration

l = [10, 20, 30, 40, 50]

length = len(l)

# for i in range(length): # range in python is a built-in function that generates a sequence of numbers. It can take one, two, or three arguments: start, stop, and step. The range function returns an iterable object that produces numbers from the start value (inclusive) to the stop value (exclusive), incrementing by the step value. If only one argument is provided, it is treated as the stop value, and the start defaults to 0. If two arguments are provided, they are treated as the start and stop values, respectively. If three arguments are provided, they are treated as the start, stop, and step values.
#     print(i)
    
# for n in range(length):
#     print(l[n])

# for n in l:
#     print(n)
    
# for n in range(length-1, -1, -1): # range(start, stop, step)
#     print(l[n])



l = [10, 20, 30, 40, 50]

# If you want to delete something from list, there are multiple ways to do it. You can use the del statement, the remove() method, or the pop() method and clear() method.

del l[2]  # deletes the element at index 2

print("List after deleting element at index 2:", l)  # Output: List after deleting element at index 2: [10, 20, 40, 50]


# remove () method removes the first occurrence of a specified value from the list. If the value is not found, it raises a ValueError.
l = [10, 20, 30, 40, 50]

l.remove(20)

print("List after removing 20:", l)  # Output: List after removing 20: [10, 30, 40, 50]


# pop() method removes and returns the element at the specified index. If no index is specified, it removes and returns the last item in the list. If the index is out of range, it raises an IndexError.

l = [10, 20, 30, 40, 50]

removed_number=l.pop(0)

# print("List after popping element at index 0:", l)  # Output: List after popping element at index 0: [20, 30, 40, 50]
# print("Removed number:", removed_number)  # Output: Removed number: 10

# l.pop()
# print("List after popping last element:", l)  # Output: List after popping last element: [20, 30, 40]

# l.clear()  # This will remove all elements from the list, making it an empty list.
# print("List after clearing all elements:", l)  # Output: List after clearing all elements

# l.pop(5)  # This will raise an IndexError because index 101 is out of range for the list.


# As lists are mutable, you can change the value of an element in a list by accessing it via its index and assigning a new value to it.

# list_abc = [10, 20, 30, 40, 50]

# list_abc[1] = 25  # Changing the value at index 1 from 20 to 25
# print("List after changing value at index 1:", list_abc)  # Output: List after changing value at index 1: [10, 25, 30, 40, 50]

# list_abc[5] = 60  # This will raise an IndexError because index 5 is out of range for the list.



# for adding the data into existing list we have different methods like insert(), append(), extend() and concatenation.


l = [10, 20, 30, 40, 50]

# insert() method inserts an element at a specified index in the list. If the index is greater than the length of the list, the element will be added to the end of the list. If the index is negative, it counts from the end of the list.
l.insert(1, 15)  # inserts 15 at index 1
print("List after inserting 15 at index 1:", l)  # Output: List

l.insert(9, 90)  # inserts 90 at index 9
print("List after inserting 90 at index 9:", l)  # Output: List

l.insert(-1, 100)  # inserts 100 at the last index
print("List after inserting 100 at the last index:", l)  # Output: List


# append() method adds an element to the end of the list. It does not take any index as an argument, and it always adds the new element at the end of the list.

l.append(60)  # adds 60 at the end of the list
print("List after appending 60:", l)  

l2 = [70, 80, 90]
l.append(l2)  # adds the entire list l2 as a single element at the end of the list l
print("List after appending l2:", l)  # Output: List after appending


# extend() method adds all elements of an iterable (like a list, tuple, or string) to the end of the list. It takes an iterable as an argument and adds each element of that iterable to the list.

l3 = [101, 102, 103]
string = "Khushal"
l.extend(l3)  # adds all elements of list l3 to the end of the list l
print("List after extending with l3:", l)  # Output: List after extending with l3:

l.extend(string)  # adds each character of the string to the end of the list l
print("List after extending with string:", l)  # Output: List after extending with string



# concatenation of lists can be done using the + operator. It creates a new list that contains all the elements of the original lists.

la = [1, 2, 3]
lb = [4, 5, 6]

concatenated_list = la + lb  # concatenates lists la and lb
print("Concatenated list:", concatenated_list)  # Output: Concatenated list: [1, 2, 3, 4, 5, 6]