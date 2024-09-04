def calculate_damage(attacker, defender):
    # Example damage calculation
    base_damage = attacker.troop_size * 0.1
    modifier = max(0, attacker.equipment_level - defender.equipment_level) * 0.05
    return int(base_damage + base_damage * modifier)
