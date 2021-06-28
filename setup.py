from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Calculator',
    url='https://github.com/Abimbola-ai/simple-calculator',
    author='Abimbola Ojikutu',
    author_email='abimbola.ojikutu@ubh.de',
    # Needed to actually package something
    packages=['calculator'],
    # Needed for dependencies
    install_requires=['pytest'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A simple calculator for your math run',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)