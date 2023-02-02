#!/bin/sh
$(python --version 2> /dev/null)
if [ $? -eq 127 ]; then
    python3 -m coverage run --branch -m unittest Testit/unittests.py
    python3 -m coverage html
    python3 -m coverage report --format=markdown
else
    python -m coverage run --branch -m unittest Testit/unittests.py
    python -m coverage html
    python3 -m coverage report --format=markdown
fi
cp ./htmlcov/index.html ./Dokumentaatio/Coverage_report.html
echo Created Coverage_report.html under /Dokumentaatio