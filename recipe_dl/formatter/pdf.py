import os
import importlib
import preppy as p

from fpdf import FPDF, HTMLMixin


def get_html(recipe):
    """
    Generate HTML using formatter.html
    """
    html = importlib.import_module('formatter.html')
    output = html.generate(recipe)
    return output


def generate(recipe):
    """
    Generate PDF

    """

    class MyFPDF(FPDF, HTMLMixin):
        pass

    pdf = MyFPDF()

    pdf.compress = False

    pdf.add_page()


    markup = get_html(recipe)
    pdf.write_html(markup)

    # write to file
    # pdf.output(filename, 'F')
    # stdout
    output = pdf.output()

    return output
