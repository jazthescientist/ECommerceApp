
# ---
# title: User Accounts
# description: Handles user accounts with functions for signup, login, and profile updates.
# author: Jazlynn Bailey
# date: 2024-11-13
# ---


# list to store user accounts
user_accounts = [
    {'username': 'byte_me', 'password': 'p@ssw0rd1'},
    {'username': 'function_fanatic', 'password': 'call_me_maybe'},
    {'username': '404_notfound', 'password': 'lost_in_code'}
]

def login(user):
    """Log in a user if credentials match any user in user_accounts."""
    for account in user_accounts:
        if account['username'] == user['username'] and account['password'] == user['password']:
            print(f"Welcome {user['username']}!")
            return True
    print("Invalid user credentials")
    return False

def signup(user):
    """Add a new user to user_accounts and display a confirmation message."""
    user_accounts.append(user)
    print(f"{user['username']} was added to user accounts")

def update_profile(user):
    """Update an existing user's profile if username matches and display a confirmation message."""
    for i, existing_user in enumerate(user_accounts):
        if existing_user['username'] == user['username']:
            user_accounts[i] = user
            print(f"{user['username']} has been updated in user accounts")
            return
    print(f"{user['username']} is not in user accounts")

# signup 
def test_signup():
    print("Testing signup function")
    new_user = {
        'username': 'new_user',
        'password': 'abc123'
    }
    signup(new_user)  # new user
    import pprint
    pprint.pprint(user_accounts)  # addition check 

# Test the login function
def test_login():
    print("Testing login function")
    
    # valid user
    valid_user = {'username': 'byte_me', 'password': 'p@ssw0rd1'}
    login(valid_user)  # "Welcome byte_me!"
    
    # invalid user
    invalid_user = {'username': 'byte_me', 'password': 'wrong_password'}
    login(invalid_user)  # "Invalid user credentials"

# update_profile test 
def test_update_profile():
    print("Testing update_profile function")
    
    # existing user with update
    updated_user = {
        'username': 'new_user',
        'password': 'new_password456'
    }
    update_profile(updated_user)  #update the profile new_user
    
    # update a non-existent user test 
    non_existent_user = {
        'username': 'nonexistent_user',
        'password': 'random_password'
    }
    update_profile(non_existent_user)  # user is not found
    
    import pprint
    pprint.pprint(user_accounts)  # update check  

# main guard test
if __name__ == '__main__':
    test_signup()
    test_login()
    test_update_profile()


