import os
from setuptools import setup

# https://pythonhosted.org/an_example_pypi_project/setuptools.html

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PYTHON_TOTAL_DOC",
    version = "0.1",
    author = "Benjamín Neira",
    author_email = "bneira@gmail.com",
    description = ("ESTA ES UNA DISTRIBUCIÓN DE PRUEBA"),
    keywords = "PRUEBA DISTRIBUCIÓN PYTHON",
    packages=['PYTHON_TOTAL_DOC', 'PYTHON_TOTAL_DOC.SUB_PYTHON_TOTAL'],
    classifiers=[],
)

