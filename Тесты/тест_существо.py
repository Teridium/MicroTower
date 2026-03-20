from creatures import creatures_data

def calculate_damage(attacker, defender):
    delta_size = max(0, defender['size'] - attacker['size'])
    delta_mind = max(0, attacker['mind'] - defender['mind'])
    damage = attacker['sharpness'] - delta_size + delta_mind
    return max(0, damage)

def simulate_battle(main, opponent):
    damage_mto = calculate_damage(main, opponent)
    damage_otm = calculate_damage(opponent, main)
    main_hp = main['hp']
    opponent_hp = opponent['hp']

    if damage_mto == 0 and damage_otm == 0:
        return 'draw', opponent['name']
    
    if damage_mto == 0 and damage_otm > 0:
        return 'defeat', opponent['name']
    
    if damage_mto > 0 and damage_otm == 0:
        return 'win', opponent['name']

    if main['initiative'] == opponent['initiative']:
        # Simultaneous attacks
        while True:
            main_hp -= damage_otm
            opponent_hp -= damage_mto

            if main_hp <= 0 and opponent_hp <= 0:
                return 'draw', opponent['name']
            elif main_hp <= 0:
                return 'defeat', opponent['name']
            elif opponent_hp <= 0:
                return 'win', opponent['name']
    else:
        # Non-simultaneous attacks
        if main['initiative'] < opponent['initiative']:
            # main attacks first
            while True:
                opponent_hp -= damage_mto
                if opponent_hp <= 0:
                    return 'win', opponent['name']
                main_hp -= damage_otm
                if main_hp <= 0:
                    return 'defeat', opponent['name']
        else:
            # opponent attacks first
            while True:
                main_hp -= damage_otm
                if main_hp <= 0:
                    return 'defeat' , opponent['name']
                opponent_hp -= damage_mto
                if opponent_hp <= 0:
                    return 'win', opponent['name']

# Define entities
# Павильо
testing_creature = creatures_data[60]

wins = 0
draws = 0
defeats = 0
wins_against = []
loses_against = []
draws_against = []

# Simulate the battle
for opponent in creatures_data:
    result = simulate_battle(testing_creature, opponent)
    if result[0] == 'draw':
        draws += 1
        draws_against += [result[1]]
    elif result[0] == 'win':
        wins += 1
        wins_against += [result[1]]
    elif result[0] == 'defeat':
        defeats += 1
        loses_against += [result[1]]

print(f'Результаты {testing_creature['name']}:')
print(f'Победы: {wins} против {wins_against}')
print(f'Ничьи: {draws} против {draws_against}')
print(f'Поражения: {defeats} против {loses_against}')
