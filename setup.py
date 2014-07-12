import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'rosie',
    version = '0.0.5-dev',
    author = 'Guy Jacks',
    author_email = 'guy.jacks@gmail.com',
    description = 'Rosie works hard to make state machines easy!',
    long_description = read('README'),
    packages = find_packages()
)
