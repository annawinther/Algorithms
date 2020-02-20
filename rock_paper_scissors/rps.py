#!/usr/bin/python
"""
I need a helper function that will take care of the for loop

function that is a recursvie function

a list of the resutlts

n is the rounds of the game 

if n = 1 --> im playing 1 round and all the possible outcomes is: rock_paper_scissors(1), [['rock'], ['paper'], ['scissors']]

I'll be doing a for loop inside of a for loop becasue I want to create ALL of the possible moves in sequential order based on the number of rounds being played (or passed in to the function)
"""

import sys

def rock_paper_scissors(n):
  # set the different moves to be a list off all different moves

  # set the outcomes to be an empty list 

  # define a helperfuncition that takes in the rounds remaining and the result (initialize as an empty list)
    # have a base case is there are no more rounds left 
      # return the outcomes and append the result from the function
    # do a for in loop in the moves lists
      # this is a recursive call
      # using the helperfunction decrementing the remaining rounds for each itteration and adding the resutl together with reach move 
      
  # then invoking the helperfunction

  # and return the outcomes form that

  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')