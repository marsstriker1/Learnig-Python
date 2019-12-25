def calc(a, op, b):
    if op == "+":
        res = a + b
    elif op == "-":
        if a > b:
            res = a - b
        else:
            res = b - a

    elif op == "*":
        res = a * b
    elif op == "/":
        res = a / b
    else:
        print("Invalid operator")
        return
    print(res)
  #print(type(res))
print("Press Enter after each entry!!!")
a = input("")
a = float(a)
op = input("")
b = float(input())
calc(a, op, b)

