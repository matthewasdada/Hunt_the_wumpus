from cave import Cave

cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave")
grotto = Cave("Grotto")
grotto.set_description("A smale cave with ancient markings")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

cavern.get_details()
dungeon.get_details()
grotto.get_details()