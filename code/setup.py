from setuptools import setup, find_packages

NAME = 'biustestdocker'

REQUIRES = [
    'psycopg2-binary',
    'pandas'
]

DEPENDENCY_LINKS = []

setup(
    name=NAME,
    version="0.1.0",
    packages=find_packages(),
    install_requires=REQUIRES,
    dependency_links=DEPENDENCY_LINKS,
    description='',
    author='victoria.mohr@hellofresh.com'
)
