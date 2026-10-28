#!/usr/bin/env bash
set -eu
python3 --version
python3 -m py_compile *.py
echo "Python source compiles. Confirm Python and Python Debugger extensions in VS Code."
