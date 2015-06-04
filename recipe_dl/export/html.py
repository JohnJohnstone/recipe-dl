import preppy as p
import os.path

export_dir = os.path.dirname(__file__)

default_template = os.path.join(export_dir, "html/default.prep")

def gen_html(recipe_dict):

    mymodule = p.getModule(default_template)

    name = recipe_dict['name']
    ingredients = recipe_dict['ingredients']
    method = recipe_dict['method']

    html = mymodule.get(name, ingredients, method)

    return html