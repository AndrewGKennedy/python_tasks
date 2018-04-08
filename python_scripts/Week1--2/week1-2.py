-# Andrew Kennedy/ Ian McLoughlin
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 30
ans = fib(x)
print("Fibonacci number", x, "is", ans)
import sys
import string

## fib2.py - 2nd exercise
## using command line arguments and string functions
## Andrew Kennedy
## Student ID: G00364899

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i


""""------------ Start Function position -------------------------"""

""""function pos, args letter a char"""
"""" Get the position in the alphabet, assuming all uppercase"""
"""" Input: Letter, the letter to find index 1-26 (uppercase)"""
"""" Output: the index 1-26"""
"""" Globls: String Aplhabet"""


def position(Aletter):

    print("debug --lastletter is incoming ", Aletter)

    """ define the alphabet, only in uppercase for now.."""
    "An array n chars"

    Alphabet = "abcdefghijklmnopqrstuvwxyz" 

    """"Find position in variable Alphabet    
    a =  string.lowercase(Aletter)


    """"add one on as string arrays start at 0"""
    """" use the string.index function to find position and add 1 on.."""
    
    Aletter = Aletter.lower()
    a = Alphabet.index(Aletter)
    
    a = a+1
    print("debug - position(string) position is: ",a)
    return a

""""----------------- End Function position ---------------------"""

""""------------------------Start Main ----------------------"""
print ("The main(argv[0]):is is the name of the script: ", sys.argv[0])
print ("Second argument: ", sys.argv[1])

Name = sys.argv[1]
print("name:", Name)

FirstLetter = Name[0]
print("FirstLetter:", FirstLetter)

print("NameLength", len(Name))


""""Get the last letter in the name"""
LastLetter = Name[len(Name) -1]
print("LastLetter:", LastLetter)

Let_a = position(FirstLetter)
Let_b = position(LastLetter)


Fib1 = fib(Let_a)
print("Fibonacci for first letter is:", Fib1)
Fib2 = fib(Let_b)
print("Fibonacci for last letter is:", Fib2)

Answer = Fib1+Fib2
print ("Total fibonacci is:", Answer)
"""" -------------- End Main Function --------------------------"""
# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Kennedy"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


## Output
## Exercise 1
#Fibonacci number 30 is 832040

## Exercise 1 with my name, command line args

##The main(argv[0]):is is the name of the script:  answer_tsks_1_2.py
##Second argument:  Andrew
##name: Andrew
##FirstLetter: A
##NameLength 6
##LastLetter: w
##debug --lastletter is incoming  A
##debug - position(string) position is:  1
##debug --lastletter is incoming  w
##debug - position(string) position is:  23
##Fibonacci for first letter is: 1
##Fibonacci for last letter is: 28657
##Total fibonacci is: 28658

## Exercise 2 Ord function
##My surname is Kennedy
##The first letter K is number 75
##The last letter y is number 121
##Fibonacci number 196 is 40934782466626840596168752972961528246147

## Exercise 2 comment on Ord function

##Ord (n) returns the the unicode value of a unicode char or byte, if the language is using unicode.
##
##Some languages do not, for example Microsoft programmes used to use their own values to indicate

##the value of a char, and you had to bitshift them one by one to get them into unicode...
 