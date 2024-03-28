import numpy as np
import random
import pandas as pd
import sys
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

def generate_bot (bot_name):

    ##rolling initial stats
    health = 100
    level = 1
    rarity = 'common'
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

    return {'name': bot_name, 'rarity': rarity, 'level': level, 'health':health, 'size':size, 'crit':crit, 'haste':haste ,'resilience':resilience,
            'resource_yield_increase':resource_yield_increase, 'mission_success_boost':mission_success_boost, 'mission_crit_chance':mission_crit_chance, 'starting_energy':starting_energy, 'current_energy':starting_energy}
    #return rarity, level, health, size, haste, crit, resilience, energy, resource_yield_increase, mission_success_boost, mission_crit_chance, starting_energy


def roll_mission_destruction (resilience):

    destruction_number = random.randint(1,100000)

    return True if destruction_number<resilience else False

def mission_outcome(success_ratio):

    random_chance = random.random()
    
    return True if random_chance < success_ratio else False


def data_vaults_mission(hours, resilience,mission_success_boost):
    
    sucess_rate = 0.4 + mission_success_boost

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
        'junk_hour': (0,0),
        'silicon_reward': 0,
    }

    mission_status = mission_outcome(sucess_rate)  # Sucess Chance

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

    return mission_status, silicon_reward, xp_earned, bits_earned, energy_cost, junk_earned

def refinery_mission(hours, resilience,mission_success_boost):
    
    sucess_rate = 0.5 + mission_success_boost

    # Check Bot Destruction
    if roll_mission_destruction(resilience):
        print ('ded')
        return False

    mission_rewards = {
        2: {'metal_range': (2, 3), 'xp_hour': 40, 'bits_hour': 40, 'junk_hour': (2, 4)},
        4: {'metal_range': (3, 4), 'xp_hour': 40, 'bits_hour': 40, 'junk_hour': (2, 4)},
        8: {'metal_range': (5, 8), 'xp_hour': 40, 'bits_hour': 40, 'junk_hour': (2, 4)},
    }

    failure_rewards = {
        'xp_hour': 12,
        'bits_hour': 12,
        'junk_hour': (0,0),
        'metal_range': 0,
    }

    mission_status = mission_outcome(sucess_rate)  # Sucess Chance

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

    return mission_status, metal_reward, xp_earned, bits_earned, energy_cost, junk_earned


def plastic_mission(hours, resilience,mission_success_boost):
    
    # Check Bot Destruction
    if roll_mission_destruction(resilience):
        return False

    sucess_rate = 0.6+mission_success_boost
    mission_rewards = {
        2: {'plastic_range': (4, 5), 'xp_hour': 40, 'bits_hour': 30, 'junk_hour': (2, 4)},
        4: {'plastic_range': (5, 8), 'xp_hour': 40, 'bits_hour': 30, 'junk_hour': (2, 4)},
        8: {'plastic_range': (6, 16), 'xp_hour': 40, 'bits_hour': 30, 'junk_hour': (2, 4)},
    }

    failure_rewards = {
        'xp_hour': 12,
        'bits_hour': 9,
        'junk_hour': (0,0),
        'plastic_range': 0,
    }

    mission_status = mission_outcome(sucess_rate)  # Sucess/Failure Mission

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

    return mission_status, plastic_reward, xp_earned, bits_earned, energy_cost, junk_earned


def run_mission(bot, mission_time):
    
    resilience = bot['resilience']
    resource_yield_increase = bot['resource_yield_increase']
    mission_success_boost = bot['mission_success_boost']
    mission_crit_chance = bot['mission_crit_chance']
    bot_name = bot['name']
    ##mission types
    missions = [data_vaults_mission, refinery_mission, plastic_mission]

    # mission selection
    selected_mission = random.choice(missions)
    selected_mission_name = selected_mission.__name__
    # list resource name
    resource_names = {
        data_vaults_mission: 'Silicon',
        refinery_mission: 'Metal',
        plastic_mission: 'Plastic'
    }
    resource_name = resource_names[selected_mission]

    # run executed mission
    mission_status, resource_reward, xp_earned, bits_earned, energy_cost, junk_earned = selected_mission(mission_time, resilience, mission_success_boost)
     

    # Final resource rewards
    total_bits, total_material, crit_mission = mission_final_rewards(bits_earned, resource_reward, resource_yield_increase, mission_crit_chance)
    
    
    # print rewards
    print(f"Misión seleccionada: {resource_name}")
    print(f"Estado de la misión: {'Éxito' if mission_status else 'Fallo'}")
    print(f"Recompensa de {resource_name}: {total_material}")
    print(f"XP ganada: {xp_earned}, Bits totales: {total_bits}, Costo de energía: {energy_cost}, Basura obtenida: {junk_earned}, Misión crítica: {crit_mission}")

    return bot_name, selected_mission_name, resource_name, mission_time, mission_status, total_material, xp_earned, total_bits, energy_cost, junk_earned, crit_mission


def mission_final_rewards (bits_earned, material_reward,resource_yield_increase,mission_crit_chance):

    total_bits = round(bits_earned * (1+resource_yield_increase),1)
    
    random_chance_mission = random.random()

    crit_mission = 2 if random_chance_mission < mission_crit_chance else 1

    total_material = material_reward * crit_mission

    return total_bits, total_material, crit_mission

def recharge_energy(current_energy, max_energy):

    energy_needed = max_energy - current_energy

    time_needed = (energy_needed / 20) * 0.5  
    
    
    new_energy = current_energy + (time_needed * 40) 

    if new_energy > max_energy:
        new_energy = max_energy
    
    return new_energy, time_needed


def assign_skill_points(size, haste, crit):
    # random assignment of 2 skill points to size, haste, or crit

    for _ in range(2): 
        increase = random.choice(["size", "haste", "crit"])
        if increase == "size":
            size += 1
        elif increase == "haste":
            haste += 1
        else:
            crit += 1
    return size, haste, crit

def check_level_up(total_xp, total_bits, level, size, haste, crit):

    level_requirements = [
        {"level": 1, "xp_cost": 0, "bit_cost": 0},  # Initial Level
        {"level": 2, "xp_cost": 700, "bit_cost": 450},
        {"level": 3, "xp_cost": 800, "bit_cost": 500},
        {"level": 4, "xp_cost": 900, "bit_cost": 550},
        {"level": 5, "xp_cost": 1000, "bit_cost": 600},
    ]
    
    if level < len(level_requirements):
        next_level_req = level_requirements[level]  # Check requirements for next level

        if total_xp >= next_level_req["xp_cost"] and total_bits >= next_level_req["bit_cost"]:
            
            ## we assign the 2 skill points randomly
            size, haste, crit = assign_skill_points(size, haste, crit)
            
            return True, level + 1, size, haste, crit ##the true/false is needed as we'll need to upgrade the size/haste/crit variables
            
        else:

            return False, level, size, haste, crit
    else:

        return False, level, size, haste, crit  

def check_and_upgrade_rarity(level, rarity, total_junk, total_silicon, total_metal, total_plastic):
    rarity_levels = [5, 10, 15]  
    rarity_upgrade_requirements = {
        'common': {'junk_cost': 150, 'silicon_cost': 80, 'metal_cost': 40, 'plastic_cost': 120},
        # add uncommon, rare costs
    }
    next_rarity = {
        'common': 'uncommon',
        'uncommon': 'rare',
        'rare': 'epic',
        'epic': 'legendary'
    }

    if level in rarity_levels and rarity in rarity_upgrade_requirements: ##check that we have the correct level + we are not legendary
        
        requirements = rarity_upgrade_requirements[rarity] ##requirements for the current rarity upgrade

        # Comprobar si el bot tiene suficientes recursos
        if (total_junk >= requirements['junk_cost'] and total_silicon >= requirements['silicon_cost'] and 
           total_metal >= requirements['metal_cost'] and total_plastic >= requirements['plastic_cost']):
            
            # update on the total resources remaining & rarity
            new_rarity = next_rarity[rarity]
            total_junk -= requirements['junk_cost']
            total_silicon -= requirements['silicon_cost']
            total_metal -= requirements['metal_cost']
            total_plastic -= requirements['plastic_cost']

            ##print(f"Rarity upgraded to {new_rarity}. Resources deducted. New resources: Junk {junk}, Silicon {silicon}, Metal {metal}, Plastic {plastic}")
            return new_rarity, total_junk, total_silicon, total_metal, total_plastic
        else:
            ##print("Not enough resources to upgrade rarity.")
            return rarity, total_junk, total_silicon, total_metal, total_plastic
    else:
        # we dont have enough level to upgrade or we are at max level
        return rarity, total_junk, total_silicon, total_metal, total_plastic



def main():

    bots = []
    bot_name_start = 1

    for _ in range (4):
        bot_name = f'bot{bot_name_start}'
        bot = generate_bot(bot_name)
        bots.append(bot)
        bot_name_start +=1
    
    #rarity, level, health, size, haste, crit, resilience, max_energy, resource_yield_increase, mission_success_boost, mission_crit_chance, starting_energy = generate_bot(bot_name)
    
    accumulated_results = []  # list to store mission progress
    individual_missions = []
    bot_stats = []

    total_play_time = 0
    total_xp = 0
    total_junk = 0
    total_bits = 0
    total_plastic = 0
    total_metal = 0
    total_silicon = 0


    i = 0
    # Establece la condición de parada del while aquí, por ejemplo, un número máximo de iteraciones o un nivel mínimo de energía
    while i < 100:

        for bot in list(bots):

            mission_time = random.choice([2, 4, 8])
        
            bot_name, selected_mission_name, resource_name, mission_time, mission_status, total_material, xp_earned, final_bits, energy_cost, junk_earned, crit_mission = run_mission(bot, mission_time)
            
            ##if I can't complete the mission I need to recharge my bot
            if (bot['current_energy'] < energy_cost): ## special "recharge energy" mission
            
                new_energy, recharge_time = recharge_energy(bot['current_energy'], bot['starting_energy'])

                total_play_time += recharge_time  # adding the needed time to recharge to the total time
                bot['current_energy'] = new_energy

                selected_mission_name = 'Energy Recharge'
                resource_name = 'Energy'
                mission_time = recharge_time
                mission_status = True
                crit_mission = 1
                total_material = 0
                xp_earned = 0
                final_bits = 0
                energy_cost = 0
                junk_earned = 0
            
                individual_missions.append ([bot_name,selected_mission_name, resource_name, mission_time, mission_status, crit_mission, total_material, xp_earned, final_bits, energy_cost, junk_earned])
                accumulated_results.append([bot_name,selected_mission_name, resource_name, mission_time, mission_status, energy_cost, crit_mission,
                        total_plastic, total_metal, total_silicon, total_xp, total_bits, total_junk, bot['current_energy']])
                
                continue

            ## else we compute the mission rewards
            
            individual_missions.append ([bot_name, selected_mission_name, resource_name, mission_time, mission_status, crit_mission, total_material, xp_earned, final_bits, energy_cost, junk_earned])
        
            ## adding mission gains to general counters
            total_play_time += mission_time
            total_xp += xp_earned
            total_junk += junk_earned
            total_bits += final_bits
            bot['current_energy'] -= energy_cost

            if resource_name == 'Plastic':
                total_plastic += total_material
            elif resource_name == 'Metal':
                total_metal += total_material
            else:
                total_silicon += total_material
            ## adding mission gains to general counters
            ##checking if the bot can level up

            can_level_up, new_level, new_size, new_haste, new_crit = check_level_up(total_xp, total_bits, bot['level'], bot['size'], bot['haste'], bot['crit'])
            
        if can_level_up:

            bot['level'] = new_level
            bot['size'] = new_size
            bot['haste'] = new_haste
            bot['crit'] = new_crit
            bot['resource_yield_increase'] = 0.01*bot['size']
            max_energy = bot['starting_energy'] + bot['size']
            mission_success_boost = 0.005*haste
            mission_crit_chance = 0.005*crit

        ##we check if we can upgrade rarity just after level up bc you can get to lvl 5 and be able to upgrade w/o doing any mission
        rarity, total_junk, total_silicon, total_metal, total_plastic = check_and_upgrade_rarity(level, rarity, total_junk, total_silicon, total_metal, total_plastic)

        # Store the final values
        accumulated_results.append([selected_mission_name, resource_name, mission_time, mission_status, energy_cost, crit_mission,
                        total_plastic, total_metal, total_silicon, total_xp, total_bits, total_junk, energy_counter,total_play_time])
        bot_stats.append ([total_play_time, total_xp, level, rarity, health, size, haste, crit, resilience, max_energy, resource_yield_increase, mission_success_boost, mission_crit_chance])
        #print(selected_mission_name, resource_name, mission_time, mission_status, total_material, xp_earned, final_bits, energy_cost, junk_earned, crit_mission)
        i+=1

    # df creation to track
    columns_accumulated = ['Bot Name','Mission Name', 'Resource Name', 'Mission Time', 'Mission Status', 'Energy Cost', 'Crit Mission',
                'Total Plastic', 'Total Metal', 'Total Silicon', 'Total XP', 'Total Bits','Total Junk', 'Total Energy','Total Play Time']
    
    columns_mission = ['Bot Name','Mission Name', 'Resource Name', 'Mission Time', 'Mission Status', 'Crit Mission',
                'Material Earned', 'XP Earned', 'Bits Earned', 'Energy Cost', 'Junk Earned']
    
    columns_stats = ['Total Play Time', 'Total XP','Level', 'Rarity', 'Health','Size','Haste','Crit','Resilience','Max Energy','Res. Yield Incr.','Mission Success Boost','Mission Crit Chance']
    df_results = pd.DataFrame(accumulated_results, columns=columns_accumulated)
    df_results.to_csv('accumulated_results.xlsx', index=False)

    df_missions =  pd.DataFrame(individual_missions, columns=columns_mission)
    df_missions.to_csv('missions_results.xlsx', index=False)

    df_bot_stats = pd.DataFrame(bot_stats, columns=columns_stats)
    df_bot_stats.to_csv('bot_stats.csv',index=False)

if __name__ == '__main__':

    main()