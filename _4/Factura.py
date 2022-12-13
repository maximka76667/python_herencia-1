class Factura(object):

    def __init__(self, num_factura, fecha, dni_cliente, precio_metro_cubico, metros_cubicos_consumidos, importe_saneamiento, importe_residuales):
        self.__num_factura = num_factura
        self.__fecha = fecha
        self.__dni_cliente = dni_cliente
        self.__precio_metro_cubico = precio_metro_cubico
        self.__metros_cubicos_consumidos = metros_cubicos_consumidos
        self.__importe_consumo = precio_metro_cubico * metros_cubicos_consumidos
        self.__importe_saneamiento = importe_saneamiento
        self.__importe_residuales = importe_residuales
        self.__total = self.__importe_consumo + self.__importe_saneamiento + self.__importe_residuales

    def get_importe_consumo(self):
        return self.__importe_consumo

    def get_total(self):
        return self.__total

    def set_total(self, total):
        self.__total = total
