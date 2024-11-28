def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return(final_price)
    else:
        return(price)

try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        message = (
            f"The final price after applying the discount is: ${final_price:.2f}"
            if discount_percent >= 20
            else f"No discount applied. The original price is: ${price:.2f}"
        )
        print(message)
except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")