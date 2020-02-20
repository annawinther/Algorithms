#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # if the n is less than zero
    # return zero
  # otherwise if n is equal to zero
    # return one
  # otherwise 
    # return a recursive call to the function for n - 1 + n - 2 + n - 3
    pass


print(eating_cookies(3))
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


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')