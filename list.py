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

for i in range(length): # range in python is a built-in function that generates a sequence of numbers. It can take one, two, or three arguments: start, stop, and step. The range function returns an iterable object that produces numbers from the start value (inclusive) to the stop value (exclusive), incrementing by the step value. If only one argument is provided, it is treated as the stop value, and the start defaults to 0. If two arguments are provided, they are treated as the start and stop values, respectively. If three arguments are provided, they are treated as the start, stop, and step values.
    print(i)
    
for n in range(length):
    print(l[n])

for n in l:
    print(n)
    
for n in range(length-1, -1, -1): # range(start, stop, step)
    print(l[n])