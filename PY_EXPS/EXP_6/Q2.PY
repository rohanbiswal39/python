# 2. WAP to print a matrix along with a sumation of row elements and column elements after entering a 3*3 matrix.

def row_sum(matrix):
    for i in range(3):
        print("Row", i + 1, "sum =", sum(matrix[i]))


def column_sum(matrix):
    for j in range(3):
        total = 0
        for i in range(3):
            total = total + matrix[i][j]
        print("Column", j + 1, "sum =", total)


def display(matrix):
    print("Matrix:")
    for row in matrix:
        print(row)


# Input 3 × 3 matrix
matrix = []

print("Enter 3 × 3 matrix:")

for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

display(matrix)

print("\nSummation of rows:")
row_sum(matrix)

print("\nSummation of columns:")
column_sum(matrix)