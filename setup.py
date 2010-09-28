""" Installer
"""
from setuptools import setup, find_packages
import os
from sys import version_info

NAME = 'naaya.sql'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

requires = ['setuptools']
if version_info < (2, 5):
    requires.append('pysqlite2')

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
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['naaya'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
