from DiscoDuro import DiscoDuro
from Pendrive import Pendrive
from TarjetaGrafica import TarjetaGrafica

disco_duro = DiscoDuro("HD1050", "Western Digital", 118.77, 2, "SATA3")
tarjeta_grafica = TarjetaGrafica("TG0004", "ASUS", 131.28, "GTX550", 1024, "PCI Express")

print("Precio disco duro:", disco_duro.get_precio())
print("Precio tajeta:", tarjeta_grafica.get_precio())

print(disco_duro.precio_descuento(0.15))
print(tarjeta_grafica.precio_descuento(0.15))

print(tarjeta_grafica.get_memoria_gb())

pendrive = Pendrive("USB1001", "SanDisk", 18, 16)

print(pendrive.precio_descuento(0.1))

pendrive.set_precio(20)
pendrive.set_ref("USB1002")

print("\nCambiar precio y referencia")

print(pendrive.get_ref())
print(pendrive.get_marca())
print(pendrive.get_precio())
print(pendrive.get_capacidad_gb())
