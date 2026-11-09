# 3. WAP to print the transpose of a matrix of n*n order

def transpose(matrix, n):
    print("Transpose of matrix:")

    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=" ")
        print()


n = int(input("Enter the order of matrix: "))

matrix = []

print("Enter the matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Original Matrix:")

for row in matrix:
    print(row)

transpose(matrix, n)