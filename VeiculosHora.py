from Veiculos import Veiculo
class VeiculosHora:
    def __init__(self, horas, Categoria):
        self.horas = horas
        self.Categoria = Categoria
    def mostrar_datos(self):
        return super().mostrar_datos() + f"Cantidad de horas: {self.horas}\n"