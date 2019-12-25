mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(mat1[0][0])
for i in mat1:
    print(i)

for i in range(0,3):
    for j in range(0,3):
        mat1[i][j] = int(input("Enter element"))
for i in mat1:
    for j in i:
        print(j, end=" ")
    print()