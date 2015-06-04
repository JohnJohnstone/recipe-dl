import click
# import recipe-dl module
from recipe_dl import main as rd
# Export Functions
from recipe_dl.export import html
from recipe_dl.export import pdf


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--format', '-f', default='html', type=click.Choice(['html', 'pdf', 'pydict']), help='Output format')
@click.option('--filename', '-n', type=click.Path(resolve_path=True), help="Output filename")
@click.argument('url', default=False, required=True, type=str)
def get_recipe(url, format, filename):
    """recipe-dl is a simple recipe downloader"""
    if url == False:

        click.echo('Have you provided the URL argument')

    else:

        if rd.has_plugin(url) == False:

            click.echo('No Plugin Available')

        else:

            raw_html = rd.get_raw_html(url)

            dict = rd.get_recipe_dict(raw_html, rd.has_plugin(url))

            markup = html.gen_html(dict)

            recipe_name = dict['name'].replace(" ", "_")

            filename = recipe_name + '.'+ format

            saved = click.echo('saved to : %s' % filename)

            if format == 'html':

                markup = html.gen_html(dict)

                saved

                with click.open_file(filename, 'w') as f:

                    f.write(markup)

            elif format == 'pdf':

                pdf.gen_pdf(dict, markup, filename)

                saved

            elif format == 'pydict':

                click.echo(dict)

            else:

                pass