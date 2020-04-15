#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # First arg is recipe
    # Second arg is total ingredients available
    # Return num of batches possible, given the ingredients available.
    batches_possible_arr = []
    # Loop through ingredients to see how many batches can be made, considering that ingredient.
    # Return the lowest batch number.
    for ingredient in recipe.keys():
        if ingredient in ingredients.keys():
            batches_possible_arr.append(
                ingredients[ingredient] // recipe[ingredient])
        else:
            return 0
    return min(batches_possible_arr)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 138, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
