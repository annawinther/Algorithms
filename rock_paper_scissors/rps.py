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
  # base cases: 
  # if n is equal to 0 
    # return empty list
  # if n = 1 
    # return the list of moves

  # # set the outcomes to be an empty list 

  # use recursvie function and loop over each sub array of the array
    # inside of this loop also loop over the moves

      # for each sub array inside of the main array set the play to be the sub array plus the move 

      # append the resutl of play to the outcome

  # return the outcome
  pass
print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')