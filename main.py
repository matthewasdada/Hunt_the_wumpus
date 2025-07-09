"""The main program for Hunt the Wumpus"""
import os
from cave import Cave
from character import Enemy
from character import Character
from inventory import Inventory

player_inventory = Inventory()

def clear_console():
    """Clear the console function that clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


spawn = Cave("Spawn Area")
spawn.set_description("This is your spawn point, choose a path..")
cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave")
grotto = Cave("Grotto")
grotto.set_description("A smale cave with ancient markings..type ____ to go back")
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
castle_of_librety = Cave("abandoned castle")
castle_of_librety.set_description("an abandoned castle.?")
downstairs = Cave("downstairs of the castle")
downstairs.set_description("where does this lead to?")
basement = Cave("Basement")
basement.set_description("A dark looking basement..")
weaponry = Cave("A kings old weaponary room")
weaponry.set_description("Who was the owner of all this.?")
upstairs = Cave("upstairs of the castle")
pathway = Cave("A long dark hallway")
pathway.set_description("A long dark hallway that leads to two doors")
left_room = Cave("Left Room")
left_room.set_description("A old room filled with books")
right_room = Cave("Right room")
right_room.set_description("A old office..?")
outlook = Cave("outlook view")
outlook.set_description("What a beautiful view..type ____ to go back")
sales_of_good = Cave("Shop")
sales_of_good.set_description("A shop filled with items, talk to owner")

harry = Enemy("harry", " A dirty, smelly Wumpus")
harry.set_conversation("Come closer. I cannot see you..")
harry.set_weakness(" vegemite")
dungeon.set_character(harry)

owner = Character("a cool Owner", "what would you like to do?")
owner.set_conversation("List: \n Bottle \n Toilet paper \n Toothbrush \n Spoon \n Fork \n Plate")
sales_of_good.set_character(owner)

spawn.link_caves(serpents_cross, "south")
spawn.link_caves(walkers_road, "north")
spawn.link_caves(goveil_trail, "west")
spawn.link_caves(runes_passage, "east")

serpents_cross.link_caves(cavern, "south")
serpents_cross.link_caves(spawn, "north")
cavern.link_caves(serpents_cross,"north")
cavern.link_caves(outlook, "east")
cavern.link_caves(grotto, "west")
grotto.link_caves(cavern, "east")
outlook.link_caves(cavern, "west")

goveil_trail.link_caves(stairs_to_life, "west")
runes_passage.link_caves(castle_of_librety, "east")
runes_passage.link_caves(spawn, "north")
castle_of_librety.link_caves(upstairs, "north")
castle_of_librety.link_caves(downstairs, "west")
castle_of_librety.link_caves(runes_passage, "south")
upstairs.link_caves(pathway, "north")
upstairs.link_caves(castle_of_librety, "south")
pathway.link_caves(upstairs, "south")
pathway.link_caves(right_room, "east")
right_room.link_caves(pathway, "west")
left_room.link_caves(pathway, "east")
pathway.link_caves(left_room, "west")
downstairs.link_caves(basement, "north")
downstairs.link_caves(castle_of_librety, "south")
basement.link_caves(weaponry, "north")#requires a key to get from right room FIX
basement.link_caves(downstairs, "south")
weaponry.link_caves(basement, "south")



walkers_road.link_caves(sales_of_good, "north")
walkers_road.link_caves(spawn, "south")
sales_of_good.link_caves(walkers_road, "south")

current_cave = spawn
dead = False
while dead is False:
    clear_console()
    print("\n")
    current_cave.get_details()
    print(f" Location: {current_cave.get_name()}")
    inhabitated = current_cave.character

    if current_cave == right_room and not player_inventory.has_item("Basement Key"):
        print("\nA old rusty key wonder what it's used for..")
        print("Do you want to pick up old rusty key..? yes or no")
        pick_key = input().lower()
        if pick_key == "yes":
            player_inventory.pick_up_key()
            input("Press enter to continue")
        else:
            print("Dont pick up mysterious key..")
            input("Press enter to continue")
        
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ").lower()
    if command in ["north", "east", "south", "west"]:
        if current_cave == downstairs and command == "north":
            if player_inventory.has_item("Basement Key"):
                current_cave = current_cave.move(command)
                print("You have unlocked the basement that has a dark  mysterious room ")
                input("press enter to continue")

                current_cave = current_cave.move("north")
                print("You are now in the kings weaponry room.")
                print(f" Location: {current_cave.get_name()}")
                input("Press enter to continue")
            else:
                print("\nThe basement door is locked, it requires a key to unlock..")
                input("press enter to continue")
        else:
            current_cave = current_cave.move(command)
                
    
    elif command == "talk":
        clear_console()
        if inhabitated is not None:
            inhabitated.talk()
            item = input("What would you like to purchase? ").lower()

            available_items = ["bottle", "toilet paper", "toothbrush", "spoon", "fork", "plate"]
        
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

            arena = Cave("Boss Fight Arena")
            arena.set_description("good boy land")
            current_cave = arena
            print("\nYou have reached the very top, a boss fight arena..")
            boss = Enemy("bossman", " A good boy")
            arena.set_character(boss)
            current_cave.get_details()

    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What do you want to fight with? ").lower()
            if inhabitated.fight(fight_with):
                print("Bravo, you have won the battle!")
                current_cave.set_character(None)
            else:
                print("Dog walk style home, You lost the fight")
            input("Press enter to continue..")
    else:
        print("There is noone here to fight with.")
        input("press enter to continue")
#End