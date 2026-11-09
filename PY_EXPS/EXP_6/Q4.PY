# 4. WAP to check if a value is present in the list or not, using lambda function.

lst = list(map(int, input("Enter list elements: ").split()))

value = int(input("Enter value to search: "))

check = lambda x: x in lst

if check(value):
    print("Value is present in the list")
else:
    print("Value is not present in the list")