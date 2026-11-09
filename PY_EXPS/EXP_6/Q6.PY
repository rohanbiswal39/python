# 6. WAP to print the intersection of 2 arrays using lambda function

a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

intersection = lambda x: x in b

result = []

for x in a:
    if intersection(x):
        result.append(x)

print("Intersection =", result)