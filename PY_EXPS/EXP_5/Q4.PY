# 4. WAP to enter a set and copy the content of the set into a new set one element at a time. 

s=set(eval(input("Enter a set element:"))) 
s1=set()

for i in range(1,len(s)+1): 
    s1.update(s)

print("Updated set is :",s1);