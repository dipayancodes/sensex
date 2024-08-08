def calculate_quantity(amount, premium_price=100, lot_size=10):
    cost_per_lot = premium_price * lot_size
    number_of_lots = amount // cost_per_lot
    quantity = number_of_lots * lot_size
    return quantity

# Example usage
lot_size = 10
amount = int(input("Enter your amount: "))
quantity = calculate_quantity(amount)
print(f"With ₹{amount}, you can trade {quantity} contracts of {quantity / lot_size} lots")

