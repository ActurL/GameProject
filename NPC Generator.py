# NPC GENERATOR

from Name_Gen import names
from Stat_Gen import stat_gen
import os.path
import random

if os.path.isfile("Names.txt") and os.path.isfile("Surnames.txt"):  # Check if name files exist;
    pass
else: 
    names()

class NPC : 

    def name_data(self):  # generates name data from name lists

        self.name = random.choice(open("Names List.txt", 'r').readlines())
        name = self.name[: -2]


        return name

    def gender_data(self):  # randomly picks gender

        if random.randint(1,2) == 1: 
            self.gender = "Male"
        else: 
            self.gender = "Female"

        gender = self.gender

        return gender

    def race_data(self):  # generates random race for NPC

        races = ["Dwarf", "Elf", "Half-elf", "Human", "Orc"]

        return random.choice(races)

    def stats_data(self):  # generates stats

        self.stats = stat_gen()
        stats = self.stats

        return stats

    def profession_data(self): 

        #  full list of professions
        professions = {"Agriculture": {"Farmer": ["Cowherd", "Dung Carter", "Farmer", "Gardner", "Goatherd", "Hawker",
                                                  "Peasant", "Serf", "Shepherd", "Swineherd", "Woodcutter"],
                                      
                                       "Hunter": ["Falconer", "Forester", "Fowler", "Hawker", "Hunter", "Rat Catcher"]},

                       "Aquaculture": {"Fisherman": ["Fisherman", "Oysterer"]},

                       "Artist": {"Visual_Art": ["Fresco painter", "Glass painter", "Painter", "Sculptor"],

                                  "Literary_Art": ["Composer", "Playwright", "Poet", "Writer"]},

                       "Craftsman": {"Main": ["Shoemaker", "Tailor", "Jeweler", "Mason", "Carpenter", "Weaver", "Baker",
                                              "Hatmaker", "Butcher", "Roofer", "Locksmith", "Ropemaker", "Tanner",
                                              "Rugmaker"],

                                     "Blacksmith": ["Armorsmith", "Bladesmith", "Fletcher", "Gunsmith"],

                                     "Craft_Misc": ["Basketmaker", "Beekeeper", "Bellmaker", "Bookbinder",
                                                    "Bookprinter", "Brewer", "Calligrapher", "Cardmaker",
                                                    "Cartographer", "Cheesemaker", "Clockmaker", "Dyer",
                                                    "Furniture maker", "Glassblower",]},

                       "Criminal": {"Thief": ["Bandit", "Burglar", "Charlatan", "Pickpocket"]},

                       "Entertainer": {"Musician": ["Bard", "Fiddler", "Harper", "Piper", "Singer"],

                                       "Entertain_Misc": ["Actor", "Dancer", "Jester", "Juggler", "Storyteller"]},

                       "Government": {"Main": ["Bailiff", "Captain of the Guard", "Chamberlain", "Chancellor",
                                               "Constable", "Diplomat", "Emperor", "Herald", "Jailer", "Judge",
                                               "King", "Noble", "Prince", "Seneschal", "Scheriff", "Steward",
                                               "Tax Collector", "Treasurer"]},

                       "Merchant": {"Main": ["Apothecary", "Banker", "Innkeeper", "Merchant", "Spice Merchant",
                                             "Wine Seller", "Wood Seller"]},

                       "Military": {"Soldier": ["Archer", "Crossbowman", "Halberdier", "Knight", "Pikeman",
                                                "Scout", "Spearman", "Squire"],

                                   "Officer": ["Admiral", "Captain", "General", "Marhsal", "Sergeant"],

                                   "Camp_Follower": ["Camp Cook"]},

                       "Religion": {"Main": ["Archbishop", "Bishop", "Cardinal", "Chantry Priest", "Curate", "Friar",
                                             "Monk", "Nun", "Priest"]},

                       "Scholar": {"Main": ["Alchemist", "Astronomist", "Herbalist", "Librarian", "Mathematician",
                                            "Philosopher", "Theologian"]},

                       "Unemployed": {"Main": ["Beggar", "Housewife", "Landlord", "Urchin"]}
                       }

        #  Select a category of professions from the dictionary

        npc_profession_category = professions[random.choice(list(professions.keys()))]

        #  Select a sub-group of professions from the selected category

        npc_profession_list = npc_profession_category[random.choice(list(npc_profession_category.keys()))]

        #  Select a specific profession

        npc_profession = random.choice(npc_profession_list)

        return(npc_profession)

def npc_gen(npc_num):  # generates npc_num number of NPCs
    NPCs = []

    for i in range(npc_num):   # for i in range of the number of NPCs wanted do: 
        j = NPC()  # make j an NPC class

        # append lists of NPC data
        NPCs.append({j.name_data():[ j.gender_data(), j.stats_data(), j.race_data(), j.profession_data()]})

    return NPCs # return list of generated NPCs


for i in npc_gen(5):
    print(i)