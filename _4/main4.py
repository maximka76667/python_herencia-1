from Factura import Factura
from FacturaTipoA import FacturaTipoA
from FacturaTipoB import FacturaTipoB

factura = Factura(1, "13-12-2022", "12345678H", 2, 4, 15, 10)

print(factura.get_total())
# 2 * 4 + 15 + 10 = 8 + 25 = 33

factura_tipo_a = FacturaTipoA(2, "13-12-2022", "5475837G", 2, 20, 40, 30)

print(factura_tipo_a.get_total())
# 2 * 20 + 40 * (1 - 0.2) + 30 * (1 - 0.2) = 40 + 32 + 24 = 96

factura_tipo_b = FacturaTipoB(2, "13-12-2022", "5475837G", 2, 20, 40, 30)

print(factura_tipo_b.get_total())
# 2 * 20 + 40 * (1 - 0.75) + 30 * (1 - 0.5) = 40 + 10 + 15 = 65
