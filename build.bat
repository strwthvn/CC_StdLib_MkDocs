@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Building documentation site...
mkdocs build

echo Build complete! Output is in the 'site' directory
pause