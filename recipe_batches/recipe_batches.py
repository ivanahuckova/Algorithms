#!/usr/bin/python

import math
recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
ingredients = {'milk': 1288, 'flour': 9, 'sugar': 95}


def recipe_batches(recipe, ingredients):
    min_amount = float('inf')
    recipe_items = list(recipe.keys())

    for i in range(0, len(recipe_items)):
        try:
            val = str(ingredients[recipe_items[i]])
        except KeyError:
            min_amount = 0
            return min_amount

        if ingredients[recipe_items[i]]/recipe[recipe_items[i]] < min_amount:
            min_amount = int(
                ingredients[recipe_items[i]]/recipe[recipe_items[i]])

    return min_amount


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
