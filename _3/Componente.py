class Componente():

    def __init__(self, ref, marca, precio):
        self.__ref = ref
        self.__precio = precio
        self.__marca = marca

    def get_ref(self):
        return self.__ref

    def set_ref(self, ref):
        self.__ref = ref

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def precio_descuento(self, descuento):
        return self.__precio * (1 - descuento)
