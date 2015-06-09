#Lewis Travers
#09/06/2015
#Virtual Pet

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.age = 0
        self.energy = 50
        self.foods("Apple", "Grapes", "Ice cream")
        self.mood = 10
        self.weight = 20
        self.fatigue = 100

    def eat(self, food):
        if self.energy < 85:
            if food in self.foods:
                if food == self.foods[0]:   
                    self.energy = self.energy + 20
                    self.mood = self.mood + 2
                    self.weight = self.weight + 5
                    print("Yummy!")
                elif food == self.foods[1]:
                    self.energy = self.energy + 10
                    self.mood = self.mood + 5
                    self.weight = self.weight + 2
                    print("Delicious!")
                elif food == self.foods[2]:
                    self.energy = self.energy + 5
                    self.mood = self.mood + 5
                    self.weight = self.weight + 10
                    print("That's my favourite!!")
                else:
                    print("I'm not going to eat that!")
        else:
            print("I'm not hungry!")
            
    def walk(self):
        if energy > 20:
            self.weight = self.weight - 10
            self.energy = self.energy - 10
            self.mood = self.mood + 5
        else:
            print("I'm too tired!")
            
    def sleep(self):
        if 
        

pet_one = VirtualPet()

