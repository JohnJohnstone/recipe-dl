import os
from setuptools import setup, find_packages

# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(

    name='recipe_dl',
    version='0.1',

    description="food recipe downloader",
    long_description=readme,


    url='https://github.com/Johnstone-Tech/recipe-dl',

    author='John Johnstone',
    author_email='jjohnstone@riseup.net',


    packages=find_packages(),
    include_package_data = True,

     package_data = {
        # If any package contains *.txt files, include them:
        '': ['*.prep'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        'recipe_dl': ['formatter/html/*.prep'],
    },

    install_requires=[

        'Click',
        'lxml',
        'requests',
        'fpdf',
        'preppy',
    ],

    entry_points='''
        [console_scripts]
        recipe-dl=recipe_dl.main:main
    ''',

)
