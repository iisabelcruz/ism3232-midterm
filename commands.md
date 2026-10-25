# Setup Midterm
```
mkdir ism3232-midterm

touch business_rules.py main.py commands.md README.md

mkdir tests

cd tests

touch __init__.py test_business_rules.py

cd ism3232

code .

```

# Setting Up the Environment
```
python3 -m venv .venv

source .venv/bin/activate

which python 3              /Users/isabelcruz/ism3232-midterm/.venv/bin/python3

pip list                    Package and version of pip is stated

pip install pytest ruff

pip list                    List of packages and version installed

pip freeze > reuirements.txt

cat requirements.txt

echo '.venv/' > .gitignore

echo '__pycache__/' >> .gitgignore

cat .gitignore 

ls -la
```
```
which python 3
```
```
/Users/isabelcruz/ism3232-midterm/.venv/bin/python3
```
The path ends in '.venv/bin/python3', so the project's virtual environment is active.

# The Project Structure
```
tree -L 2
```

```
.
├── __pycache__
│   └── business_rules.cpython-313.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```
.gitignore, .venv, and .pytest_cache are all files and folders that are on my computer but not in the Github repository because .gitignore and .venv is a file that tells Git what files and folders not to track.

# Every function and test

```
rg 'def'
```

```
business_rules.py
35:def calculate_rental_cost(daily_rate: float, days: int) -> float:
39:def get_rental_discount(days: int, contractor: bool = False) -> float:
53:def calculate_quote(
66:def requires_deposit(quote: float) -> bool:
70:def needs_inspection(days: int, quote: float) -> bool:
77:def total_quoted(rentals: list) -> float:
95:def largest_rental(rentals: list) -> str:
117:def format_rental_line(
```
business_rules.py defines 8 functions

```
tests/test_business_rules.py
14:def test_calculate_rental_cost():
20:def test_no_dicount_at_two_days():
23:def test_standard_discount_at_three_days():
26:def test_standard_discount_at_six_days():
29:def test_long_rental_discount_at_seven_days():
32:def test_contractor_gets_minimum_discount():
36:def test_contractor_keeps_higher_discount():
42:def test_calculate_quote_with_discount():
45:def test_damage_waiver_below_150():
48:def test_damage_waiver_at_150():
51:def test_no_damage_waiver_above_150():
57:def test_deposit_not_required_below_1000():
60:def test_deposit_required_at_1000():
63:def test_deposit_required_above_1000():
69:def test_inspectionn_not_required_at_four_days():
72:def test_inspection_required_at_five_days():
75:def test_inspection_not_required_at_800():
78:def test_inspection_required_above_800():
81:def test_inspection_not_required_when_both_conditions_fail():
86:def test_total_quoted_with_two_rentals():
93:def test_total_quoted_with_empty_list():
98:def test_largest_rental_returns_largest_quote():
106:def test_largest_rental_keeps_first_customer_in_tie():
113:def test_largest_rental_with_empty_list():
119:def test_format_rental_line_with_no_deposit_or_inspection():
125:def test_format_rental_line_with_deposit_and_inspection():
131:def test_format_rental_line_with_deposit_only():
137:def test_format_rental_line_with_inspection_only():
```
test_business_rules.py defines 28 functions


# Which files print

```
rg -l 'print'
```

```
main.py
```

# The commit story

```
git log --oneline
```
```
5c98364 (HEAD -> main, origin/main) Fixed rental report and organized imports
228caf6 Add updated contene to README.md for others to interpret better this project
ba624a1 Adding current git log to commands
8eb08b2 Added commands before final commit story and previewing the github visuals
4a4444a Testing blocks for command.md
50fbcf8 Add Tests for the Rules of cost, discounts, applying waiver, inspection, and deposit for the rental limitation
3646b0f Add rentals list and access to run a report
85868dd Add rental costs and rental discount rules
c3ee46d Set Up of Midterm From the Terminal
```