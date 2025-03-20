
# ---
# title: Payment Processing
# description: Processes payments by calculating cart totals and applying discounts.
# author: Jazlynn Bailey
# date: 2024-11-13
# ---


# calculate the total price of the cart
def calculate_total(cart):
    """Calculate the total price for all items in the cart (each item has 'name', 'price', and 'quantity')."""
    total_price = sum([item['price'] * item['quantity'] for item in cart])
    print(f"The total price of the cart is {total_price:.2f}")
    return total_price

# apply a discount to a total amount
def apply_discount(total, discount):
    """Apply a discount to the total amount and display the discounted total."""
    discounted_total = total * (1 - discount)
    print(f"The cost is ${discounted_total:.2f} after applying a {discount*100:.1f}% discount to {total:.2f}")
    return discounted_total

# calculate_total 
def test_calculate_total():
    print("Testing calculate_total function")
    cart = [
        {'name': 'Item A', 'price': 10.00, 'quantity': 2},
        {'name': 'Item B', 'price': 5.50, 'quantity': 3},
        {'name': 'Item C', 'price': 2.75, 'quantity': 5}
    ]
    return calculate_total(cart)  # price for testing apply_discount

# apply_discount 
def test_apply_discount():
    print("Testing apply_discount function")
    total = test_calculate_total()  # total
    
    # applying different discounts
    apply_discount(total, 0.1)  # 10% discount
    apply_discount(total, 0.2)  # 20% discount
    apply_discount(total, 0.25)  # 25% discount

# main guard tests
if __name__ == '__main__':
    test_apply_discount()
