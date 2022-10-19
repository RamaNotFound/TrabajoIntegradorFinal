from vehiculos import vehiculo
class vehiculosMes:
    def __init__(self, Id, Slot):
        self.Id = Id
        self.Categoria = Categoria
    def mostrar_datos(self):
        return super().mostrar_datos() + f"Id: {self.Id}\n"
