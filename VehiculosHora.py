from vehiculos import vehiculo
class vehiculosHora:
    def __init__(self, horas, Slot):
        self.horas = horas
        self.Categoria = Categoria
    def mostrar_datos(self):
        return super().mostrar_datos() + f"Cantidad de horas: {self.horas}\n"