op = 'y'
while(op.upper()=='Y'):
    a = input("\nNum:")
    i = 0
    while(int(a) % 10 !=int(a)):
        ans = 1
        i=i+1
        for x in str(a):
            ans = ans * int(x)
        a = ans
        print(ans, end="\n")
    print("Multiplicative Persistence = ",i, end='\n')
    op=input("Continue?(Y/N)")