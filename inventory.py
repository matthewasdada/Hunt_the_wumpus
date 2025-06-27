class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            print(f"You picked up: {item}")
        else:
            print(f"You already own this {item}.")
    
    def pick_up_key(self, inventory):
        key_name = "Basement Key"
        inventory.add_item(key_name)
    
    def has_item(self, item):
        return item in  self.items

    def enter_basement(self, inventory):
        if inventory.has_item("Basement Key"):
            print("You have unlocked the basement door.")
        else:
            print("This door is locked, requires a key to enter")

    player_inventory = Inventory()
    pick_up_key(player_inventory)
    enter_basement(player_inventory)

    