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


def data_vaults_mission (hours,resilience):

    success_chance = 0.4

    is_destroyed = roll_mission_destruction(resilience)

    if is_destroyed:

        return False
    
    mission_status = mission_outcome(success_chance)

    energy_cost_hour = 2

    if mission_status: ##mission successful

        xp_hour = 40
        bits_hour = 50
        junk_hour = random.randint(2,4)

        if (hours == 2):
            
            silicon_reward = random.randint(1,2)

            xp_earned = xp_hour*hours
            bits_earned = bits_hour*hours
            junk_earned = junk_hour*hours
            energy_cost = energy_cost_hour*hours

            return silicon_reward, xp_earned, junk_earned, energy_cost
        
        if (hours == 4):
            
            silicon_reward = random.randint(2,3)

            xp_earned = xp_hour*hours
            bits_earned = bits_hour*hours
            junk_earned = junk_hour*hours
            energy_cost = energy_cost_hour*hours

            return silicon_reward, xp_earned, junk_earned, energy_cost

        if (hours == 8):
            
            silicon_reward = random.randint(4,6)

            xp_earned = xp_hour*hours
            bits_earned = bits_hour*hours
            junk_earned = junk_hour*hours
            energy_cost = energy_cost_hour*hours

            return silicon_reward, xp_earned, junk_earned, energy_cost
        
    else:

        xp_hour = 12
        bits_hour = 15
        junk_hour = 0

        if (hours == 2):
            
            silicon_reward = 0

            xp_earned = xp_hour*hours
            bits_earned = bits_hour*hours
            junk_earned = junk_hour*hours
            energy_cost = energy_cost_hour*hours

            return silicon_reward, xp_earned, junk_earned, energy_cost
        
        if (hours == 4):
            
            silicon_reward = 0

            xp_earned = xp_hour*hours
            bits_earned = bits_hour*hours
            junk_earned = junk_hour*hours
            energy_cost = energy_cost_hour*hours

            return silicon_reward, xp_earned, junk_earned, energy_cost

        if (hours == 8):
            
            silicon_reward = 0

            xp_earned = xp_hour*hours
            bits_earned = bits_hour*hours
            junk_earned = junk_hour*hours
            energy_cost = energy_cost_hour*hours

            return silicon_reward, xp_earned, junk_earned, energy_cost



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

def main():

    generate_bot()


if __name__ == '__main__':

    main()