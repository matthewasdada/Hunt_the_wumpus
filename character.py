"""Character class for Hunt the Wumpus"""
class Character:
    """Defines attributes and methods for Character objects"""
    def __init__(self, char_name, char_description):
        """Sets the class attributes"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Displays information about the character"""
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Sets what the character can say"""
        self.conversation = conversation
    
    def talk(self):
        """Allows chracters to talk to the player"""
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + "does not want to talk to you.")

    def fight(self):
        """Allows characters to fight with the player"""
        print(self.name + "does not want to fight you")
        return True

class Enemy(Character):
    """Defines attributes and methods for the Enemy sub-class"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if self.weakness is None:
            print(f"{self.name} has no weakness. You cant not defeat Harry..")
            return False
        
        if combat_item.strip().lower() == self.weakness.strip().lower():
            print(f"You fend off {self.name} off with {combat_item}.") 
            return True
        else:
            print(self.name + " swallows you whole! You died.")
            return False    