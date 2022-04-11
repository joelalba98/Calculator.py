a = input('first number?')
op = input("enter operator: ")
b = input('second number?')

if op == "+" :
    print(int(a) + int(b))
elif op == "-":
    print(int(a) - int(b))
elif op == "*":
    print(int(a) * int(b))
elif op == "/":
    print(int(a) / int(b))
else:
    print("invalid operator")

