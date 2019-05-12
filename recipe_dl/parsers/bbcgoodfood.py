import re
from lxml.cssselect import CSSSelector

# Plugin name as a string
name = "BBC Good Food"

# Plugin website URL as string
regex = re.compile('\S*bbcgoodfood\.com')

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
    name_css_selector = CSSSelector('.recipe-header__title')
    name = name_css_selector(tree)

    recipe['name'] = name[0].text


    # cook time
    cook_time_selector = CSSSelector('.recipe-details__cooking-time-cook')
    cook_time = cook_time_selector(tree)

    recipe['cook_time'] = cook_time[0].text_content().split(':')[1].strip()


    # prep time
    prep_time_selector = CSSSelector('.recipe-details__cooking-time-prep')
    prep_time = prep_time_selector(tree)

    recipe['prep_time'] = prep_time[0].text_content().split(':')[1].strip()


    # ingredients
    ingredient_css_selector = CSSSelector('.ingredients-list__item')
    ingredients = ingredient_css_selector(tree)

    for ingredient in ingredients:
        recipe['ingredients'].append(ingredient.items()[2][1])


    # method
    method_css_selector = CSSSelector('.method__item > p')
    method = method_css_selector(tree)

    for step in method:
        recipe['method'].append(step.text_content())


    return recipe
