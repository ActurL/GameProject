#NPC GENERATOR

from Name_Gen import names
from Stat_Gen import stat_gen
import os.path
import random

if os.path.isfile("Names.txt") and os.path.isfile("Surnames.txt"): #Check if name files exist;
    pass
else:
    names()

class NPC :

    def name_data(self):

        self.name = random.choice(open("Names List.txt", 'r').readlines())
        name = self.name

        return name

    def stats_data(self):
        self.stats = stat_gen()
        stats = self.stats

        return stats
    
    John = NPC()
    print(John.name_data())
    print(John.stats_data())
