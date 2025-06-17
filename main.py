"""The main program for Hunt the Wumpus"""
import os
from cave import Cave
from character import Enemy
from character import Character

def clear_console():
    """Clear the console function that clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


spawn = Cave("Spawn Area")
spawn.set_description("This is your spawn point, choose a path..")
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
stairs_to_life = Cave("Stairs to life")
stairs_to_life.set_description("Stairs that lead to what...type climb to start climbing")
castle_of_librety = Cave("abandoned caste")
castle_of_librety.set_description("an abandoned castle.?")
downstairs = Cave("downstairs.")
downstairs.set_description("where does this lead to?")
basement = Cave("Basement")
basement.set_description("A dark looking basement..")
weaponry = Cave("Filled with weapons.")
weaponry.set_description("Who was the owner of all this.?")
upstairs = Cave("Upstairs of the castle")
pathway = Cave("A long dark hallway.")
pathway.set_description("A long dark hallway that leads to two doors..")
left_room = Cave("Left Room.")
left_room.set_description("A old room filled with books")
right_room = Cave("A old office")
right_room.set_description("A old office..?")
outlook = Cave("view of the waters")
outlook.set_description("What a beautiful view..")
sales_of_good = Cave("Shop")
sales_of_good.set_description("A shop filled with items, talk to owner")

harry = Enemy("harry", " A dirty, smelly Wumpus")
harry.set_conversation("Come closer. I cannot see you..")
harry.set_weakness(" vegemite")
dungeon.set_character(harry)

owner = Character("Owner", "a chill guy")
owner.set_conversation("List: \n Sword \n Axe \n Pickaxe \n Dagger \n Spear \n Mace")
sales_of_good.set_character(owner)

spawn.link_caves(serpents_cross, "south")
spawn.link_caves(walkers_road, "north")
spawn.link_caves(goveil_trail, "west")
spawn.link_caves(runes_passage, "east")

serpents_cross.link_caves(cavern, "south")
goveil_trail.link_caves(stairs_to_life, "west")
runes_passage.link_caves(castle_of_librety, "east")

walkers_road.link_caves(sales_of_good, "north")
walkers_road.link_caves(spawn, "south")
sales_of_good.link_caves(walkers_road, "south")
owner = Character("Owner", "a chill guy")
owner.set_conversation("List: \n Sword \n Axe \n Pickaxe \n Dagger \n Spear \n Mace")
sales_of_good.set_character(owner)

goveil_trail.link_caves(stairs_to_life, "west")







current_cave = spawn
dead = False
while dead is False:
    clear_console()
    print("\n")
    current_cave.get_details()
    inhabitated = current_cave.character
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ").lower()
    if command in ["north", "east", "south", "west"]:
        current_cave = current_cave.move(command)
    
    elif command == "talk":
        clear_console()
        if inhabitated is not None:
            inhabitated.talk()
            item = input("What would you like to purchase? ").lower()

            available_items = ["sword", "axe", "pickaxe", "dagger", "spear", "mace"]
        
            if item in available_items:
                print(f"\nShop Owner: Great choice! This {item} is all yours to keep.")
                input("press enter to leave conversation.")
            else:
                print("\nShop Owner: Sorry, I dont have this item")
                input("Press enter to continue")

    elif command == "climb":
        clear_console()
        if current_cave == stairs_to_life:
            print("\nYouve began to climb, no going back now..")
            input("Press enter to continue the climb.")

            current_cave = Enemy#FIX
            print("\nYou have reached the very top, a boss fight arena..")
        else:
            print("\nYou have not yet reached the top yet. WAIT.")


    
    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What do you want to fight with? ")
            if inhabitated.fight(fight_with) is True:
                print("Bravo, you have won the battle!")
                current_cave.set_character(None)
            else:
                print("Dog walk style home, You lost the fight")
    else:
        print("There is noone here to fight with.")
        input()
#End
