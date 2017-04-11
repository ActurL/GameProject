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
        name = self.name[:-2]


        return name

    def gender_data(self):

        if random.randint(1,2) == 1:
            self.gender = "Male"
        else:
            self.gender = "Female"

        gender = self.gender

        return gender

    def stats_data(self):
        self.stats = stat_gen()
        stats = self.stats

        return stats

NPCs = []
for i in range(10):
    j = NPC()
    NPCs.append([j.name_data(),j.gender_data(),j.stats_data()])

for i in NPCs:
    print(i,"\n")
