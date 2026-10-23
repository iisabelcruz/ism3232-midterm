# Setup Midterm
mkdir ism3232-midterm
touch business_rules.py main.py commands.md README.md
mkdir tests
cd tests
touch __init__.py test_business_rules.py
cd ism3232
code .

# Setting Up the Environment
python3 -m venv .venv
source .venv/bin/activate
which python 3              /Users/isabelcruz/ism3232-midterm/.venv/bin/python3
pip list                    Package and version of pip is stated
pip install pytest ruff
pip list                    List of packageS and version installed
pip freeze > reuirements.txt
cat requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitgignore
cat .gitignore 
ls -la
