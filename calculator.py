print("What do you want?")
first = input("Enter 'A' for arithmetic operations or 'B' for comparison of two numbers:  ")
if first == "A" or "a":
    n1 = float(input("Enter a number: "))
    n2 = float(input("Enter another number: "))
    op = input("Enter the operator(+, -, *, /): ")
    if op == "+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*":
        print(n1 * n2)
    elif op == "/":
        print(n1 / n2)
    else:
        print("You entered the wrong operator")


elif first == "b" or "B":
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
