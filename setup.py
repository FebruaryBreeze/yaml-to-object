"""
Generate Python Class & Object from YAML file
Author: SF-Zhou
Date: 2019-01-03
"""

from setuptools import setup

name = 'yaml_to_object'
setup(
    name=name,
    version='0.0.7',
    description='Generate Python Class & Object from YAML file',
    url=f'https://github.com/SF-Zhou/{name.replace("_", "-")}',
    author='SF-Zhou',
    author_email='sfzhou.scut@gmail.com',
    keywords='YAML class object',
    py_modules=[f'{name}'],
    install_requires=['pyyaml']
)
