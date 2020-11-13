#! /bin/bash
# gen notes: make sure penv and pyinstaller are working
# Script for building standalone binary

rm -r dist build
env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.6.9
pyenv local 3.6.9
pip install https://github.com/pyinstaller/pyinstaller/tarball/develop

python setup.py install

pyinstaller --version
pyinstaller trezorCliTool.spec
