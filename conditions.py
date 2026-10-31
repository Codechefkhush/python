# if condition
# if else condition
# if elif else condition


a=float(input("Enter first input..."))
b=float(input("Enter second input..."))
c=input("Enter something...")
d=float(input("Enter percentage of a student :- "))


# if condition

if a == 2:
    print("condtion is passed")
    
# String checking
if isinstance(c, str):
    print("this is string")
    
if type(c) == str:
    print("this is string")
    
    

# if else condition

# Even checking
if a%2 == 0:
    print("This is even number.")
else:
    print("This is odd number.")


# Odd checking
if b%2 != 0:
    print("This is odd number.")
else:
    print("This is even number.")
    
    
# if elif else condition
if d >= 75:
    print("first division.")
elif d >=60 and d<75:
    print("second division.")
elif d >= 35:
    print("third division.")
else:
    print("failed....")

    
    
    