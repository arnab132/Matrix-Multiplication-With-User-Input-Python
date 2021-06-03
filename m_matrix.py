 
print("Enter order of 1st matrix:")
 
# take integer inputs in one line
m,n = list(map(int,input().split()))
 
print("Enter Row wise values")
 
# empty list for 1st matrix
mat1 = []
 
# row wise insertion in the matrix
for i in range(m) :
    print("Enter row",i,"value:")
 
    # take 1d- integer array input in one line
    row = list(map(int,input().split()))
    mat1.append(row)
 
print("Enter order of 2nd matrix:")
 
# take integer inputs in one line
p,q = list(map(int,input().split()))
 
print("Enter Row wise values")
 
# empty list for 2nd matrix
mat2 = []
 
# row wise insertion in the matrix
for j in range(p) :
    print("Enter row",j,"value:")
 
    # take 1d- integer array input in one line
    row = list(map(int,input().split()))
    mat2.append(row)
 
# showing 1st and 2nd matrix
print("Matrix 1:",mat1)
print("Matrix 2:",mat2)
 
# empty list for resulatant matrix
resultant = []
 
# create a 0-matrix of order m x q
for i in range(m):
    row = []
    for j in range(q):
        row.append(0)
 
    resultant.append(row)
 
print("Matrix Multiplication: ")
 
# perform matrix multiplication
# using nested for loops
for i in range(m):
    for j in range(q):
        for k in range(n) :
            resultant[i][j] += mat1[i][k] * mat2[k][j]
 
# matrix printing row wise            
for row in resultant:
    print(row)
