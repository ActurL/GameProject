# Stats generator for NPCs

import random  # import the random module

def stat_gen():
    stats = {'STR':0, 'DEX':0, 'CON':0, 'INT':0, 'WIS':0, 'CHA':0} # make blank stats for the NPC

    for k, v in stats.items():  # Generate a random roll for each stat

        roll = []  # Make empty list of dice rolls

        # Make 4 dice rolls and drop the lowest one; sum the nums to get stat roll
        for die in range(4):
            roll.append(random.randint(1,6))

        roll.remove(min(roll))

        roll = sum(roll)

        # Set stat to its roll

        stats[k] = roll
    return stats

