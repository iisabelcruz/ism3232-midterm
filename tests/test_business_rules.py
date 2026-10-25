from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)

# Tests for calculate_rental_cost


def test_calculate_rental_cost():
    assert round(calculate_rental_cost(60.00, 2), 2) == 120.00


# Tests for get_rental_discount
# Rule 2: Discounts depending on the number of rental days


def test_no_dicount_at_two_days():
    assert get_rental_discount(2) == 0.0


def test_standard_discount_at_three_days():
    assert get_rental_discount(3) == 0.10


def test_standard_discount_at_six_days():
    assert get_rental_discount(6) == 0.10


def test_long_rental_discount_at_seven_days():
    assert get_rental_discount(7) == 0.20


def test_contractor_gets_minimum_discount():
    assert get_rental_discount(2, False) == 0.0
    assert get_rental_discount(2, True) == 0.10


def test_contractor_keeps_higher_discount():
    assert get_rental_discount(7, True) == 0.20


# Tests for calculate_quote
# Rule 4: Damage waiver is applied if the discounted cost is less than $100


def test_calculate_quote_with_discount():
    assert round(calculate_quote(100.00, 3), 2) == 270.00


def test_damage_waiver_below_150():
    assert round(calculate_quote(149.99, 1), 2) == 174.99


def test_damage_waiver_at_150():
    assert round(calculate_quote(150.00, 1), 2) == 150.00


def test_no_damage_waiver_above_150():
    assert round(calculate_quote(150.01, 1), 2) == 150.01


# Tests for requires_deposit
# Rule 5: Deposit required at $1000 or more


def test_deposit_not_required_below_1000():
    assert requires_deposit(999.99) == False


def test_deposit_required_at_1000():
    assert requires_deposit(1000.00) == True


def test_deposit_required_above_1000():
    assert requires_deposit(1000.01) == True


# Tests for need_inspection
# Rule 6: Pickup inspection required when rental runs 5 days or more and its quote is over $800.


def test_inspectionn_not_required_at_four_days():
    assert needs_inspection(4, 900.00) is False


def test_inspection_required_at_five_days():
    assert needs_inspection(5, 900.00) is True


def test_inspection_not_required_at_800():
    assert needs_inspection(5, 800.00) is False


def test_inspection_required_above_800():
    assert needs_inspection(5, 800.01) is True


def test_inspection_not_required_when_both_conditions_fail():
    assert needs_inspection(4, 800.00) is False


# Tests for total_quoted


def test_total_quoted_with_two_rentals():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2},
        {"customer": "Chowdhurry", "daily_rate": 85.00, "days": 4},
    ]
    assert round(total_quoted(rentals), 2) == 451.00


def test_total_quoted_with_empty_list():
    assert round(total_quoted([]), 2) == 0.00


# Tests for largest_rental


def test_largest_rental_returns_largest_quote():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2},
        {"customer": "Eastman", "daily_rate": 210.00, "days": 8},
        {"customer": "Hughes", "daily_rate": 200.00, "days": 7},
    ]
    assert largest_rental(rentals) == "Eastman"


def test_largest_rental_keeps_first_customer_in_tie():
    rentals = [
        {"customer": "Brown", "daily_rate": 200.00, "days": 5},
        {"customer": "Chen", "daily_rate": 200.00, "days": 5},
    ]
    assert largest_rental(rentals) == "Brown"


def test_largest_rental_with_empty_list():
    assert largest_rental([]) == ""


# Tests for format_rental_line


def test_format_rental_line_with_no_deposit_or_inspection():
    result = format_rental_line("Alvarez", 145.00, False, False)
    assert result == ("Alvarez: $145.00 | deposit: no | inspection: no")


def test_format_rental_line_with_deposit_and_inspection():
    result = format_rental_line("Eastman", 1344.00, True, True)
    assert result == ("Eastman: $1344.00 | deposit: yes | inspection: yes")


def test_format_rental_line_with_deposit_only():
    result = format_rental_line("Eastman", 1000.00, True, False)
    assert result == ("Eastman: $1000.00 | deposit: yes | inspection: no")


def test_format_rental_line_with_inspection_only():
    result = format_rental_line("Dvorak", 960.00, False, True)
    assert result == ("Dvorak: $960.00 | deposit: no | inspection: yes")
