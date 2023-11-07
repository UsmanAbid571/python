


print("What do you want?")
first = input("Enter 'A' for arithmetic operations or 'B' for comparison of two numbers:  ").lower()
if first == "a":

    def add(n1, n2):
            return n1 + n2
    def sub(n1, n2):
            return n1 - n2
    def mul(n1, n2):
            return n1 * n2
    def div(n1, n2):
            return n1 / n2

    op = input("Enter the operation you want (+, -, *, /): ")
    n1 = float(input("Enter a number: "))
    n2 = float(input("Enter another number: "))

    if op == "+":
        print(add(n1, n2))
    elif op == "-":
        print(sub(n1, n2))
    elif op == "*":
        print(mul(n1, n2))
    elif op == "/":
        print(div(n1, n2))
    else:
        print("You entered the wrong operator")


elif first == "b":
     num1 = float(input("Enter a number: "))
     num2 = float(input("Enter another number: "))
     num3 = float(input("Enter another number: "))
     if num1 > num2 and num1 > num3:
         print("Number 1: " + str(num1) + " that you entered is greater ")
     elif num2 > num1 and num2 > num3:
         print("Number 2: " + str(num2) + " that you entered is greater ")
     elif num3 > num1 and num3 > num2:
         print("Number 3: " + str(num3) + " that you entered is greater ")
     else:
         print("The numbers that you entered are all equal ")
else:
    print("Your input is incorrect")
