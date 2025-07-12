class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            print(f"You picked up: {item}")
        else:
            print(f"You already own this {item}.")
    
    def pick_up_key(self):
        key_name = "Basement Key"
        self.add_item(key_name)
    
    def has_item(self, item):
        return item in  self.items

    def enter_basement(self):
        if self.has_item("Basement Key"):
            print("You have unlocked the basement door.")
        else:
            print("This door is locked, requires a key to enter")

    def list_items(self):
        if self.items:
            print("The items you have are:")
            for item in self.items:
                print(f" - {item}")
        
        else:
            print("You have nothing in your inventory.")