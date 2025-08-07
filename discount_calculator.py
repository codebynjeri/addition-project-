def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Test with sample values
price = 100
discount = 25

final_price = calculate_discount(price, discount)
print("Final price:", final_price)

