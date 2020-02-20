#!/usr/bin/python
"""
I need a helper function that will take care of the for loop

function that is a recursvie function

a list of the resutlts

n is the rounds of the game 

if n = 1 --> im playing 1 round and all the possible outcomes is: rock_paper_scissors(1), [['rock'], ['paper'], ['scissors']]

I'll be doing a for loop inside of a for loop becasue I want to create ALL of the possible moves in sequential order based on the number of roiunds being played (or passed in to the function)
"""

import sys

def rock_paper_scissors(n):
  # set the different moves to be a list off all different moves
  
  # set the list to be an empty list 

  # if n is equal to 0 
    # return empty list
  # otherwise if n is 1 
    # return list.append['rock'], ['paper'], ['scissors']
  # 
  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')