# 5. WAP to print Fibonacci series up to n terms using lambda function.

n = int(input("Enter number of terms: "))

a = 0
b = 1

fibonacci = lambda a, b: (b, a + b)

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = fibonacci(a, b)