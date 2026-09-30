def recursion_factorial(n):
    if  n==1: 
         return 1
    else:
         return n*recursion_factorial(n-1)

num=int(input("enter a number:"))

# Cheack if the number is negative

if num <0:
     print("Sorry, factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of", num, "is", recursion_factorial(num))

    #recursive is when the fuction re calls it self.         # four function in a claculator