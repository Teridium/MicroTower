class Entity:
    def __init__(self, size, weight, sharpness, mind):
        self.size = size
        self.weight = weight
        self.sharpness = sharpness
        self.mind = mind
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

    if entity1.weight == entity2.weight:
        # Simultaneous attacks
        while True:
            entity1.hp -= damage2_to_1
            entity2.hp -= damage1_to_2

            if entity1.hp <= 0 and entity2.hp <= 0:
                return "ничья, оба cдохли нафиг"
            elif entity1.hp <= 0:
                return "2 победил"
            elif entity2.hp <= 0:
                return "1 победил"
    else:
        # Non-simultaneous attacks
        if entity1.weight < entity2.weight:
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
            defender.hp -= attacker_damage
            if defender.hp <= 0:
                return f"{attacker_name} победил"

            attacker.hp -= defender_damage
            if attacker.hp <= 0:
                return f"{defender_name} победил"

# Define entities
# Енкель
entity1 = Entity(size=3, weight=1, sharpness=2, mind=1) # Вес 1 для инициативы
entity1.hp = 3 # Настоящее здоровье от Веса 3
# Зозерат
entity2 = Entity(size=3, weight=3, sharpness=3, mind=1)

# Simulate the battle
result = simulate_battle(entity1, entity2)
print(result)
