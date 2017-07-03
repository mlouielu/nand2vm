try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
"""


setup(name="nand2vm",
      description="nand2vm",
      long_description=long_description,
      license="MIT",
      version="0.1",
      author="Louie Lu",
      author_email="git@louie.lu",
      maintainer="Louie LU",
      maintainer_email="git@louie.lu",
      url="https://github.com/mlouielu/nand2vm",
      packages=['nand2vm'],
      test_suite='test',
      classifiers=[
          'Programming Language :: Python :: 3',
      ]
      )
