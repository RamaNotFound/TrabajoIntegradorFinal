from VeiculosMes import VeiculosMes
class AgregarVeiculo:
    def __init__(self):
        self.listadeveiculos = []
    def agregar_Veiculo(self, Id = None, Tiempo = None):
        if Id:
            e = VeiculosMes(Id)
        
