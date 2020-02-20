#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies_without_cache(n, cache=None):
  # if the n is less than zero
  if n < 0:
    # return zero
    return 0
  # otherwise if n is equal to zero
  elif n == 0:
    # return one
    return 1
  # otherwise 
  else:
    # return a recursive call to the function for n - 1 + n - 2 + n - 3
    return eating_cookies_without_cache(n - 1) + eating_cookies_without_cache(n - 2) + eating_cookies_without_cache(n - 3)

def eating_cookies(n, cache=None):
  # if the n is less than zero
  if n < 0:
    # return zero
    return 0
  # otherwise if n is equal to zero
  elif n == 0: 
    # return one
    return 1
  # otherwise if the case of the cache at index of n contains the answer
  elif cache and cache[n] > 0:
    # return the cache at index of n
    return cache[n] 
  # otherwise
  else:
    # test if there is a cache at all (if not)
    if not cache:
      # create a cache using a range based loop
      cache = {i: 0 for i in range(n + 1)}
    
    # set the cache at index n to the recursive call passing th ecache as we go
    cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    # return the cache at index n
    return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')