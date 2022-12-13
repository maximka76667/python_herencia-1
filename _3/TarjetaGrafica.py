from Componente import Componente


class TarjetaGrafica(Componente):

    def __init__(self, ref, marca, precio, modelo, memoria_mb, tipo_bus):
        super().__init__(ref, marca, precio)
        self.__modelo = modelo
        self.__memoria_mb = memoria_mb
        self.__tipo_bus = tipo_bus

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_memoria_mb(self):
        return self.__memoria_mb

    def set_memoria_mb(self, memoria_mb):
        self.__memoria_mb = memoria_mb

    def get_tipo_bus(self):
        return self.__tipo_bus

    def set_tipo_bus(self, tipo_bus):
        self.__tipo_bus = tipo_bus

    def precio_descuento(self, descuento):
        return super().get_precio()

    def get_memoria_gb(self):
        return self.__memoria_mb * pow(10, -3)
