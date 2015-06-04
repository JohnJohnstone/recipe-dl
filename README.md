# recipe-dl

Python library and command-line application for downloading recipes.

recipe-dl currently utilises plugins written in python that scrape specific websites for recipes.

## Install

Install from reository using pip

`$ pip install git+https://github.com/Johnstone-Tech/recipe-dl.git`


## Command-line

```
    $ recipe-dl --help

    Usage: recipe-dl [OPTIONS] URL

    Options:
      -f, --format [html|pdf|pydict]  Output format
      -n, --filename PATH             Output filename
      -h, --help                      Show this message and exit.
```

### Examples

If you only pass a url to `recipe-dl` it will use the defualt output of html and save the file to the current directory.

```
 $ recipe-dl https://www.rivercottage.net/recipes/cambodian-wedding-day-dip
 saved to : Cambodian_wedding_day_dip.html
```

## Python library

return a python dict from a given url

```python

    import recipe-dl

    url = "www.recipe-site.com"
    raw_html = recipe-dl.get_raw_html(url)
    dict = recipe-dl.get_recipe_dict(raw_html, recipe-dl.has_plugin(url))

    print(dict)
```

#### Contact me

[johnstone-tech.co.uk](http://johnstone-tech.co.uk)
[GitHub @Johnstone-Tech](https://github.com/johnstone-tech)