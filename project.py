
# Currency Converter Program

EXCHANGE_RATES = {
    'INR': 1.0,
    'USD': 83.0,
    'EUR': 90.0,
    'GBP': 105.0
}

# Convert currency into INR
def convert_to_inr(amount, from_curr):
    return amount * EXCHANGE_RATES[from_curr]


# Main conversion function
def convert_currency(amount_str, from_curr, to_curr):

    # Convert currency codes to uppercase
    from_curr = from_curr.upper()
    to_curr = to_curr.upper()

    # Check valid currencies
    if from_curr not in EXCHANGE_RATES:
        return "Unsupported source currency!"

    if to_curr not in EXCHANGE_RATES:
        return "Unsupported target currency!"

    # Check amount
    try:
        amount = float(amount_str)
    except ValueError:
        return "Invalid amount! Enter a number."

    # Check negative amount
    if amount < 0:
        return "Amount cannot be negative!"

    # Convert into INR
    amount_in_inr = convert_to_inr(amount, from_curr)

    # Convert into target currency
    final_amount = amount_in_inr / EXCHANGE_RATES[to_curr]

    # Display result
    amount_display = int(amount) if amount.is_integer() else amount

    return f"{amount_display} {from_curr} = {final_amount:.2f} {to_curr}"


# Main Program
if __name__ == "__main__":

    print("================================")
    print("       CURRENCY CONVERTER")
    print("================================")

    while True:

        print("\nAvailable Currencies: INR, USD, EUR, GBP")

        amount = input("Enter amount: ")
        from_curr = input("From currency: ")
        to_curr = input("To currency: ")

        result = convert_currency(amount, from_curr, to_curr)

        print("\nResult:", result)

        choice = input("\nConvert again? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for using Currency Converter!")
            break
