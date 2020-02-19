#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # less or equal to 1 return 1 --> base case
  if n <= 1:
    return 1
  # if we give 5:
    # 1 1 1 1 1
    # 1 1 1 2
    # 1 1 2 1
    # 1 1 3
    # 1 2 1 1
    # 1 2 2
    # 2 1 1 1
    # 2 1 2
    # 2 2 1
    # 2 3
    # 3 1 1
    # 3 2


  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')