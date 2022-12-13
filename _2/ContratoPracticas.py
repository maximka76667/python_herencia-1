from Contrato import Contrato

class ContratoPracticas(Contrato):

    __titulacion_curso = ""
    __duracion_meses = 6

    def __init__(self, num_contrato, dni):
        super().__init__(num_contrato, dni)

    def get_titulacion_curso(self):
        return self.__titulacion_curso

    def set_titulacion_curso(self, titulacion_curso):
        self.__titulacion_curso = titulacion_curso

    def get_duracion_meses(self):
        return self.__duracion_meses

    def set_duracion_meses(self, duracion_meses):
        self.__duracion_meses = duracion_meses

    def __str__(self):
        return super().__str__() + " " + str(self.__duracion_meses) + " " + self.__titulacion_curso
