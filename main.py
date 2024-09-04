from models.agent import Agent
from utils.combat import calculate_damage

def main():
    agent_a = Agent(terrain_score=5, troop_size=1000, equipment_level=8, morale=7)
    agent_b = Agent(terrain_score=6, troop_size=800, equipment_level=7, morale=6)

    # Simulate combat
    damage_a = calculate_damage(agent_a, agent_b)
    damage_b = calculate_damage(agent_b, agent_a)

    print(f"Damage dealt by Agent A: {damage_a}, Damage dealt by Agent B: {damage_b}")

if __name__ == "__main__":
    main()
