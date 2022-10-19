class Potion:
    def __init__(self,item_name="item_name", price= 0 , health = 0, mana = 0, stamine = 0):
        self.item_name = item_name
        self.price = price 
        self.health = health
        self.mana = mana
        self.stamine = stamine
        
class HealthPotion(Potion):
    def __init__(self, item_name ='Health Potion', price=100, health = 50):
        super().__init__(health)
        self.item_name = item_name
        self.price = price
        self.health = health

class ManaPotion(Potion):
    def __init__(self, item_name ='Mana Potion', price=150, mana = 50):
        super().__init__(mana)
        self.item_name = item_name
        self.price = price
        self.mana = mana
        
class StaminePotion(Potion):
    def __init__(self, item_name ='Stamine Potion', price=200, stamine = 50):
        super().__init__(stamine)
        self.item_name =item_name
        self.price = price
        self.stamine = stamine  

SP = StaminePotion()           
MP = ManaPotion()           
HP = HealthPotion()           