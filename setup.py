""" Installer
"""
from setuptools import setup, find_packages
import os
from sys import version_info

NAME = 'naaya.sql'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

requires = []
if version_info < (2, 5):
    requires.append('pysqlite')

setup(name=NAME,
      version=VERSION,
      description="",
      long_description=open("README.rst").read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='naaya sql',
      author='Eau de Web',
      author_email='office@eaudeweb.ro',
      url='http://naaya.eaudeweb.ro',
      packages=find_packages(),
      namespace_packages=['naaya'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
