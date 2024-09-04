class Agent:
    def __init__(self, terrain_score, troop_size, equipment_level, morale):
        self.terrain_score = terrain_score
        self.troop_size = troop_size
        self.equipment_level = equipment_level
        self.morale = morale
        self.casualties = 0

    def engage(self, enemy):
        # Combat logic here
        if self.equipment_level > enemy.equipment_level:
            enemy.casualties += self.troop_size * 0.1  # Example damage calculation
        else:
            self.casualties += enemy.troop_size * 0.05  # Example damage received
        pass
