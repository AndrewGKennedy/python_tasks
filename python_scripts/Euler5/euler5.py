
##Author: Andrew Kennedy, with significant help from web, see Ref's below
##Date: 07/04/2018
##Ver: 1.0
#Rel: 1
##Python for Project Euler #5: http://projecteuler.net/index.php?section=problems&id=5
##Find the smallest number that is divisible with all integers from 1 to 20"""
##Ref: 1.0 #https://gist.github.com/PEZ/47534
##Ref: 2.0 http://www.math.com/school/subject1/lessons/S1U3L3GL.html
##Ref 3.0 https://stackoverflow.com/questions/12605320/project-euler-3-why-does-this-method-work

#It's the Least Common Multiple; lcm(1,2, ..., 20) 
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)

llcm = lcm(11, 12)
for n in range(12, 20):
  llcm = lcm(n, llcm)


#Reused from Eueler problem 3, see forum, ref 3.0

i = 1
for k in (range(1, 21)): 
  if i % k > 0: 
    for j in range(1, 21): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print(i)