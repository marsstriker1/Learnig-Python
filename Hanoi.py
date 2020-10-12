def move(a, b):
    print("Move Disc from "+ a +" to " + b +"!")
def hanoi(n,f,h,t):
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)
n=int(input("Number of discs?:"))
hanoi(n,"a","b","C")