"""Cave class for Hunt the Wumpus"""
class Cave:
    """Defines attribute and methods for cave bjects"""
    def __init__(self, cave_name):
        """Sets the class attributes"""
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

    def set_name(self, cave_name):
        """Sets the cave name"""
        self.name = cave_name

    def get_name(self):
        """Gets the cave name"""
        return self.name
       
    def set_description(self, cave_description):
        """Sets the cave description"""
        self.description = cave_description

    def get_description(self):
        """Gets the cave description"""
        return self.description
    
    def describe(self):
        """Prints the cave's description"""
        print(self.description)

    def link_caves(self, cave_to_link, direction):
        """Populated dictionary of linked caves"""
        self.linked_caves[direction] = cave_to_link
        #print(self.name + " linked caves:" + repr(self.linked_caves))

    def get_details(self):
        """Prints details about te current cave"""
        print(self.name)
        print("----------")
        print(self.description)
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        """Allows movement between linked caves"""
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You cannot go that way.")
            return self
        
    def set_character(self, new_character):
        """Sets the chracter objects in the cave objects"""
        self.character = new_character

    def get_character(self):
        """Returns the name of character object in this cave"""
        return self.character
    