# 6. WAP to enter two different sets with string elements combine both the sets remove any duplicates are present, print the new set. 

s1=set(eval(input('Enter the 1ST set:'))) 
s2=set(eval(input('Enter the 2nd set:'))) 
s3=set()

s1.update(s2) 
s3=s1

print("After updation the new set is:",s3)