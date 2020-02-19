#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # 9 lines of code?
  # Find the maximum difference between smallest and largest price in list
  # current_min_price_so_far and the max_profit_so_far?
  # min price has to come before --> make a loop
  # assign first value to min price so far...
  # - min price --> [0] in array
  # max price (currently on) - min price
  # max profit 
  # loop: if you find price smaller than current price - set that to be smallest - else continue with that mic price
  # curr profit just calculates  --> currr profit net i in the list minus the min - price
  # if price at index we're at is lower than min price - set it to be the min price
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))