# ---
# title: Inventory 
# description: Manages inventory functions including adding, removing, and updating items in inventory.
# author: Jazlynn Bailey
# date: 2024-11-13
# ---


# inventory list
inventory = []

def add_item(item):
    """Add an item to the inventory and display a confirmation message."""
    inventory.append(item)
    print(f"{item['name']} was added to the inventory")

def remove_item(item):
    """Remove an item from the inventory and display a confirmation message."""
    if item in inventory:
        inventory.remove(item)
        print(f"{item['name']} was removed from the inventory")
    else:
        print(f"{item['name']} is not in the inventory")

def update_inventory(item):
    """Update an item in the inventory if it exists and display a confirmation message."""
    for i, existing_item in enumerate(inventory):
        if existing_item['name'] == item['name']:
            inventory[i] = item
            print(f"{item['name']} has been updated in the inventory")
            return
    print(f"{item['name']} is not in the inventory")

# add_item 
def test_add_item():
    print("Testing add_item function")
    item = {
        'name': 'Tabletop Ironing Board',
        'description': 'Compact tabletop ironing board for pressing garments and linens, craft projects, and quick ironing needs.\nMachine-washable cover can be easily removed and replaced; extra thick padding with a smooth, reticulated surface that dissipates heat and vapor.\nDimensions: 23.6" x 14.3" x 7.1"',
        'seller': 'Amazon Basics',
        'price': 20.99,
        'quantity': 100
    }
    add_item(item)
    import pprint
    pprint.pprint(inventory)  # inventory check 

# remove_item 
def test_remove_item():
    print("Testing remove_item function")
    item = {
        'name': 'Tabletop Ironing Board',
        'description': 'Compact tabletop ironing board for pressing garments and linens, craft projects, and quick ironing needs.\nMachine-washable cover can be easily removed and replaced; extra thick padding with a smooth, reticulated surface that dissipates heat and vapor.\nDimensions: 23.6" x 14.3" x 7.1"',
        'seller': 'Amazon Basics',
        'price': 20.99,
        'quantity': 100
    }
    remove_item(item)
    import pprint
    pprint.pprint(inventory)  # inventory check 

# update_inventory 
def test_update_inventory():
    print("Testing update_inventory function")
    
    # add 
    item = {
        'name': 'Tabletop Ironing Board',
        'description': 'Compact tabletop ironing board for pressing garments and linens, craft projects, and quick ironing needs.\nMachine-washable cover can be easily removed and replaced; extra thick padding with a smooth, reticulated surface that dissipates heat and vapor.\nDimensions: 23.6" x 14.3" x 7.1"',
        'seller': 'Amazon Basics',
        'price': 20.99,
        'quantity': 100
    }
    add_item(item)  # add item 
    
    # updated item 
    item2 = {
        'name': 'Tabletop Ironing Board',
        'description': 'Updated description for ironing board.',
        'seller': 'Amazon Essentials',
        'price': 25.99,
        'quantity': 150
    }
    
    
    update_inventory(item2)
    import pprint
    pprint.pprint(inventory)  # inventory check 

# main guard test 
if __name__ == '__main__':
    test_add_item()
    test_update_inventory()
    test_remove_item()
