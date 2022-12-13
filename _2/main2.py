from ContratoIndefinido import ContratoIndefinido
from ContratoPracticas import ContratoPracticas
from ContratoTemporal import ContratoTemporal

contrato_indefinido = ContratoIndefinido("1", "12345678H")
contrato_indefinido.set_nombre("Max")
contrato_indefinido.set_apellidos("Griven")
contrato_indefinido.set_salario_bruto_mensual(2000)
contrato_indefinido.set_irpf(0.15)
contrato_indefinido.set_pagas_prorrateadas(True)

contrato_temporal = ContratoTemporal("2", "87654321Z")
contrato_temporal.set_irpf(0.15)
contrato_temporal.set_nombre("Pablo")
contrato_temporal.set_apellidos("Perez")

contrato_practicas = ContratoPracticas("3", "5453534J")
contrato_practicas.set_irpf(0.15)
contrato_practicas.set_nombre("Antonio")
contrato_practicas.set_apellidos("Sanchez")

print(contrato_indefinido)
print(contrato_temporal)
print(contrato_practicas)
