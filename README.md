# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Isabel Cruz
- **Version:** Midterm Exam
- **Date:** October 25, 2026

## What This Program Does

This projects purpose was to quote customers rental equipment by the day from Ridgeline Tool Rental business. With this information use Python to test the company's business rules to create a report the owner can evaluate easily. This program uses 'busines_rules.py' to turn the company's six business rules into eight functions. 'main.py' imports these functions from 'business_rules.py' and runs them over eight provided rental orders that includes each customer's name, their daily rate for the rentals, the amount of days they are renting, and whether they are a contractor or not. 'main.py' runs these functions and prints a report that shows the results of each renters name and total, whether the renter required a deposit, whether the renter required an inspection. Following each renters information, the report shares the total amount of rentals, the average quote, the largest quote, the deposits required, and the inspections required, pulled from the rentals list provided.


## Business Rules

1. The rental cost is the daily rate time the number of days of rental. 
2. Rentals of fewer than 3 days do not receive a discount. Rentals of a minimum of 3 days or a max of 3 days receive a 10% discount. Rentals of 7 days or more receive a 20% discount.
3. If a customer is a contractor their rental quotes will always get a minimum of a 10% discount on their rental orders. This applies even if their rental is for less than 3 days. Contractors always get a 10% discount on their orders but it is not an additional 10% discount applied. For example, if they are renting between 3-6 days it would remain 10% discount as normal and if they are renting for 7 days or more it would remain at 20%, they would not receive an additional 10%. This rule is mainly to apply for contractors to receive a 10% discount with a rental of fewe then 3 days.
4. A $25 damage waiver is applied when the discounted cost is under $150.
5. A quote of $1,000 or more requires a deposit from the customer.
6. Any rental with a quote over $800 and rented for 5 or more days, needs a pickup inspection.

## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff format .
ruff check .
pytest -v
```

The test file has 28 tests, including both sides of every limit.

## Files in This Repository

- `business_rules.py`: the defined constants and the defined eight functions
- `main.py`: the provided list of rentals and the prints for a report
- `tests/test_business_rules.py`: the pytest tests for the functions
- `tests/__init__.py`: an empty file that lets the tests import the functions
- `commands.md`: the terminal commands that built and checked the project, with their output. Along with a organized list of the functions and tests written. 
- `README.md`: this current file
- `requirements.txt`: the packages to install for this program 
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository

## AI Use Statement

I did not use AI on this exam.