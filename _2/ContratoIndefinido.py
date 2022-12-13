from Contrato import Contrato


class ContratoIndefinido(Contrato):
    
    __es_pagas_prorrateadas = True
    
    def __init__(self, num_contrato, dni):
        super().__init__(num_contrato, dni)
        
    def get_pagas_prorrateadas(self):
        return self.__es_pagas_prorrateadas
    
    def set_pagas_prorrateadas(self, es_pagas_prorrateadas):
        self.__es_pagas_prorrateadas = es_pagas_prorrateadas
    
    def __str__(self):
        return super().__str__() + " " + str(self.__es_pagas_prorrateadas)
