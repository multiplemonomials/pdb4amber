#!/bin/sh

if [ "$NO_SETUPTOOLS" = "True" ]; then
   python setup.py install --no-setuptools
else
   pip install . -v --upgrade
fi
