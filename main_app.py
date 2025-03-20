
# ---
# title: Main App
# description: Main app file that integrates functions for inventory, user accounts, and payment processing.
# author: Jazlynn Bailey
# date: 2024-11-13
# inputs: Item details, user information, and cart contents for testing functions
# outputs: Confirmation messages, total cart price, and discounted price after applying discount
# ---

import inventory
import user_accounts
import payment_processing

# main function
def main():
    # add item to inventory
    item1 = {
        'name': 'Tabletop Ironing Board',
        'description': 'Compact ironing board for quick ironing needs.',
        'seller': 'Amazon Basics',
        'price': 20.99,
        'quantity': 100
    }
    inventory.add_item(item1)

    # sign up user
    user1 = {'username': 'new_user', 'password': 'abc123'}
    user_accounts.signup(user1)

    # log in user
    user_accounts.login({'username': 'new_user', 'password': 'abc123'})

    # sample cart for calculating total
    cart = [
        {'name': 'Item A', 'price': 10.00, 'quantity': 2},
        {'name': 'Item B', 'price': 5.50, 'quantity': 3},
        {'name': 'Item C', 'price': 2.75, 'quantity': 5}
    ]
    # calculate total
    total = payment_processing.calculate_total(cart)

    # apply discount
    payment_processing.apply_discount(total, 0.1)

# main guard
if __name__ == '__main__':
    main()
