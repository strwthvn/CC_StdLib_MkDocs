@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Starting MkDocs server...
mkdocs serve

pause