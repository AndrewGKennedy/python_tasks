import logging
print = __builtins__.print if debug else logging.debug


## global variables

a = [1,2,3,4,5]
num = 0
answer = False


def checknum(n):
  for i in range(len(a)):
    print("Debug Func: checknum. Range is: ", i, " Value: ", a[i])
    print("Debug Func: checknum. Value of input n is: ", n)
    while  n % 2 == 0 and i != len(a):
       n + 1 
      continue
    elif n % 2 != 0:
      n + 1
     ## break
    else:
      return True



## if n % 2 != 0:   
 ##     break
 ##   elif n % 2 == 0: 
 ##     print("Debug Func: checknum. Here line 15")
 ##     continue
 ##   else:
 ##     return True
##''''

 #      if n == len(a) and n % 2 == 0:
 #        return True
 #   else:
 #       n = n+1
 

## main loop
while answer <= len(a):
  answer = checknum(num)
  if answer == True:
    print("Success, num is :", num)
  else:
    print("Fail, num is :", num)
    num + 1




