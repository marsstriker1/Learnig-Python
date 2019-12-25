def adds():
    a = input("N1=? ")
    b = input("N2=? ")
    sum = float(a) + float(b)
    print(sum)
def subtractsAfterAsking(n1, n2):
    sum = float(n1) - float(n2)
    return sum
    print("This line will not be printed as return breaks control flow")
print("Process Start.")
adds()
a = input("N1=? ")
b = input("N2=? ")
print(subtractsAfterAsking(a, b))   #returned value is printed.
ans = subtractsAfterAsking(a, b)
print(ans)
print("Process End.")