print("""This is your calculator.
      It supports -
      + Addition,
      - Subtraction,
      * Multiplication,
      / Division """)


input1=float(input("Enter first number :- "))
input2=float(input("Enter second number :- "))
operator=str(input("Enter the operator, supported operators are +,-,*,/ :- "))


if operator == "+":
    print("Doing Addition ...")
    print(input1+input2)
elif operator == "-":
    print("Doing Subtraction ...")
    print(input1-input2)
elif operator == "*":
    print("Doing Multiplication ...")
    print(input1*input2)
elif operator == "/":
    print("Doing Division ...")
    print(input1/input2)
else:
    print("unknown operation.....")