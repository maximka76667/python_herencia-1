from Componente import Componente



class Pendrive(Componente):

    def __init__(self, ref, marca, precio, capacidad_gb):
        super().__init__(ref, marca, precio)
        self.__capacidad_gb = capacidad_gb

    def get_capacidad_gb(self):
        return self.__capacidad_gb

    def set_capacidad_gb(self, capacidad_gb):
        self.__capacidad_gb = capacidad_gb
