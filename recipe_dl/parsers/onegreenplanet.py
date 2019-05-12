import re
from lxml.cssselect import CSSSelector

# Plugin name as a string
name = "One Green Planet"

# Plugin website URL as string
regex = re.compile('\S*onegreenplanet\.org')

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
    name_css_selector = CSSSelector('.recope-title')
    name = name_css_selector(tree)

    recipe['name'] = name[0].text


    # ingredients
    ingredient_css_selector = CSSSelector('.recipe-ingredients > ul > li')
    ingredients = ingredient_css_selector(tree)

    for ingredient in ingredients:
        ingredient = ingredient.text_content().replace(u'\xa0',' ')
        recipe['ingredients'].append(ingredient)


    # method
    method_css_selector = CSSSelector('.recipe-preparation > ol > li')
    method = method_css_selector(tree)

    for step in method:
        recipe['method'].append(step.text_content().strip())

    # from ptpython.repl import embed
    # embed(globals(), locals())

    return recipe
