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
        if 

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
