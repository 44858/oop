# Cow Class

from animal_class import *

class Cow(Animal):
    """ A cow animal """
    def __init__(self):
        super().__init__(1,3,6)
        self._weight = 12
        self._type =  "Cow"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Newborn" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            elif self._status == "Old" and water > self._water_need:
                self._weight += self._growth_rate / 2
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

        
