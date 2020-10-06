
# import time
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
    op = input("Continue?(Y/N)")
# start_time=time.time()
# num=0
# i = 0
# while(num<10000000000000000 or i==4):
#     a = num
#     print(num,end="\n")
#     i=0
#     while(int(a) % 10 !=int(a)):
#         ans = 1
#         for x in str(a):
#             ans = ans * int(x)
#         a = ans
#         i=i+1
#         # print(ans, end="\n")
#     num = num+1
#
#     print("Multiplicative Persistence = ",i, end='\n')
#     if(i==9):
#         break
# print(time.time()-start_time)