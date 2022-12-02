# Added in update 1.1
class Village:
    """This module is not approved by or associated with Mojang AB """
    def __init__(self):
        # Defines all class variables to be used later
        self.processed = False
        self.villagers = -1
        self.beds = -1
        self.houses = -1
        self.doors = -1
        self.chests = -1
        self.wheat = -1
        self.carrots = -1
        self.potatoes = -1
        self.beetroot = -1
        self.fields = -1
        self.melons = -1
        self.pumpkins = -1
        self.illagers = -1
        self.raid = -1
        self.hero = -1
        self.bells = -1
        self.well_x = -1
        self.well_z = -1
        self.well_water_y = -1
        self.water_pits = -1
        self.piers = -1
        self.rivers = -1
        self.biome = -1
        self.average_house_y = -1
        self.outpost = -1
        self.church = -1
        self.num_workbenches = -1
        self.farm_animals = -1
        self.world_seed = -1
        self.version_num = -1
        self.version_game = -1
        self.stats = []
        self.feedback = []
        self.show_stats = False

    # Uses parameters to generate file
    def define(self, villagers: int, beds: int, houses: int, doors: int, nat_chests: int, wheat: int, carrots: int,
               potatoes: int, beetroot: int, num_fields: int, melons: int, pumpkins: int, illagers: int, raid: bool,
               hero: bool, bells: int, well_x: float, well_z: float, well_water_y: int, water_pits: int, piers: int,
               rivers: int, biome: int, average_house_y: float, outpost: bool, church: bool, num_workbenches: int,
               farm_animals: bool, world_seed: int, version_num: float, version_game: bool):
        """Biome will be listed using this key. 1 = Plains. 2 = Desert, 3 = Savanna, 4 = Tiaga, 5 = Jungle, 6 = Snowy
         Tundra. This function converts information about a Minecraft village into the format of a 31-D
         village vector. This does not store it as a vector, rather it stores it as a string. For the Game Version,
         Bedrock is True and Java is False"""
        # open file
        file = open(input("What is the file name? Without .txt ")+".txt", "w")

        # convert booleans to numbers
        if raid:
            raid = 1
        else:
            raid = 0

        if hero:
            hero = 1
        else:
            hero = 0

        if outpost:
            outpost = 1
        else:
            outpost = 0

        if church:
            church = 1
        else:
            church = 0

        if version_game:
            version_game = 1
        else:
            version_game = 0

        if farm_animals:
            farm_animals = 1
        else:
            farm_animals = 0

        # write all data to the file
        file.write(f"{villagers} {beds} {houses} {doors} {nat_chests} {wheat} {carrots} {potatoes} {beetroot} ")
        file.write(f"{num_fields} {melons} {pumpkins} {illagers} {raid} {hero} {bells} {well_x} {well_z} ")
        file.write(f"{well_water_y} {water_pits} {piers} {rivers} {biome} {average_house_y} {outpost} {church} ")
        file.write(f"{num_workbenches} {farm_animals} {world_seed} {version_num} {version_game}")
        # close the file
        file.close()

    # read village data in from a file and process it
    def read_in(self, filename):
        """File name must not have .txt in it. This method reads in a village vector from a file."""
        # makes sure file name is valid
        done = False
        while not done:
            try:
                # opens file
                file = open((filename+".txt"), "r")
                vector = file.readline()
                file.close()
                done = True
            # excepts the error if there is one and asks for another name
            except FileNotFoundError:
                # asks for new file name
                print("This file was not found. Please enter the name of the file you would like to use. This may not include .txt.")
                file = open((filename + ".txt"), "r")
                vector = file.readline()
                file.close()
                done = False

        # splits the string into parts
        v = vector.split(" ")
        # puts the parts into variables defined in __init__
        self.villagers = int(v[0])
        self.beds = int(v[1])
        self.houses = int(v[2])
        self.doors = int(v[3])
        self.chests = int(v[4])
        self.wheat = int(v[5])
        self.carrots = int(v[6])
        self.potatoes = int(v[7])
        self.beetroot = int(v[8])
        self.fields = int(v[9])
        self.melons = int(v[10])
        self.pumpkins = int(v[11])
        self.illagers = int(v[12])
        self.raid = int(v[13])
        self.hero = int(v[14])
        self.bells = int(v[15])
        self.well_x = float(v[16])
        self.well_z = float(v[17])
        self.well_water_y = int(v[18])
        self.water_pits = int(v[19])
        self.piers = int(v[20])
        self.rivers = int(v[21])
        self.biome = int(v[22])
        self.average_house_y = float(v[23])
        self.outpost = int(v[24])
        self.church = int(v[25])
        self.num_workbenches = int(v[26])
        self.farm_animals = int(v[27])
        self.world_seed = int(v[28])
        self.version_num = float(v[29])
        self.version_game = int(v[30])
        # marks it as processed
        self.processed = True
        print("The data has been processed.")

    def value(self):
        """Finds the value of a village"""
        # makes sure data has been processed
        if not self.processed:
            # asks to process it
            print("The data has not been processed, so this method may not be run.")
            process = input("Y/N, Would you like to process the data? ").capitalize()
            while process != "Y" and process != "N":
                print("Please enter a valid input.")
                process = input("Y/N, Would you like to process the data? ").capitalize()
            if process == "Y":
                self.read_in(input("What is the name of the file? You may not include the .txt extension on the end. "))
                self.value()
        else:
            # defines stats and feedback lists
            stats = []
            feedback = []
            # defines the variable that stores points
            points = 0
            # gets the percentage of unused villager houses
            space = 1 - round(self.villagers/self.houses, 3)
            # appends it to stats list
            stats.append(f"{space*100}% of the space is open.")
            # checks to see if a high enough percentage is used.
            if space <= 0.25:
                points += 10
            else:
                # appends feedback to the list
                feedback.append(f"Your village needs more villagers. {space*100}% of the space is open.")

            # finds attributes and gives or removes points for them while appending stats and feedback
            if self.melons > 0:
                points += 2
            else:
                feedback.append("Wouldn't it be nice if the village had melons. You could get 2 extra points!")

            if self.outpost == 0:
                points += 5
            else:
                feedback.append("You have a pillager outpost. It is not safe"+
                                " tear it down and replace the ground near it with slabs")
            stats.append(f"You have {self.outpost} pillager outposts.")

            if self.wheat > 36:
                points += 5
            else:
                feedback.append("You need more wheat! You can get seeds from breaking tall or short grass.")

            if self.illagers > 0:
                feedback.append("This village is not safe. The illagers could kill your villagers.")
            else:
                points += 7

            if self.hero == 1:
                points += 15
            else:
                feedback.append("Consider fighting a pillager raid, you can get discounts once you defeat the raid.")

            if self.version_num >= 1.14:
                points += 10
            else:
                feedback.append("1.14, the Village and Pillage update greatly improved villages. Follow this link for"
                                + " more information. https://www.minecraft.net/en-us/updates/village-pillage")
            if self.version_num >= 1.15:
                points += 10
            else:
                feedback.append("1.15 added bees, honey can be used to cure poison. More info"
                                +" https://www.minecraft.net/en-us/updates/buzzy-bees")
            if self.raid == 1:
                points -= 5
                feedback.append("You need to finish fighting the raid.")

            if self.farm_animals == 1:
                points += 4
            else:
                feedback.append("The village needs farm animals.")

            version = "Java Edition"
            if self.version_game == 1:
                version = "Bedrock Edition"

            stats.append(f"Version: {version} {self.version_num}")

            if self.bells > 1:
                points += 3
            else:
                feedback.append("The village needs more bells, so villagers can be alerted if there is danger.")

            if self.rivers <= 0:
                feedback.append("It would be nice if there were rivers here, maybe build a canal, as this counts.")
            else:
                points += 2

            if self.carrots >= 36:
                points += 5
            else:
                feedback.append("Plant some more carrots, so you will have food.")

            if self.pumpkins > 3:
                points += 4
            else:
                feedback.append("Your village needs more pumpkins! Carving or crafting a pumpkin will yield seeds.")
            self.feedback = feedback
            self.stats = stats
            return f"The score of the village is {(round(points, 4)/82)*100}%"

    def set(self):
        # changes display stats
        print("Rule: Display Statistics?")
        stats = bool(input("What would you like to change it to? List as boolean. "))
        self.show_stats = stats

    def show_feedback(self):
        # prints feedback and possibly stats depending on settings
        feed = self.feedback
        print("Here is some feedback generated during the evaluation:\n")
        for i in feed:
            print("-", i)
        if self.show_stats:
            print("Here are the statistics of the village:\n")
            stats = self.stats
            for j in stats:
                print(j)

    def get_feedback(self):
        # returns feedback and possibly stats
        return_val = (self.feedback, self.stats)
        return return_val