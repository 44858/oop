# Sheep Class

from animal_class import *

class Sheep(Animal):
    """ A sheep animal """
    def __init__(self):
        super().__init__(1,3,6)
        self._weight = 10
        self._type =  "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Newborn" and water > self._water_need:
                self._weight += self._growth_rate * 1.4
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 1.3
            elif self._status == "Old" and water > self._water_need:
                self._weight += self._growth_rate / 2
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

