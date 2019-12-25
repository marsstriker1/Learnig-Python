def basic_if():
    condition1 = True
    c1 = True
    c2 = False
    if condition1:
        print("The condition is true.")
    else:
        print("The condition is not true. ")
    condition1 = False
    print("Condition Changed.")
    if condition1:
        print("The condition is true.")
    else:
        print("The condition is not true. ")
    if c1 or c2:
        print("Either c1 or c2 is True.")
    if c1 and c2:
        print("Both c1 and c2 are True.")
    else:
        print("Any one of c1 and c2 is not true.")
    if c1 and not(c2):
        print("Both c1 and c2 are True.")
    else:
        print("Any one of c1 and c2 is not true.")
basic_if()
a = input("Enter a number: ")
b = input("Enter another number: ")
if (a>b):
    diff = float(a)-float(b)
else:
    diff = float(b) - float(a)
print("The difference is", diff)
if int(a) != (int(b)+1):
    print(a, " != ", b)
elif int(a) == int(b):
    print(a, " = ", b)



