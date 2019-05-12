import re
from lxml.cssselect import CSSSelector

# Plugin name as a string
name = "River Cottage"

# Plugin website URL as string
regex = re.compile('\S*rivercottage\.net')

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
    name_css_selector = CSSSelector('h1')
    name = name_css_selector(tree)

    recipe['name'] = name[0].text

    # cook time
    cook_time_selector = CSSSelector('.hm__minutes')
    cook_time = cook_time_selector(tree)

    try:
        recipe['cook_time'] = cook_time[1].text
    except:
        recipe['cook_time'] = ''


    # prep time
    prep_time_selector = CSSSelector('.hm__minutes')
    prep_time = prep_time_selector(tree)

    try:
        recipe['prep_time'] = prep_time[0].text
    except:
        recipe['prep_time'] = ''


    # ingredients
    ingredient_css_selector = CSSSelector('.ingredients__list > ul > li')
    ingredients = ingredient_css_selector(tree)

    for ingredient in ingredients:
        ingredient = ingredient.text_content()
        recipe['ingredients'].append(ingredient)


    # method
    method_css_selector = CSSSelector('.recipe-detail__content > p')
    method = method_css_selector(tree)

    for step in method:
        step = step.text_content()
        recipe['method'].append(step)


    return recipe
