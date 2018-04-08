
##Author: Andrew Kennedy 
##Date: 08/04/2018
#Exercise: Factorial input/out
##Version 1.0
##Release 1.0

##Changes list:
##None

##Ref: https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

##------------------------------- Function Main ------------------------------------------------------


import mat


print("Please enter a number (positive  Integer):")
try:

    ##cast to do int do type cast checking. alwawys a good idea. need to research debug options
    number = (int(input()))
except ValueError:
          print("Error Not a a positive Integer. Please enter a valid Integer 5, 7 10.")
try:
    ##pass the input to the func that proceses the number to calculate factorial
    answer = factorial(number)
    print(answer)
except ValueError:
    print("Error: Calling factorial(n)",answer)
##---------------------------  End Function Main --------------------------------------------------------

##--------------------------------- Start Function Factorial ----------------------------------------------------
def factorial(x):
    result = 1
    for i in xrange(2, x + 1):
        result *= i
    return result

##----------------------------    End  Function Factorial --------------------------------------------------