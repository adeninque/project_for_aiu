from typing import Type


class Cell:
    def __init__(self, tribe):
        if type(tribe) != str:
            raise TypeError('Tribe should be string')
        self.__tribe = tribe
        self.__color = tribe

    @property
    def tribe(self):
        return self.__tribe

    @property
    def color(self):
        return self.__color
    
    def __str__(self):
        return self.__color