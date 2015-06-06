import os
import sys
import importlib

from urllib.parse import urlparse
from lxml import html

import requests

# Plugin code

package_directory = os.path.dirname(__file__)

plugin_dir = os.path.join(package_directory, "plugins/")

plugin_dir_list = os.listdir(plugin_dir)

def clean_plugin_dir_list(plugin_dir_list):

    i = plugin_dir_list
    i.remove('__init__.py')
    i.remove('__pycache__')

    return i

plugin_list = clean_plugin_dir_list(plugin_dir_list)

plugin_sites = {}

for f in plugin_list:

    fname, ext = os.path.splitext(f)

    if ext == '.py':

        module = importlib.import_module('recipe_dl.plugins' + '.' + fname)

        website = module.Plugin.website

        plugin_sites[website] = module.Plugin

        # print (plugin_sites)


def has_plugin(url):

    """returns plugin if True else False"""

    parsed_url = urlparse(url).netloc

    if parsed_url in plugin_sites:

        plugin = plugin_sites[parsed_url]

        # print(plugin)

        return plugin

    else:

        return False


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
