#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  print('test', recipe.items())
  # 1st is recipe 2 is ingredients I have
  # how many times 
  # lowest item in list --> hold you back can only make up to that point

  # cereal for br3akfast = 2 milk & 2 cereal
  # 4 milk & 3 milk 
  # max batch = 1
  # max batch is based on the lowest ingreditent

  # I need to check if the recipie and ingredient has the same keys
    # then I need to set an initial min_ratio/batch and initial number of batches 
    # then loop over the recipe dictionary 
      # set the bacthes variable (which essentially is the ratio between the recipe and the ingredients I have available)
      # and if the max_batches is greater then the batches we calculated 
        # then set the the max_batches to be equal to the batches
        # oterwise return the max_batches as is
  # if there are ingredients missing, 
    # return 0
 
  if set(recipe.keys()).issubset(set(ingredients.keys())): # coverting data structure to a set adn checking if recipe are present in subset of ingredient
      min_ratio = math.inf
      for ingredient in recipe:
        # print('i', ingredient, 'a', amount)
        ratio = ingredients[ingredient] // recipe[ingredient]
        if ratio < min_ratio:
          min_ratio = ratio
          print(min_ratio)
      return min_ratio
  else: 
    return 0 

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 1080, 'butter': 500, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))