class Entity:
    def __init__(self, size, weight, sharpness, mind, initiative=None, hp=None):
        self.sharpness = sharpness
        self.size = size
        self.mind = mind
        if initiative:
            self.initiative = initiative
        else:
            self.initiative = weight
        if hp:
            self.hp = hp
        else:
            if weight == 0:
                self.hp = 1
            else:
                self.hp = weight

def calculate_damage(attacker, defender):
    delta_size = max(0, defender.size - attacker.size)
    delta_mind = max(0, attacker.mind - defender.mind)
    damage = attacker.sharpness - delta_size + delta_mind
    return max(0, damage)

def simulate_battle(entity1, entity2):
    damage1_to_2 = calculate_damage(entity1, entity2)
    damage2_to_1 = calculate_damage(entity2, entity1)

    if damage1_to_2 == 0 and damage2_to_1 == 0:
        return "ничья, урон - нули"

    round_num = 1
    if entity1.initiative == entity2.initiative:
        # Simultaneous attacks
        while True:
            entity1.hp -= damage2_to_1
            entity2.hp -= damage1_to_2
            print(f"Раунд {round_num}:")
            print("1 здоровье =", f'{entity1.hp};', '2 здоровье =', entity2.hp )

            if entity1.hp <= 0 and entity2.hp <= 0:
                return "ничья, оба cдохли нафиг"
            elif entity1.hp <= 0:
                return "2 победил"
            elif entity2.hp <= 0:
                return "1 победил"
            round_num += 1
    else:
        # Non-simultaneous attacks
        if entity1.initiative < entity2.initiative:
            # Entity 1 attacks first
            attacker = entity1
            defender = entity2
            attacker_damage = damage1_to_2
            defender_damage = damage2_to_1
            attacker_name = "1"
            defender_name = "2"
        else:
            # Entity 2 attacks first
            attacker = entity2
            defender = entity1
            attacker_damage = damage2_to_1
            defender_damage = damage1_to_2
            attacker_name = "2"
            defender_name = "1"

        while True:
            print(f"Раунд {round_num}:")
            defender.hp -= attacker_damage
            print(f"{defender_name} здоровье =", defender.hp)
            if defender.hp <= 0:
                return f"{attacker_name} победил"

            attacker.hp -= defender_damage
            print(f"{attacker_name} здоровье =", attacker.hp)
            if attacker.hp <= 0:
                return f"{defender_name} победил"
            round_num += 1

# Define entities
# 
entity1 = Entity(size=1, weight=2, sharpness=5, mind=1)
# 
entity2 = Entity(size=4, weight=3, sharpness=1, mind=0)

# Simulate the battle
result = simulate_battle(entity1, entity2)
print("Результат:")
print(result)
