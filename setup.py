from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='lab5Popovych',
    version='0.2',
    description='Bracket validatior for string matching',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    install_requires=[

    ]
)