def fac(n1):
    #n1 = float(n1)
    if (n1 > 1):
       return n1 * fac(n1-1)
    else:
        return n1
def power(a, b):
    ans = 1
    for x in range(int(b)):      #range takes integer value     also range(1,(int(b)+1))
        ans = ans*a
    return ans
a = float(input("Enter the number: "))
print(fac(a))
print(power(float(input("Enter the base number: ")),float(input("Enter the power"))))
