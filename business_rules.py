# Business Rules for Ridgeline Tool Rental
# Author: Isabel Cruz

# Rule #2: the discount depends on the number of rental days

STANDARD_DISCOUNT_MIN_DAYS = 3
LONG_RENTAL_MIN_DAYS = 7
NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.10
LONG_RENTAL_DISCOUNT = 0.20

# Rule #3: Automatic Licensed Contractors Discount 

CONTRACTOR_MIN_DISCOUNT = 0.10

# Rule #4: Damage Waiver Applied on discounted costs below $150

DAMAGE_WAIVER_THRESHOLD = 150.00
DAMAGE_WAIVER_COST = 25.00
FULL_PRICE = 1.00
DECIMAL_PLACES = 2


# Rule 5: Deposit Required at a quote of $1000 OR more

DEPOSIT_THRESHOLD = 1000.00

# Rule 6: Pickup Inspection Required when rental runs 5 days or more and its quote is over $800

INSPECTION_MIN_DAYS = 5
INSPECTION_QUOTE_THRESHOLD = 800.00



def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return the rental cost before discount."""
    return daily_rate * days

def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the discount rate for the rental."""
    if days >= LONG_RENTAL_MIN_DAYS:
        discount = LONG_RENTAL_DISCOUNT
    elif days >= STANDARD_DISCOUNT_MIN_DAYS:
        discount = STANDARD_DISCOUNT
    else:
        discount = NO_DISCOUNT

    if contractor and discount < CONTRACTOR_MIN_DISCOUNT:
        discount = CONTRACTOR_MIN_DISCOUNT

    return discount 

def calculate_quote(
        daily_rate: float, days: int, contractor: bool = False
) -> float:
    """Return the discounted rental quote including any damage waiver."""
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    discounted_cost = cost * (FULL_PRICE - discount)

    if discounted_cost < DAMAGE_WAIVER_THRESHOLD:
        discounted_cost += DAMAGE_WAIVER_COST

    return round(discounted_cost, DECIMAL_PLACES)

def requires_deposit(quote: float) -> bool:
    """Return True when a deposit is required."""
    return quote >= DEPOSIT_THRESHOLD

def needs_inspection(days: int, quote: float) -> bool:
    """Return True when a pickup inspection is required."""
    return (
        days >= INSPECTION_MIN_DAYS
        and quote > INSPECTION_QUOTE_THRESHOLD
    )

def total_quoted(rentals: list) -> float:
    """Return the total of all rental quotes."""
    total = 0.0

    for rental in rentals:
        if "contractor" in rental:
            contractor = rental["contractor"]
        else:
            contractor = False   
        quote = calculate_quote(
            rental["daily_rate"],
            rental["days"],   
            contractor
        )
        total += quote

    return round(total, DECIMAL_PLACES)

def largest_rental(rentals: list) -> str:
    """Return the customer with the largest quote."""
    largest_customer = ""
    largest_quote = None

    for rental in rentals:
        if "contractor" in rental:
            contractor = rental["contractor"]
        else:
            contractor = False   
        quote = calculate_quote(
            rental["daily_rate"],
            rental["days"],
            contractor
        
        )
        if largest_quote is None or quote > largest_quote:
            largest_quote = quote
            largest_customer = rental["customer"]

    return largest_customer

def format_rental_line(
        customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Return one formatted line for the rental report."""
    deposit_text = "no"
    inspection_text = "no"

    if deposit:
        deposit_text = "yes"

    if inspection:
        inspection_text = "yes"

    return (
        f"{customer}: ${quote:.2f} | "
        f"deposit: {deposit_text} | "
        f"inspection: {inspection_text}"
    )        
