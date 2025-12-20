from time import sleep
import random

# ASCII Art
open_art = ''' ,  ,
             / \/ \,'| _
            ,'    '  ,' |,|
           ,'           ' |,'|
          ,'                 ;'| _
         ,'                    '' |

        ,'                        ;-,
       (___                        /
     ,'    `.  ___               ,'
    :       ,`'   `-.           /
    |-._ o /         \         /
   (    `-(           )       /
  ,'`.     \      o  /      ,'
 /    `     `.     ,'      /
(             `"""'       /
 `._                     /
    `--.______        '"`.
       \__,__,`---._   '`; 
            ))`-^--')`,-'
          ,',_____,'  |
          \_          `).
           `.      _,'  `
            /`-._,-'      '''
print(open_art)
sleep(2)

print('👋 Hello, bro! Welcome to the digital dungeon. I am your helper.')
sleep(1.5)
name = input('Please enter your name: ')
print(f'📝 Okay {name}, let\'s begin your adventure!')
sleep(2.5)

# Character selection
print("⚔️ Let's choose your base character")
sleep(1.5)
print("Choose wisely, you can't change later.")
sleep(2.5)

# Base stats
player_def = 0
player_attack = 0
player_hp = 0
player_speed = 0
player_stamina = 10  # max stamina

while True:
    try:
        choice = int(input('''1. 💨 Powerful atk, fast but low hp
2. 🛡️ Strong def but weak atk and slow
3. ❤️ More hp but weak atk : '''))
        if choice == 1:
            player_attack, player_def, player_hp, player_speed = 25, 15, 15, 20
            max_hp = 20  # special max HP for base character 1
        elif choice == 2:
            player_attack, player_def, player_hp, player_speed = 10, 25, 20, 10
            max_hp = player_hp  # max HP same as starting HP
        elif choice == 3:
            player_attack, player_def, player_hp, player_speed = 10, 20, 25, 15
            max_hp = player_hp  # max HP same as starting HP
        else:
            print('Please choose 1, 2, or 3.')
            sleep(1.5)
            continue
        break
    except Exception:
        print("⚠️ Please enter a valid number!")
        sleep(1.5)

print(f'Player stats: atk:{player_attack}, def:{player_def}, hp:{player_hp}, speed:{player_speed}, stamina:{player_stamina}')
sleep(2.5)

# Inventory system (start with potions)
player_inventory = ['sword', 'potion', 'stamina potion', 'attack potion']
item_effects = {
    "potion": {"hp": 20},
    "stamina potion": {"stamina": 5},
    "attack potion": {"attack": 5}
}
revive_tool = 1

print('🎒 Good. This is your inventory.')
print(f'Right now you have {player_inventory} in your inventory.')
sleep(2)
print('🩺 You received 1 revive tool in case you die.')
sleep(2)
print('🚪 The gate is open...')
sleep(2.5)
print('⚔️ Game start! A monster has appeared!')
sleep(2.5)

# First Monster (stronger)
monster1 = {
    "name": "corrupted_bright",
    "hp": 80,            # stronger HP
    "atk": 25,           # stronger attack
    "speed": 18,         # faster
    "loot": ['potion', 'stamina potion', 'attack potion']
}

print(f"👹 {monster1['name']}: Hmmm {name}, you chose to come in, now there is no escape!")
sleep(3)
print(f"{monster1['name']} stats - atk:{monster1['atk']}, hp:{monster1['hp']}, speed:{monster1['speed']}")
sleep(2.5)

# Battle loop
while monster1['hp'] > 0 and player_hp > 0:
    print("\nWhat will you do?")
    print(f'💪 Player stamina: {player_stamina}')
    print(f'🎒 Inventory: {player_inventory}')
    try:
        fight1 = int(input('1. ⚔️ Attack   2. 💨 Dodge   3. 🛡️ Defense   4. 🎒 Use Item: '))
    except Exception:
        print("⚠️ Enter a valid number!")
        continue

    if fight1 == 1:  # Attack
        player_damage = player_attack + random.randint(-2, 2)
        if random.random() < 0.15:
            player_damage *= 2
            print("💥 CRITICAL HIT! 💥")
            sleep(1.5)
        print(f"You attack {monster1['name']} for {player_damage} damage!")
        monster1['hp'] -= player_damage
        monster1['hp'] = max(monster1['hp'], 0)  # Prevent negative HP
        print(f"👹 {monster1['name']} HP: {monster1['hp']}")
        sleep(2)

        if monster1['hp'] > 0:
            monster_damage = max(0, monster1['atk'] - player_def + random.randint(-3,3))
            player_hp -= monster_damage
            player_hp = max(player_hp, 0)  # Prevent negative HP
            print(f"👹 {monster1['name']} attacks for {monster_damage}! Player HP: {player_hp}")
            sleep(2)
        else:
            print(f"🎉 {monster1['name']} has been defeated!")
            sleep(2.5)
            player_attack += 2
            print("💪 Your attack has increased by 2!")
            sleep(2)
            loot_item = random.choice(monster1['loot'])
            player_inventory.append(loot_item)
            print(f"🎁 {monster1['name']} dropped a {loot_item}! Added to your inventory.")
            sleep(2)
            print(f'Player stats: atk:{player_attack}, def:{player_def}, hp:{player_hp}, speed:{player_speed}, stamina:{player_stamina}')
            print(f'🎒 Current inventory: {player_inventory}')
            sleep(2.5)

    elif fight1 == 2:  # Dodge
        stamina_cost = 4
        if player_stamina >= stamina_cost:
            player_stamina -= stamina_cost
            if player_speed >= monster1['speed']:
                print("💨 You dodged successfully!")
                counter_damage = random.randint(2,6)
                monster1['hp'] -= counter_damage
                monster1['hp'] = max(monster1['hp'], 0)
                print(f"⚡ You hit back while dodging! {monster1['name']} takes {counter_damage} damage. HP now: {monster1['hp']}")
                if random.random() < 0.15:
                    counter_monster_damage = max(1, monster1['atk'] // 3)
                    player_hp -= counter_monster_damage
                    player_hp = max(player_hp, 0)
                    print(f"👹 {monster1['name']} lightly countered! You take {counter_monster_damage} damage. Player HP: {player_hp}")
                player_stamina = min(player_stamina + 1, 10)
                print(f"💪 You regain 1 stamina for successful dodge. Current stamina: {player_stamina}")
            else:
                print("⚠️ Dodge failed!")
                damage = max(0, monster1['atk'] - player_def)
                player_hp -= damage
                player_hp = max(player_hp, 0)
                print(f"You take {damage} damage. Player HP: {player_hp}")
        else:
            print("❌ Not enough stamina to dodge!")

    elif fight1 == 3:  # Defense
        damage = max(0, monster1['atk'] - player_def + random.randint(-3,3))
        player_hp -= damage
        player_hp = max(player_hp, 0)
        print(f"🛡️ You defended! {monster1['name']} deals {damage} damage. Player HP: {player_hp}")
        sleep(2)
        counter_damage = max(0, int(player_attack * 0.5) + random.randint(-1,1))
        monster1['hp'] -= counter_damage
        monster1['hp'] = max(monster1['hp'], 0)
        print(f"⚡ You counterattack and deal {counter_damage} damage back! {monster1['name']} HP: {monster1['hp']}")
        sleep(2)

    elif fight1 == 4:  # Use item
        usable_items = [item for item in player_inventory if item in item_effects]
        if not usable_items:
            print("🎒 No usable items in inventory!")
            sleep(2)
        else:
            print(f"🎒 Your items: {usable_items}")
            item_choice = input("Which item do you want to use? ").lower()
            if item_choice in usable_items:
                effect = item_effects[item_choice]
                if "hp" in effect:
                    player_hp = min(player_hp + effect["hp"], max_hp)
                    print(f"❤️ You used a potion! HP +{effect['hp']}. Current HP: {player_hp}")
                if "stamina" in effect:
                    player_stamina = min(player_stamina + effect["stamina"], 10)
                    print(f"⚡ You used a stamina potion! Stamina +{effect['stamina']}. Current stamina: {player_stamina}")
                if "attack" in effect:
                    player_attack += effect["attack"]
                    print(f"🔥 You used an attack potion! Attack +{effect['attack']}. Current Attack: {player_attack}")
                player_inventory.remove(item_choice)
                sleep(2)
            else:
                print("❌ Invalid item or not in inventory.")
                sleep(2)
    else:
        print("⚠️ Invalid choice, try again.")
        sleep(2)

    # Stamina regen
    player_stamina = min(player_stamina + 1, 10)

    # Revive
    if player_hp <= 0:
        if revive_tool > 0:
            revive_tool -= 1
            player_hp = 20
            print(f"🩺 You used a revive tool! HP restored to {player_hp}.")
            sleep(2.5)
        else:
            print("💀 You have died. Game Over.")
            break

if monster1['hp'] <= 0:
    print(f"🏆 You won the first battle against {monster1['name']}! The dungeon continues...")
    sleep(3)