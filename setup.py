import os, sys
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirementes = [
    'pandas',
    'xgboost',
    'sklearn'
]
    
setup(
    name='sanfrancisco',
    version='0.0.1',
    description='mlops demo',
    long_description=readme,
    author='nobuyuki kuromatsu',
    author_email='n.kuromatsu@gmail.com',
    install_requires=requirementes,
    url='https://github.com/kuromt/sanfrancisco_house',
    license=license,
    entry_points=[
        'guild.models': [
            'predict_price=guild.model:PackageModel',
        ],
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
)