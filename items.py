class Potion:
    def __init__(self,item_name="item_name", price= 0 , health = 0, mana = 0, stamine = 0):
        self.item_name = item_name
        self.price = price 
        self.health = health
        self.mana = mana
        self.stamine = stamine

class SmallManaPotion(Potion):
    def __init__(self, item_name ='Small Mana Potion', price=50, mana = 25):
        super().__init__(mana)
        self.item_name = item_name
        self.price = price
        self.mana = mana

class SmallHealthPotion(Potion):
    def __init__(self, item_name ='Small Health Potion', price=50, health = 25):
        super().__init__(health)
        self.item_name = item_name
        self.price = price
        self.health = health

class SmallStaminaPotion(Potion):
    def __init__(self, item_name ='Small Stamine Potion', price=50, stamine = 25):
        super().__init__(stamine)
        self.item_name = item_name
        self.price = price
        self.stamine = stamine
        
class ManaPotion(Potion):
    def __init__(self, item_name ='Mana Potion', price=100, mana = 60):
        super().__init__(mana)
        self.item_name = item_name
        self.price = price
        self.mana = mana

class HealthPotion(Potion):
    def __init__(self, item_name ='Health Potion', price=100, health = 60):
        super().__init__(health)
        self.item_name = item_name
        self.price = price
        self.health = health
        
class StaminePotion(Potion):
    def __init__(self, item_name ='Stamine Potion', price=100, stamine = 60):
        super().__init__(stamine)
        self.item_name =item_name
        self.price = price
        self.stamine = stamine  

class GreatManaPotion(Potion):
    def __init__(self, item_name ='Great Mana Potion', price=250, mana = 350):
        super().__init__(mana)
        self.item_name = item_name
        self.price = price
        self.mana = mana

class GreatHealthPotion(Potion):
    def __init__(self, item_name ='Great Health Potion', price=250, health = 350):
        super().__init__(health)
        self.item_name = item_name
        self.price = price
        self.health = health
        
class GreatStaminePotion(Potion):
    def __init__(self, item_name ='Great Stamine Potion', price=250, stamine = 350):
        super().__init__(stamine)
        self.item_name =item_name
        self.price = price
        self.stamine = stamine  


SMP = SmallManaPotion()
SHP = SmallHealthPotion()
SSP = SmallStaminaPotion()

         
MP = ManaPotion()           
HP = HealthPotion()
SP = StaminePotion()  

GMP = GreatManaPotion()
GHP = GreatHealthPotion()
GSP = GreatStaminePotion()