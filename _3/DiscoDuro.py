from Componente import Componente

class DiscoDuro(Componente):

    def __init__(self, ref, marca, precio, capacidad_tb, tipo_bus):
        super().__init__(ref, marca, precio)
        self.__capacidad_tb = capacidad_tb
        self.__tipo_bus = tipo_bus

    def get_capacidad_tb(self):
        return self.__capacidad_tb

    def set_capacidad_tb(self, capacidad_tb):
        self.__capacidad_tb = capacidad_tb

    def get_tipo_bus(self):
        return self.__tipo_bus

    def set_tipo_bus(self, tipo_bus):
        self.__tipo_bus = tipo_bus
