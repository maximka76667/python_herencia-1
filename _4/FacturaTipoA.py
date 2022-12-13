from Factura import Factura

class FacturaTipoA(Factura):

    __descuento = 0.2

    def __init__(self, num_factura, fecha, dni_cliente, precio_metro_cubico, metros_cubicos_consumidos, importe_saneamiento, importe_residuales):
        super().__init__(num_factura, fecha, dni_cliente, precio_metro_cubico, metros_cubicos_consumidos, importe_saneamiento, importe_residuales)
        super().set_total(super().get_importe_consumo() + (importe_saneamiento + importe_residuales) * (1 - self.__descuento))
