import random
from enum import Enum
from game_informations import GameAttributes
from game_character import player_equipment
from game_character import player_backpack


class DropEqItems():

    def __init__(self,item_name="test_item", health="Health", mana="Mana", attack="Attack", defence="Defence", stamine="Stamine", magic="Magic", lucky="Lucky", experience="Experience"):
        self.item_name = item_name
        self.health = (health,random.randint(1,5))
        self.mana = (mana,random.randint(1,5))
        self.attack = (attack,random.randint(1,5))
        self.defence = (defence,random.randint(1,5))
        self.stamine = (stamine,random.randint(1,5))
        self.magic = (magic,random.randint(1,5))
        self.lucky = (lucky,random.randint(1,5))
        self.experience = (experience,random.randint(2,3))


    def attributes(self):
        attr = [
            self.health,
            self.mana,
            self.attack,
            self.defence,
            self.stamine,
            self.magic,
            self.lucky,
            self.experience,
        
        ]
        item_attributes = random.sample(attr, k=(random.randint(1,8)))
        return self.item_name, item_attributes

class Sword(DropEqItems):
    def __init__(self,item_name="Sword", attack= "Attack", defence = "Defence"):
        super().__init__(item_name)
        self.item_name = item_name
        self.attack = (attack,random.randint(5,20))
        self.defence = (defence,random.randint(10,25))

class Wand(DropEqItems):
    def __init__(self,item_name="Wand", magic= "Magic", defence = "Defence", mana = "Mana"):
        super().__init__(item_name)
        self.item_name = item_name
        self.magic = (magic,random.randint(5,20))
        self.defence = (defence,random.randint(10,25))
        self.mana = (mana,random.randint(25,50))

class Bow(DropEqItems):
    def __init__(self, item_name="Bow", attack = "Attack", speed_attack = "Speed Attack"):
        super().__init__(item_name)
        self.item_name = item_name
        self.attack = (attack,random.randint(25,30))
        self.speed_attack = (speed_attack,random.randint(2,3))

class Armor(DropEqItems):
    def __init__(self, item_name="Armor", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(10,40))
        self.health = (health,random.randint(10,100))
        self.mana = (mana,random.randint(10,100))
        self.stamine = (stamine,random.randint(10,20))

class Shorts(DropEqItems):
    def __init__(self, item_name="Shorts", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(10,40))
        self.health = (health,random.randint(10,50))
        self.mana = (mana,random.randint(10,50))
        self.stamine = (stamine,random.randint(10,20))

class Helmet(DropEqItems):
    def __init__(self, item_name="Helmet", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(40,80))
        self.health = (health,random.randint(10,25))
        self.mana = (mana,random.randint(10,25))
        self.stamine = (stamine,random.randint(10,20))


class Gloves(DropEqItems):
    def __init__(self, item_name="Gloves", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine", experience="Experience"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(40,80))
        self.health = (health,random.randint(10,25))
        self.mana = (mana,random.randint(10,25))
        self.stamine = (stamine,random.randint(10,20))
        self.experience = (experience,random.randint(3,5))

class Boots(DropEqItems):
    def __init__(self, item_name="Boots", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(40,80))
        self.health = (health,random.randint(10,25))
        self.mana = (mana,random.randint(10,25))
        self.stamine = (stamine,random.randint(80,120))

class Necklace(DropEqItems):
    def __init__(self, item_name="Necklace", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine", lucky="Lucky"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(5,10))
        self.health = (health,random.randint(5,10))
        self.mana = (mana,random.randint(5,10))
        self.stamine = (stamine,random.randint(5,10))
        self.lucky = (lucky,random.randint(5,10))

class Ring(DropEqItems):
    def __init__(self, item_name="Ring", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine", lucky="Lucky"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(5,10))
        self.health = (health,random.randint(5,10))
        self.mana = (mana,random.randint(5,10))
        self.stamine = (stamine,random.randint(5,10))
        self.lucky = (lucky,random.randint(5,10))

class Earrings(DropEqItems):
    def __init__(self, item_name="Earrings", defence = "Defence", health = "Health", mana = "Mana", stamine="Stamine", lucky="Lucky"):
        super().__init__(item_name)
        self.item_name = item_name
        self.defence = (defence,random.randint(5,10))
        self.health = (health,random.randint(5,10))
        self.mana = (mana,random.randint(5,10))
        self.stamine = (stamine,random.randint(5,10))
        self.lucky = (lucky,random.randint(5,10))

def item_draw():
    while True:
        item_list = [Sword(), Wand(), Bow(), Armor(), Shorts(), Gloves(),Helmet(), Boots(), Earrings(), Ring(), Necklace()]
        draw_item = random.choice(item_list)
        break
    return draw_item.attributes()


def inventory_add_item(inventory, item_name, item_attribute):
    add_to_inventory = input("Do you want add item to your inventory? ")
    while True:
        if add_to_inventory == "Y":
            inventory.append({item_name:list(item_attribute)})
            for item in player_backpack.inventory:
                print(item)
            print(f"ITEM HAS BEEN ADDED TO INVENTORY")
            break
        else:
            print({item_name:list(item_attribute)})
            item = {item_name:list(item_attribute)}
            del item
            break

def add_item(equipment, inventory, item_name, item_attribute):
    print(f'You found a {item_name}, with attributes as {item_attribute}')
    add_to_equipment = input("Do you want add item to your equipment? ")
    while True:
        if add_to_equipment == "Y":
            if item_name in equipment:
                inventory_add_item(inventory, item_name, item_attribute)
                break
            else:
                equipment[item_name] = item_attribute
                print(f"ITEM HAS BEEN ADDED TO EQUIPMENT")
                break
        else:
            print("ITEM HAS BEEN DELETED")
            break

def draw_items(equipment, inventory, item_name, item_attribute):
    drop = Enum("drop_or_nothing", ("DROP", "NOTHING"))
    drop_chance = {
        drop.DROP: 99,
        drop.NOTHING: 1,
    }
    drop_chance_key = list(drop_chance.keys())
    drop_chance_value = list(drop_chance.values())
    
    draw_chance_on_drop = random.choices(drop_chance_key,drop_chance_value)[0]
    search_monster_body = input("Do u want search monster body?[Y][Q] ")
    if search_monster_body == "Y":
        if draw_chance_on_drop == drop.DROP:
            add_item(equipment, inventory, item_name, item_attribute)

        else:
            print("The monster loot is nothing")

    else:
        print("Leaving...")






def drop_item():
    while True:
        item_n,item_attr= item_draw()
        draw_items(player_equipment.equipment,player_backpack.inventory,item_n, item_attr)
        break

