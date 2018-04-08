"""Python for Project Euler #5: http://projecteuler.net/index.php?section=problems&id=5
Find the smallest number that is divisible with all integers from 1 to 20"""


""""https://gist.github.com/PEZ/47534

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

print llcm

#Found the following on the Euler Problem 3 forum, by signature lassevk
#It's quite neat!
i = 1
for k in (range(1, 21)): 
  if i % k > 0: 
    for j in range(1, 21): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print i