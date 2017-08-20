# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pypandoc import convert

long_description = convert('readme.md', 'rst')
with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='dockerregistry',
    version='0.1.0',
    description='Docker Registry Administration Helper',
    long_description=long_description,
    author='Katsuhiko Shibata',
    author_email='kshibata@seekers.jp',
    url='https://github.com/mokemoke88/docker_reg_helper',
    license=license,
    packages=find_packages(exclude=('tests','docs')),
    test_suite='tests',
    entry_points={
        'console_scripts':[
            'dockerregistry = dockerregistry.main:main',
        ],
    }
)
