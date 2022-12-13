class Mascota():
    
    __IVA = 0.21

    def __init__(self, nombre, num_patas, raza, precio, color):
        self.__nombre = nombre
        self.__num_patas = num_patas
        self.__raza = raza
        self.__precio = precio
        self.__color = color

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_num_patas(self):
        return self.__num_patas

    def set_num_patas(self, num):
        self.__num_patas = num

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def pvp(self):
        return self.__precio * (1 + self.__IVA)

    def __str__(self):
        return self.__nombre + " " + str(self.__num_patas) + " " + self.__raza + " " + str(self.__precio) + " " + self.__color
