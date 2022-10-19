from Veiculos import Veiculo
class VeiculosMes:
    def __init__(self, Id, Categoria):
        self.Id = Id
        self.Categoria = Categoria
    def mostrar_datos(self):
        return super().mostrar_datos() + f"Id: {self.Id}\n"
