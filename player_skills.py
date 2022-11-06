
# import random

# from game_character import player
# import well_monster
# from game_decorators import skill_name
# from game_decorators import thunder_attack_generator
# from game_clear_function import clearConsole
# from game_drop_system import draw_items


# class PlayerSkill():
#     def __init__(self, mana=0, min_attack=0, max_attack=0):
#         self.mana = mana
#         self.min_attack = min_attack
#         self.max_attack = max_attack


# class FireBallSkill(PlayerSkill):

#     def __init__(self, mana=0, min_attack=0, max_attack=0):
#         super().__init__(mana, min_attack, max_attack)
#         self.mana = 50
#         self.min_attack = random.randint(
#             player.min_attack, player.min_attack*2)
#         self.max_attack = random.randint(
#             player.min_attack, player.min_attack*3)

#     @skill_name
#     def fire_Ball(self,mob_health,mob_attack_min,mob_attack_max,mob_defence):
#         attack = [self.min_attack, self.max_attack]
#         if player.mana >= self.mana:
#             if mob_health > 0:
#                 hit = random.choice(attack)
#                 mob_health -= hit
#                 player.mana -= self.mana
#                 clearConsole()
#                 print(f'{100*"="}')
#                 print(
#                     f"The {self.__class__.__name__} took the monster {hit} health points. LEFT: {mob_health} Health Points. Left mana:{player.mana}/{player.max_mana} ".center(100))
#             else:
#                 print('Monster is dead')
#         else:
#             print(
#                 f"You cannot use this skill becouse your mana is to low. [{player.mana}/{self.mana}]")


# class GreatFireBallSkill(FireBallSkill):
#     def __init__(self, mana=0, min_attack=0, max_attack=0, burning=0):
#         super().__init__(mana, min_attack, max_attack)
#         self.burning = random.randint(0, 100)
#         self.mana = 80
#         self.min_attack = random.randint(
#             player.min_attack, player.min_attack*3)
#         self.max_attack = random.randint(
#             player.min_attack, player.min_attack*4)

#     @skill_name
#     def great_Fire_Ball(self):
#         if player.mana >= self.mana:
#             GreatFireBallSkill.fire_Ball(self)
#             if self.burning <= 79:
#                 pass
#             elif self.burning >= 80:
#                 self.burning = 100
#                 well_monster.Monster.health -= 1
#                 print(
#                     f"Burning took the monster 1 health points. LEFT: {well_monster.Monster.health} Health Points ")
#                 print(f'{100*"="}')
#         elif player.mana < self.mana:
#             print(
#                 f"You cannot use this skill becouse your mana is to low. {player.mana}/{self.mana}")

# class ThunderSkill(PlayerSkill):
#     def __init__(self, mana=0, min_attack=0, max_attack=0):
#         super().__init__(mana, min_attack, max_attack)
#         self.mana = 200

#     @staticmethod
#     @thunder_attack_generator
#     def test_thunder():
#         pass

#     @skill_name
#     def thunder(self):
#         if player.mana >= self.mana:
#             a = self.test_thunder()
#             well_monster.Monster.health -= a[1]
#             player.mana -= self.mana
#         else:
#             print(
#                 f"You cannot use this skill becouse your mana is to low. {player.mana}/{self.mana}")


# class HealthRegenerationSkill(PlayerSkill):
#     def __init__(self, mana=0, health=0):
#         super().__init__(mana)
#         self.mana = 20
#         self.health = 45

#     @skill_name
#     def health_Regeneration(self):
#         if player.health > player.max_health:
#             player.health = player.max_health
#         elif player.health < player.max_health:
#             if player.mana >= self.mana:
#                 player.health += self.health
#                 player.mana -= self.mana
#                 clearConsole()
#                 print(
#                     f"Your character has been healed {self.health} health points. You got {player.health}/{player.max_health}")
#                 print(
#                     f"Your character has been losed {self.mana} mana points. {player.mana}/{self.mana} ")
#                 if player.health >= player.max_health:
#                     clearConsole()
#                     player.health = player.max_health
#                     print(
#                         f"Your character has been healed {self.health} health points. You got {player.health}/{player.max_health}")
#             elif player.mana < self.mana:
#                 print(
#                     f"You cannot use this skill becouse your mana is to low. {player.mana}/{self.mana}")

#         elif player.health == player.max_health:
#             print(f'Your health is full')


# class GreatHealthRegenerationSkill(HealthRegenerationSkill):
#     def __init__(self, mana=0, health=0):
#         super().__init__(mana, health)
#         self.mana = 40
#         self.health = 90


# class UltraHealthRegenSkill(HealthRegenerationSkill):
#     def __init__(self, mana=0, health=0):
#         super().__init__(mana, health)
#         self.mana = 80
#         self.health = 200


# class AddAttackSkill(PlayerSkill):
#     def __init__(self, mana=0, min_attack=0, max_attack=0, count = 10):
#         super().__init__(mana, min_attack, max_attack)
#         self.mana = 150
#         self.count = count 


#     @skill_name
#     def add_Attack(self):
#         if player.skill_count >= 0:
#             if player.mana >= self.mana:
#                 print(f"Your attack has been increased {player.min_attack} -> {player.min_attack+10}. Amount to use {player.skill_count}/3".center(100))
#                 print(f'{100*"="}')
#                 player.skill_count -= 1

#                 player.min_attack += 10
#                 monster_hit = random.randint(
#                     well_monster.Monster.attack_min, well_monster.Monster.attack_max) / player.defence
#                 player.health -= monster_hit
#                 print(
#                     f'The monster hit you for {int(monster_hit)}. Your actually health: {int(player.health)}/{player.max_health}'.center(100))
#                 print(f'{100*"="}')    
#             else:
#                 print(f'{100*"="}')
#                 print(f"You cannot use this skill becouse your mana is to low. [{player.mana}/{self.mana}]".center(100))
#                 print(f'{100*"="}')
#         else:
#             print(f"You cannot use this skill more that three times per round".center(100))
#             print(f'{100*"="}')


# def used_skill(self, mob_health,mob_attack_min,mob_attack_max,mob_defence):
#     while True:
#         if self.health >= 0:
#             custom_skills = [
#                 cls.__name__ for cls in PlayerSkill.__subclasses__()]
#             fireball_skills_option = [
#                 cls.__name__ for cls in FireBallSkill.__subclasses__()]
#             health_skills_option = [
#                 cls.__name__ + '[DISABLED]' for cls in HealthRegenerationSkill.__subclasses__()]
#             custom_skills.extend(fireball_skills_option)
#             custom_skills.extend(health_skills_option)

            
#             print(f"{100 * '='}")
#             print(f"CHOOSE SKILL".center(100))
#             print(f"{100 * '='}")
#             for num, skill in enumerate(custom_skills):
#                 print(f'{num} {skill}'.center(100))
#             print(f"{100 * '='}")
#             print(f"What you want to do?".center(100))
#             what_do = input(f"".center(50)).upper()
#             clearConsole()
#             try:
#                 if what_do == 'FB' or what_do == 'FIREBALL' or what_do == '0':
#                     fb = FireBallSkill()
#                     fb.fire_Ball(mob_health,mob_attack_min,mob_attack_max,mob_defence)
#                     monster_hit = round(random.randint(
#                         mob_attack_min, mob_attack_max)) / player.defence
#                     player.health -= monster_hit
#                     print(f"{100 * '='}")
#                     print(f'The monster attack took YOU {monster_hit} health points. LEFT {player.health} monster Health Points'.center(100))
#                     print(f"{100 * '='}")
#                     if mob_health <= 0:
                        
#                         break
#                     break
#                 elif what_do == "T" or what_do == 'THUNDERSKILL' or what_do == '2':
#                     ts = ThunderSkill()
#                     ts.thunder()
#                     monster_hit = random.randint(
#                         well_monster.Monster.attack_min, well_monster.Monster.attack_max) / player.defence
#                     player.health -= monster_hit
#                     print(
#                         f'The monster attack took YOU {monster_hit} health points. LEFT {player.health} monster Health Points'.center(100))
#                     print(f"{100 * '='}")
#                     if well_monster.Monster.health <= 0:
#                         break
#                     break
#                 elif what_do == "HR" or what_do == 'HEALTHREGENERATION' or what_do == '3':
#                     hp = HealthRegenerationSkill()
#                     hp.health_Regeneration()
#                     monster_hit = random.randint(
#                         well_monster.Monster.attack_min, well_monster.Monster.attack_max) / player.defence
#                     player.health -= monster_hit
#                     print(f'The monster attack took YOU {monster_hit} health points. LEFT {player.health} monster Health Points'.center(100))
#                     print(f'{100*"="}')
#                     break

#                 elif what_do == "AA" or what_do == 'ADDATTACK' or what_do == '4':
#                     aa = AddAttackSkill()
#                     aa.add_Attack()
#                     monster_hit = random.randint(
#                         well_monster.Monster.attack_min, well_monster.Monster.attack_max) / player.defence
#                     player.health -= monster_hit
#                     print(
#                         f'The monster attack took YOU {monster_hit} health points. LEFT {player.health} monster Health Points'.center(100))
#                     print(f"{100 * '='}")
#                     break

#                 elif what_do == "GF" or what_do == 'GREATFIREBALL' or what_do == '5':
#                     gf = GreatFireBallSkill()
#                     gf.great_Fire_Ball()
#                     monster_hit = random.randint(
#                         well_monster.Monster.attack_min, well_monster.Monster.attack_max) / player.defence
#                     player.health -= monster_hit
#                     print(
#                         f'The monster attack took YOU {monster_hit} health points. LEFT {player.health} monster Health Points'.center(100))
#                     print(f"{100 * '='}")
#                     if well_monster.Monster.health <= 0:
#                         break
#                     break
#                 elif what_do == "GH" or what_do == 'GREATHEAL' or what_do == '6':
#                     print("THIS SKILL IS DISABLED")
#                     break
#                 elif what_do == "UH" or what_do == 'ULTRAHEAL' or what_do == '7':
#                     print("THIS SKILL IS DISABLED")
#                     break
#                 elif what_do == "Q" or what_do == 'QUIT' or what_do == '8':
#                     del aa
#                     player.min_attack = player.max_attack
#                     break

#             except UnboundLocalError:
#                 break
#         else:
#             print("Monster is dead")
#             draw_items()
#             AddAttackSkill.count = 0
#             break
