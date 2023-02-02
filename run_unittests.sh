#!/bin/sh
$(python --version 2> /dev/null)
if [ $? -eq 127 ]; then
    python3 -m unittest --verbose Testit/unittests.py
else
    python -m unittest --verbose Testit/unittests.py
fi