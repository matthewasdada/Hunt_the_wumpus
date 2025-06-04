from character import Enemy

harry = Enemy("harry", " A dirty, smelly Wumpus")
harry.describe()
harry.set_conversation("Come closer. I cannot see you..")
harry.talk()
print(harry)