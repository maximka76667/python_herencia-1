from _1.Mascota import Mascota


class Loro(Mascota):

    def __init__(self, nombre, raza, precio, color, habla = False, num_patas = 2):
        super().__init__(nombre, num_patas, raza, precio, color)
        self.__habla = habla

    def __str__(self):
        return super().__str__() + " " + str(self.__habla)
