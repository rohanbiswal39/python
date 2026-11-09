# 1. WAP to print a matrix containing group of similar elements by giving the input randomly in another matrix. 

def group_elements(matrix):
    elements = []

    for row in matrix:
        for x in row:
            elements.append(x)

    elements.sort()

    return elements


def display(elements, rows, cols):
    k = 0
    for i in range(rows):
        for j in range(cols):
            print(elements[k], end=" ")
            k += 1
        print()


# Input
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

matrix = []

print("Enter matrix:")
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

# Function call
elements = group_elements(matrix)

print("Matrix with similar elements grouped:")
display(elements, r, c)