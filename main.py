"""The main program for Hunt the Wumpus"""
from cave import Cave
from character import Enemy

spawn = Cave("Spawn Area")
spawn.set_description("This is your spawn point.")
cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave")
grotto = Cave("Grotto")
grotto.set_description("A smale cave with ancient markings")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
serpents_cross = Cave("Serpents Cross")
serpents_cross.set_description("A titan serpents remains as a trail..")
walkers_road = Cave("Walkers Road")
walkers_road.set_description("A foggy road..")
runes_passage = Cave("Runes Passage")
runes_passage.set_description("A dark foggy Path..")
goveil_trail = Cave("Goveil Trail")
goveil_trail.set_description("A Bushy trail..")

harry = Enemy("harry", " A dirty, smelly Wumpus")
harry.set_conversation("Come closer. I cannot see you..")
harry.set_weakness(" vegemite")
dungeon.set_character(harry)

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

current_cave = cavern
dead = False
while dead is False:
    print("\n")
    current_cave.get_details()
    inhabitated = current_cave.get_character()
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ")
    if command in ["North", "East", "South", "West"]:
        current_cave = current_cave.move(command)
    elif command == "Talk":
        if inhabitated is not None:
            inhabitated.talk()
    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What do you want to fight with? ")
            if inhabitated.fight(fight_with) is True:
                print("Cravo, you have won the battle!")
                current_cave.set_character(None)
            else:
                print("Dog walk style home, You lost the fight")
    else:
        print("There is noone here to fight with.")
#End
