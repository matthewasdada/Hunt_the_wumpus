class Cave:
    def __init__(self, cave_name):
        self.name = None
        self.description = None
        self.linked_caves =

    def set_name(self, cave_name):
        self.name = cave_name

    def get_name(self):
        return self.name
       
    def set_description(self, cave_description):
        self.description = cave_description

    def get_description(self):
        return self.description
    
    def describe(self):
        print(self.description)