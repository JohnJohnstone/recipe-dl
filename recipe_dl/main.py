# imports: stdlib
import os
import importlib
import pathlib
import re
# imports: 3rd party
import requests
import lxml.html
import click

# config
package_directory = pathlib.Path(os.path.abspath(__file__)).parent
parsers_directory = package_directory.joinpath("parsers")
exporters_directory = package_directory.joinpath("exporters")


def gather_parsers(parsers_directory):
    """
    Gather parsers and return a list of parser dictionaries
    """
    parsers = []

    for path in parsers_directory.iterdir():
        if path.is_file():
            filename = path.name
            suffix = path.suffix
            name = filename.strip(suffix)
            module = importlib.import_module('.'.join(['parsers', name]))

            parser = {}

            parser['name'] = module.name
            parser['regex'] = module.regex
            parser['mod'] = module

            parsers.append(parser)

    return parsers


def get_html(url):
    """
    Pass in url and return html

    Args:
        url: website url (str)

    Returns:
        html: website html source (str)
    """
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
    request = requests.get(url, headers=headers)
    html = request.text
    return html


def get_lxml_tree(html):
    tree = lxml.html.fromstring(html)
    return tree


def get_parser(url, parsers):
    """
    Get matching parser from passed URL

    Returns:
        Parser: parser dict
    """
    for parser in parsers:
        match = parser['regex'].match(url)

        if match is not None:
            # logging
            # print('No match found using {}'.format(parser['mod'].name))
            return parser


def get_recipe(url):
    """ Pass in a url and return recipe as dict """
    parsers = gather_parsers(parsers_directory)
    parser = get_parser(url, parsers)
    html = get_html(url)
    tree = get_lxml_tree(html)
    recipe = parser['mod'].parse(tree)

    return recipe



# CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
# @click.command(context_settings=CONTEXT_SETTINGS)

@click.command()
@click.argument('url', default=False, required=True, type=str)
@click.option('--formatter', '-f', default='json', type=click.Choice(['html', 'pdf', 'json']), help='output format')
@click.option('--write', '-w', type=click.Path(resolve_path=True), help="write file")
def main(url, formatter, write):
    """
    recipe-dl: a program for downloading recipes from popular recipe websites

    """
    recipe = get_recipe(url)

    formatter = importlib.import_module('formatter.' + formatter)

    print(formatter.generate(recipe))

    # print(recipe)


if __name__ == '__main__':
    main()
