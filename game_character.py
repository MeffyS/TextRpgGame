class Character:
    def __init__(self, health=200, max_health=2500, mana=200, max_mana=2500, stamina=10, max_stamina=120, min_attack=50, max_attack=50, defence=1, magic=11, lucky=1, level=1, experience=97, points=20, skill_count=2):
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.defence = defence
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.magic = magic
        self.lucky = lucky
        self.level = level
        self.experience = experience
        self.points = points
        self.skill_count = skill_count

    def getHealth(self):
        return self.health

    def getMaxHealth(self):
        return self.max_health

    def getMana(self):
        return self.mana

    def getMaxMana(self):
        return self.max_mana

    def getStamina(self):
        return self.stamina

    def getMaxStamina(self):
        return self.max_stamina

    def getMinAttack(self):
        return self.min_attack

    def getMaxAttack(self):
        return self.max_attack

    def getDefence(self):
        return self.defence

    def getMagic(self):
        return self.magic

    def getLucky(self):
        return self.lucky

    def getLevel(self):
        return self.level

    def getExperience(self):
        return self.experience

    def getPoints(self):
        return self.points

    def setHealth(self, newHealth):
        self.health = newHealth

    def setMaxHealth(self, newMaxHealth):
        self.max_health = newMaxHealth

    def setMana(self, newMana):
        self.mana = newMana
    
    def setMaxMana(self, newMaxMana):
        self.mana = newMaxMana
    
    def setMaxStamina(self, newMaxStamina):
        self.stamina = newMaxStamina

    def setStamina(self, newStamina):
        self.stamina = newStamina

    def setMinAttack(self, newMinAttack):
        self.min_attack = newMinAttack

    def setMaxAttack(self, newMaxAttack):
        self.max_attack = newMaxAttack

    def setDefence(self, newDefence):
        self.defence = newDefence

    def setMagic(self, newMagic):
        self.magic = newMagic

    def setLucky(self, newLucky):
        self.lucky = newLucky

    def setPoziom(self, newLevel):
        self.level = newLevel

    def setExperience(self, newExperience):
        self.experience = newExperience

    def setPoints(self, newPoints):
        self.points = newPoints

class CharacterLevelUp:

    def level_up(self):
        if player.experience >= player.level * 100:
            player.experience = player.experience - (player.level * 100)
            player.max_attack = player.getMaxAttack() + (player.getLevel())
            player.health = player.getHealth() + (25*player.getLevel())
            player.max_health = player.getMaxHealth() + (25*player.getLevel())
            player.max_mana = player.getMana() + (25*player.getLevel())
            player.max_stamina = player.getStamina() + 10
            player.level = player.getLevel() + 1
            player.points = player.getPoints() + 5
            print(f'{48*"="}({player.level}){48*"="}'.center(100))
            print(f"You have advanced to level {player.level}".center(100))
            print(f'{99*"="}'.center(100))
            if 'Golden Coin' not in player_backpack.pocket:
                player_backpack.pocket['Golden Coin'] = 1
            else:
                player_backpack.pocket['Golden Coin'] += 1

class CharacterBackpack:

    coins = 0
    pocket = {'HealthPotion':1,'Golden Coin':120,'ManaPotion':20,'Diamond':20}
    chests = {}


class CharacterEquipment:
    
    equipment = {
    'Bow': [('Magic', 3), ('Mana', 3), ('Lucky', 4), ('Health', 3), ('Attack', 26)], 
    'Earrings': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
    'Helmet': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
    'Gloves': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
    'Chest': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
    'Boots': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
    }


class CharacterInventory:

    inventory = [{'Sword': [('Stamina', 2)]}, {'Helmet': [('Attack', 5)]}, {'Gloves': [('Attack', 30), ('Defence', 30), ('Health', 30), ('Mana', 30), ('Stamina', 30)]}]


class CharacterStatistic:

    def statistic(self):
        statistic_info = (f"Points[{player.points}] --> Health:[{player.max_health}], Mana:[{player.max_mana}], Stamina:[{player.max_stamina}], Defence:[{player.defence}], Attack:[{player.max_attack}], Magic:[{player.magic}], Lucky:[{player.lucky}]")
        return statistic_info

class CharacterInformation:

    def informations(self):
        character_info = (
            f"Character informations\n Health:[{player.health}],\n Mana:[{player.mana}]\n Stamina:[{player.stamina}] \
            \n Defence:[{player.defence}],\n Attack:[{player.max_attack}],\n Magic:[{player.magic}],\n Lucky:[{player.lucky}],\n  Experience:[{player.experience}]")
        return character_info



player = Character()
player_level_up = CharacterLevelUp()
player_backpack = CharacterBackpack()
player_statistic = CharacterStatistic()
player_equipment = CharacterEquipment()
player_inventory = CharacterInventory()
player_informations = CharacterInformation()



