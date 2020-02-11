import time
from Stack import Stack

# def Hanoi_rec(n, s, a, d):
# Checks to see if the number of disks is 0
# Otherwise it recursively calls itelf until the
# base case is reached printing the results
def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)

  if n == 0:
     d.push(s.pop())
  else:
     Hanoi_rec(n-1, s, d, a)
     d.push(s.pop())
     Hanoi_rec(n-1, a, s, d)
  
  print(n, s, a, d)
  print()

# def Hanoi(n):
# Sets the constructor of Source, destination and auxiliary to stack
# Pushing the disks until the disks are set
# Then initiliazes the recursive function to sort them from one stack
# to the other.
def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == '__main__':
  start = time.clock()
  n = 3
  Hanoi(n)
  end = time.clock()
  print('computed Hanoi(' + str(n) + ') in ' + str(end - start) + ' seconds.')