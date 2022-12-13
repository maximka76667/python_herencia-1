from _1.Mascota import Mascota


class Perro(Mascota):

    def __init__(self, nombre, raza, precio, color, patita = False, num_patas = 4):
        super().__init__(nombre, num_patas, raza, precio, color)
        self.__patita = patita

    def __str__(self):
        return super().__str__() + " " + str(self.__patita)
