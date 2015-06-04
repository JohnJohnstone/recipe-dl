import os
import preppy as p

from fpdf import FPDF, HTMLMixin

export_dir = os.path.dirname(__file__)
default_template = os.path.join(export_dir, "pdf/default.prep")


def gen_pdf(recipe_dict, markup, filename):

    class MyFPDF(FPDF, HTMLMixin):
        pass

    pdf = MyFPDF()

    pdf.compress = False

    pdf.add_page()

    pdf.write_html(markup)

    pdf.output(filename, 'F')