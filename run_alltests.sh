#!/bin/sh
$(python --version 2> /dev/null)
if [ $? -eq 127 ]; then
    python3 -m unittest --verbose Testit/unittests.py Testit/endtoendtests.py
else
    python -m unittest --verbose Testit/unittests.py Testit/endtoendtests.py
fi