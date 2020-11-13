#! /bin/bash
# Script for building standalone binary

rm -r dist build
# env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.6.8
pyenv local 3.6.8
#pip install https://github.com/pyinstaller/pyinstaller/tarball/develop

# python setup.py install


pyinstaller trezorCliTool.spec
