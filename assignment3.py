# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price, discount_percent):
    final_price = price*(1-discount_percent)
    if(discount_percent>=0.2):
        final_price = price*(1-discount_percent)
    else:
        final_price = price
    return final_price

final_price = calculate_discount(12000, 0.18)
print(final_price)

# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
price = float(input('Enter the price of the commoditites bought:'))
discount_percent = float(input('Enter the discount percent given:'))
def calculate_discount(price, discount_percent):
    final_price = price*(1-discount_percent)
    if(discount_percent>=0.2):
        final_price = price*(1-discount_percent)
    else:
        final_price = price
    return final_price
final = calculate_discount(price, discount_percent)
print(final)
