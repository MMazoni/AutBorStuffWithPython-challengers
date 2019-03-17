# Fantasy Game Inventory
def displayInventory(bag):
    """Display the inventory information with the itens and quantity"""
    print("Inventory:")
    item_total = 0
    for k, v in bag.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))
    print('\n')


stuff = {'dagger': 1, 'shield': 1, 'apple juice': 6, 'Pupa card': 1, 'gold coin': 139}

displayInventory(stuff)

# List to Dictionary Function for Fantasy Game Inventory
def addToInventory(inventory, addedItems):
    '''Add items to the inventory'''
    for i in addedItems:
        for k, v in inventory.items():
            if i in k:
                inventory[k] = v + 1
            else:
                inventory.setdefault(i, 1)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)