#!/bin/sh
$(python --version 2> /dev/null)
if [ $? -eq 127 ]; then
    python3 -m unittest Testit/unittests.py
else
    python -m unittest Testit/unittests.py
fi