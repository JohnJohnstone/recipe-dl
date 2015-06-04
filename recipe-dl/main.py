import os
import sys
from urllib.parse import urlparse

from lxml import html

import requests


# Plugin code
package_directory = os.path.dirname(__file__)
path = os.path.join(package_directory, "plugins/")
plugins = {}

# Load plugins
sys.path.insert(0, path)

for f in os.listdir(path):
    fname, ext = os.path.splitext(f)
    if ext == '.py':
        mod = __import__(fname)
        plugins[fname] = mod.Plugin()
sys.path.pop(0)


plugin_sites = {}

for plugin in plugins.values():

    website_url = plugin.meta()['website']

    plugin_sites[website_url] = plugin


def get_raw_html(url):

    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}

    html = requests.get(url, headers=headers)

    return html

def get_recipe_dict(raw_html, plugin):

    tree = html.fromstring(raw_html.text)

    return plugin.parse(tree)

def get_lxml_tree(raw_html):

    tree = html.fromstring(raw_html.text)

    return tree

def has_plugin(url):

    """returns plugin if True else False"""

    parsed_url = urlparse(url).netloc

    if parsed_url in plugin_sites:

        plugin = plugin_sites[parsed_url]

        return plugin

    else:

        return False
