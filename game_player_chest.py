player_items = ["Armor", "Boots"]
player_level = 2
buy_slot = 10


for item_number, item in enumerate(player_items):
    print(f"[{item_number}] {item}")


print(len(player_items))
player_chest = [[slot] for slot in range(0, 6 + player_level + buy_slot)]
while True:
    if len(player_items) > 0:
        choose_item = int(
            input("Please choose number item which you want hide in chest ")
        )
        if int(choose_item) < len(player_items):
            for chest_number, chest_place in enumerate(player_chest):
                print(chest_place)
            while True:
                enter_place = input(f"Choose slot on item")
                if int(enter_place) < len(player_chest):
                    if len(player_chest[int(enter_place)]) < 2:
                        player_chest[int(enter_place)].append(player_items[choose_item])
                        del player_items[choose_item]
                        print(player_items)
                        print(player_chest)
                        break
                    else:
                        print("This slot is taken, try choose other")
        else:
            break
    else:
        break