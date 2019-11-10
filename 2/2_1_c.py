R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix_1 = []
print("Enter the entries row wise For Matrix 1:")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix_1.append(a)

matrix_2 = []
print("Enter the entries row wise For Matrix 2:")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix_2.append(a)

print("First Matrix :")
for i in range(R):
    for j in range(C):
        print(matrix_1[i][j], end=" ")
    print()

print("Second Matrix :")
for i in range(R):
    for j in range(C):
        print(matrix_2[i][j], end=" ")
    print()

res = [[0 for x in range(R)] for y in range(C)]

# explicit for loops
for i in range(len(matrix_1)):
    for j in range(len(matrix_2[0])):
        for k in range(len(matrix_2)):
            # resulted matrix
            res[i][j] += matrix_1[i][k] * matrix_2[k][j]

print("Result :")
for i in range(R):
    for j in range(C):
        print(res[i][j], end=" ")
    print()



