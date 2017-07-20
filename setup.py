#!/usr/bin/env python

import os
import sys
from setuptools import setup

# Note: Please update version in pdb4amber.__version__
version = '1.4.1'
kws = dict(entry_points={
    'console_scripts': ['pdb4amber = pdb4amber.pdb4amber:main'],
})

setup(
    name='pdb4amber',
    version=version,
    zip_safe=False,
    description='PDB analyzer to prepare PDB files for Amber simulations.',
    author='Romain M. Wolf and AMBER developers',
    author_email='amber@ambermd.org',
    url='http://ambermd.org/',
    packages=['pdb4amber', 'pdb4amber.builder'],
    **kws)
