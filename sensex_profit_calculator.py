def calculate_profit(initial_premium, investment_amount, new_premium):
    num_contracts = investment_amount / initial_premium
    final_value = num_contracts * new_premium
    profit = final_value - investment_amount
    return profit
    
initial_premium = float(input("Enter the premium price you purchased: "))
investment_amount = float(input("Enter the amount you invested: "))
new_premium = float(input("Enter the premium price you sell: "))

profit = calculate_profit(initial_premium, investment_amount, new_premium)
round_profit = round(profit, 2)
print(f"The profit is: ₹{round_profit}")
