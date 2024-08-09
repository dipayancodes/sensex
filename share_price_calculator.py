investment = int(input("Enter your investment: "))
current_share_price = float(input("Current Share price: "))

total_share = investment / current_share_price 
total_share = float(total_share)
total_share = round(total_share, 2)

print(f" you can buy {total_share} shares of this stock")
