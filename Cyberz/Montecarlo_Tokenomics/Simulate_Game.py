import numpy as np
import random

def roll_initial_bot_stats ():

    while True:
        size = random.randint(1, 15)
        haste = random.randint(1, min(15, 20 - size))
        crit = 21 - size - haste

        if (size<=15 and haste <= 15 and crit <= 15):
            
            return size, haste, crit

def roll_initial_bot_energy_res():

    energy_values = [100, 105, 110, 115, 120]
    odds = [0.55, 0.25, 0.10, 0.07, 0.03]
    
    energy = np.random.choice(energy_values, p=odds)

    resilience = random.randint(400, 600)

    return energy, resilience

def roll_mission_destruction (resilience):

    destruction_number = random.randint(1,100000)

    return True if destruction_number<resilience else False

def mission_outcome(success_ratio):

    random_chance = random.random()
    
    return True if random_chance < success_ratio else False


def data_vaults_mission(hours, resilience):
    
    # Check Bot Destruction
    if roll_mission_destruction(resilience):
        return False

    mission_rewards = {
        2: {'silicon_range': (1, 2), 'xp_hour': 40, 'bits_hour': 50, 'junk_hour': (2, 4)},
        4: {'silicon_range': (2, 3), 'xp_hour': 40, 'bits_hour': 50, 'junk_hour': (2, 4)},
        8: {'silicon_range': (4, 6), 'xp_hour': 40, 'bits_hour': 50, 'junk_hour': (2, 4)},
    }

    failure_rewards = {
        'xp_hour': 12,
        'bits_hour': 15,
        'junk_hour': 0,
        'silicon_reward': 0,
    }

    mission_status = mission_outcome(0.4)  # Sucess Chance

    energy_cost_hour = 4

    if mission_status and hours in mission_rewards:  # Rewards for success mission
        rewards = mission_rewards[hours]
        silicon_reward = random.randint(*rewards['silicon_range'])

    else:  # rewards for failed mission
        rewards = failure_rewards
        silicon_reward = rewards['silicon_reward']

    xp_earned = rewards['xp_hour'] * hours
    bits_earned = rewards['bits_hour'] * hours
    junk_earned = random.randint(*rewards.get('junk_hour', (0, 0))) * hours if 'junk_hour' in rewards else 0
    energy_cost = energy_cost_hour * hours

    return silicon_reward, xp_earned, bits_earned, energy_cost, junk_earned

def refinery_mission(hours, resilience):
    
    # Check Bot Destruction
    if roll_mission_destruction(resilience):
        return False

    mission_rewards = {
        2: {'metal_range': (2, 3), 'xp_hour': 40, 'bits_hour': 40, 'junk_hour': (2, 4)},
        4: {'metal_range': (3, 4), 'xp_hour': 40, 'bits_hour': 40, 'junk_hour': (2, 4)},
        8: {'metal_range': (5, 8), 'xp_hour': 40, 'bits_hour': 40, 'junk_hour': (2, 4)},
    }

    failure_rewards = {
        'xp_hour': 12,
        'bits_hour': 12,
        'junk_hour': 0,
        'metal_range': 0,
    }

    mission_status = mission_outcome(0.5)  # Sucess Chance

    energy_cost_hour = 3

    if mission_status and hours in mission_rewards:  # Rewards for success mission
        rewards = mission_rewards[hours]
        metal_reward = random.randint(*rewards['metal_range'])

    else:  # rewards for failed mission
        rewards = failure_rewards
        metal_reward = rewards['metal_range']

    xp_earned = rewards['xp_hour'] * hours
    bits_earned = rewards['bits_hour'] * hours
    junk_earned = random.randint(*rewards.get('junk_hour', (0, 0))) * hours if 'junk_hour' in rewards else 0
    energy_cost = energy_cost_hour * hours

    return metal_reward, xp_earned, bits_earned, energy_cost, junk_earned


def plastic_mission(hours, resilience):
    
    # Check Bot Destruction
    if roll_mission_destruction(resilience):
        return False

    mission_rewards = {
        2: {'plastic_range': (4, 5), 'xp_hour': 40, 'bits_hour': 30, 'junk_hour': (2, 4)},
        4: {'plastic_range': (5, 8), 'xp_hour': 40, 'bits_hour': 30, 'junk_hour': (2, 4)},
        8: {'plastic_range': (6, 16), 'xp_hour': 40, 'bits_hour': 30, 'junk_hour': (2, 4)},
    }

    failure_rewards = {
        'xp_hour': 12,
        'bits_hour': 9,
        'junk_hour': 0,
        'plastic_range': 0,
    }

    mission_status = mission_outcome(0.4)  # Sucess Chance

    energy_cost_hour = 2

    if mission_status and hours in mission_rewards:  # Rewards for success mission
        rewards = mission_rewards[hours]
        plastic_reward = random.randint(*rewards['plastic_range'])

    else:  # rewards for failed mission
        rewards = failure_rewards
        plastic_reward = rewards['plastic_range']

    xp_earned = rewards['xp_hour'] * hours
    bits_earned = rewards['bits_hour'] * hours
    junk_earned = random.randint(*rewards.get('junk_hour', (0, 0))) * hours if 'junk_hour' in rewards else 0
    energy_cost = energy_cost_hour * hours

    return plastic_reward, xp_earned, bits_earned, energy_cost, junk_earned


def generate_bot ():

    ##rolling initial stats
    health = 100
    size, haste, crit = roll_initial_bot_stats ()

    starting_energy, resilience = roll_initial_bot_energy_res()

    resource_yield_increase = 0.01*size
    energy = starting_energy + size
    mission_success_boost = 0.005*haste
    mission_crit_chance = 0.005*crit
    print ("Initial Bot Stats")
    print(f"{'Size':<10}{'Haste':<10}{'Crit':<10}{'Energy':<10}{'Resilience':<12}")
    print(f"{size:<10}{haste:<10}{crit:<10}{energy :<10}{resilience:<12}")
    print(f"{'Yield Inc.':<10}{'Success Boost':<14}{'Crit Chance':<12}")
    print(f"{resource_yield_increase:<10.2f}{mission_success_boost:<14.3f}{mission_crit_chance:<12.3f}")


def mission_rewards ():

    return 1


def main():

    generate_bot()


if __name__ == '__main__':

    main()