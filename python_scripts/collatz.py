# Andrew Kennedy goo
# 18/02/2018
# Revision 1.0
# Origin https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff  
# I like code reuse! 

print("Please enter a number (positive  Integer):")
try:
    number = (int(input()))
except ValueError:
          print("Error Not a a positive Integer. Please enter a valid Integer.")
      

def collatz(number):
    print("Your valid start integer is",number)
    while number != 1:
        print("Your number is now: ",int(number))
    # Modula % 2 to determine if an even integer

        if number % 2==0:
            number = (number//2)
            print("This value is an even number", int(number))
            ## else if modula 2 != 0
        elif number % 2==1:
            number = (3*number+1) 
            print("This value is an Odd number output is modula * 3 + 1 = ", int(number))
            print(number)

            return (print("Even Number: ",int(number)))
            ## continue loop until statement 1 is true while not 1
        continue

    #Print number
collatz(number)

# Output
#C:\Users\user\Desktop\Course\python_scripts>python collatz.py
#Please enter a number (positive  Integer):
#53
#Your valid start integer is 53
#Your number is now:  53
#This value is an Odd number output is modula * 3 + 1 =  160
#160
#Even Number:  160
#
#C:\Users\user\Desktop\Course\python_scripts>

