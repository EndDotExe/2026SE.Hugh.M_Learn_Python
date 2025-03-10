num1 = int(input("Number 1? "))
num2 = int(input("Number 2? "))
op = input("Operator? ")

if op == "*":
    print(num1 * num2)
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Not a Known Operator")