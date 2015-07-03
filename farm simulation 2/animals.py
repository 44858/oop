class Animal:
    """A generic animal"""
    def __init__(self,growth_rate,food_need,water_need):
        self._weight = 8
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Newborn"
        self._type = "Generic"

    def needs(self):
        return {"food need":self._food_need,"water_need":self._water_need}

    def report(self):
        return {"type":self._type,"status":self._status,"weight":self._weight,"days growing":self._days_growing}


    def update_status(self):
        if self._weight < 80:
            self._status = "Old"
        elif self._weight < 55:
            self._status = "Mature"
        elif self._weight < 30:
            self._status = "Young"
        elif self._weight < 20:
            self._status = "Very Young"
        elif self._weight < 10:
            self._status = "Newborn"
    
            

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
