import re
from lxml.cssselect import CSSSelector

# Plugin name as a string
name = "allrecipes"

# Plugin website URL as string
regex = re.compile('\S*allrecipes\.com')

def parse(tree):
    """
    Parse lxml tree and return recipe dict

    Args:
        tree: lxml tree

    Returns:
        recipe: dictionary of recipe

    """
    recipe = {
        'name': '',
        'cook_time': '',
        'prep_time': '',
        'ingredients': [],
        'method': [],
    }

    # name
    name_css_selector = CSSSelector('.recipe-summary__h1')
    name = name_css_selector(tree)

    recipe['name'] = name[0].text

    # ingredients
    ingredient_css_selector = CSSSelector('.recipe-ingred_txt')
    ingredients = ingredient_css_selector(tree)

    for ingredient in ingredients:
        ingredient = ingredient.text_content()
        if not ingredient == "Add all ingredients to list" or ingredient == False:
            recipe['ingredients'].append(ingredient)
    recipe['ingredients'].pop()

    # method
    method_css_selector = CSSSelector('.recipe-directions__list--item')
    method = method_css_selector(tree)

    for step in method:
        recipe['method'].append(step.text_content().strip())
    recipe['method'].pop()



    return recipe
