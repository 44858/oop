#field class

from potato_class import *
from wheat_class import *
from sheep_class import *
from cow_class import *

class Field:
    """Simulate a field that can contain animals and crops"""

    #constructor
    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

def main():
    new_field = field(5,2)

if __name__ == "__main__":
    main()
