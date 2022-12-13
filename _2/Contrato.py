class Contrato():

    __nombre = ""
    __apellidos = ""
    __salario_bruto_mensual = 1000
    __irpf = 0

    def __init__(self, num_contrato, dni):
        self.__num_contrato = num_contrato
        self.__dni = dni

    def get_num_contrato(self):
        return self.__num_contrato

    def set_num_contrato(self, num_contrato):
        self.__num_contrato = num_contrato
        
    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def get_salario_bruto_mensual(self):
        return self.__salario_bruto_mensual

    def set_salario_bruto_mensual(self, salario_bruto_mensual):
        self.__salario_bruto_mensual = salario_bruto_mensual
        
    def get_irpf(self):
        return self.__irpf

    def set_irpf(self, irpf):
        self.__irpf = irpf

    def salario_neto(self):
        return self.__salario_bruto_mensual * (1 - self.__irpf)

    def __str__(self):
        return self.__num_contrato + " " + self.__dni + " " + self.__nombre + " " + self.__apellidos + " " + str(self.__salario_bruto_mensual) + " " + str(self.__irpf) + " " + str(self.salario_neto())
