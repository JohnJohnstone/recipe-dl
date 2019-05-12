import preppy
import os.path

formatter_dir = os.path.dirname(__file__)
template = os.path.join(formatter_dir, "html/default.prep")

def generate(recipe):
    """
    Generate HTML
    """
    mymodule = preppy.getModule(template)

    name = recipe['name']
    ingredients = recipe['ingredients']
    method = recipe['method']

    html = mymodule.get(name, ingredients, method)

    return html
