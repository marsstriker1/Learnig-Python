'''coordinates = (1,7)         #tupples are defined by using ( ).They are static throughout the program
coordinates2 =(4,5)
#coordinates[0] = 3     this shows error as tuples' values can't be re-assigned or changed.
print(coordinates)
print(coordinates2)
print(coordinates[0])
print(coordinates[1])
print(coordinates2[0], coordinates2[1])
coll_coor= [(1, 3),(4, 5)]
print(coll_coor)
print(coll_coor[0])
coll_coor[1] = 5
print(coll_coor[1])     #this happens because the entire tupple is replaced by another data item
coll_coor[1] = "Possible."
print(coll_coor[1])
'''
ans ='y'
while(ans=='y'):
    a = int(input())
    b = input()
    c = int(input())
    if(b=='+'):
        print(str(a) +"+"+ str(c)+" = "+str(a+c))
    elif (b=='-'):
        print(str(a) +"-"+ str(c)+" = "+str(a-c))
    elif (b=='*'):
        print(str(a) +"*"+ str(c)+" = "+str(a*c))
    elif (b=='/'):
        print(str(a) +"/"+ str(c)+" = "+str(a/c))
    ans=input("Continue?[Y]")

