# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("ploneorgbr", "portal", "theme", "version.txt")).read().strip()

setup(name='ploneorgbr.portal.theme',
      version=version,
      description="",
      long_description=open(os.path.join("ploneorgbr", "portal", "theme", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme skin',
      author='Comunidade Plone.org.br',
      author_email='contato@plone.org.br',
      url='http://www.plone.org.br/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneorgbr', 'ploneorgbr.portal'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
