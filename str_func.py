string = 'This tutorial is about Python string functions.'


# .lower() method converts all characters in a string to lowercase.
# .upper() method converts all characters in a string to uppercase.
# .title() method converts the first character of each word to uppercase and the rest to lowercase.
# .capitalize() method converts the first character of a string to uppercase and the rest to lowercase.

l=string.lower()
print("Lowercase:", l)

u=string.upper()
print("Uppercase:", u)

t=string.title()
print("Titlecase:", t)

c=string.capitalize()
print("Capitalized:", c)



# .find() method returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
# .index() method returns the index of the first occurrence of a substring in a string. If the substring is not found, it raises a ValueError.
# .isalpha() method returns True if all characters in a string are alphabetic, and False otherwise.
# .isdigit() method returns True if all characters in a string are digits, and False otherwise.
# .isalnum() method returns True if all characters in a string are alphanumeric (letters and numbers), and False otherwise.


f=string.find('o', 9) # (substring, start_index, end_index)
print("Index of 'o':", f)

missing=string.find('o', 23, 24) # if the substring is not found, it returns -1.
print("Index of 'missing':", missing)

t=string.find('tutorial')
print("Index of 'tutorial':", t)


f=string.index('o', 9) # (substring, start_index, end_index)
print("Index of 'o':", f)

# missing=string.index('o', 23, 24) # if the substring is not found, it raises a ValueError.
# print("Index of 'missing':", missing)

t=string.index('tutorial')
print("Index of 'tutorial':", t)


# the difference between .find() and .index() is that .find() returns -1 if substring is not found while .index() raises a value error if substring is not found.


alpha=string.isalpha()
print("Is the string alphabetic?:", alpha)  # this will return false, because string contains spaces and punctuation, which are not alphabetic characters.


alpha=string.replace(" ","").replace(".","").isalpha()
print("Is the string alphabetic?:", alpha)  # true, because we removed spaces and punctuation, leaving only alphabetic characters.

digitstr="1234567890"

numeric=digitstr.isdigit()
print("Is the string numeric?:", numeric)

alpha_numeric="Python3"

alphanumeric=alpha_numeric.isalnum()
print("Is the string alphanumeric?:", alphanumeric)


alphanumeric=alpha_numeric.replace("y", " ").replace("h", "@").isalnum()
print("Is the string alphanumeric with speacial character and space?:", alphanumeric)



#------------------------------------------------------------------------------------------------------------#



# chr() method returns the string representing a character whose Unicode code point is the integer passed as an argument. This takes ASCII value and return the corresponding character.
# ord() method takes a string representing a character and returns the ASCII value of that character.


int = 65
print("Character for ASCII value", int, "is:", type(chr(int)), chr(int))


str = "A"
print("ASCII value for character", str, "is:", type(ord(str)), ord(str))



# .format() method formats the specified value(s) and inserts them inside the string's placeholder. The placeholder is defined using curly brackets {}.


example1="I love {} and {} programming languages." # empty placeholders
print(example1.format("Python", "Java")) # positional arguments
example2="I love {first:>20} and {second:^20} programming languages." # named placeholders
print(example2.format(first="Python", second="Java"))
example3="I love {1} and {0} programming languages." # indexed placeholders
print(example3.format("Java", "Python"))
