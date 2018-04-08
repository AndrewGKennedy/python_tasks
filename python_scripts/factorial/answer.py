##Author: Andrew Kennedy
##Date: 08/04/2018
##Rel: 1.0
##Rev: 1.0
##Prog: factorial with input

##Ref: https://www.programiz.com/python-programming/examples/factorial-recursion
# Python program to find the factorial of a number using recursion

def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)



num = int(input("Enter a number  (5,7,10): "))

# check is the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers positive integers only..")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))