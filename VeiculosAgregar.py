from VeiculosMes import VeiculosMes
from VeiculosHora import VeiculosHora
class AgregarVeiculo:
    def __init__(self):
        self.listadeveiculos = []
    def agregar_Veiculo(self, Id = None, horas = None):
        if Id:
            e = VeiculosMes(Id)
        elif horas:
            e = VeiculosHora(horas)
        else:
            return None

        self.listadeveiculos.append(e)