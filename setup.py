import os
from setuptools import setup, find_packages

# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(

    name='recipe_dl',
    version='0.1',

    description="food recipe downloader"
    # long_description=read(README.rst)

    url='https://github.com/Johnstone-Tech/recipe-dl'

    author='John Johnstone',
    author_email='john@johnstone-tech.co.uk',


    packages=find_packages(),

    install_requires=[

        'Click',
        'lxml',
        'requests',
        'fpdf',
        'preppy',
    ],

    entry_points='''
        [console_scripts]
        recipe-dl=recipe_dl.cli:get_recipe
    ''',

)