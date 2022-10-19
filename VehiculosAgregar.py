from vehiculosMes import vehiculosMes
from vehiculosHora import vehiculosHora
class Agregarvehiculo:
    def __init__(self):
        self.listadevehiculos = []
    def agregar_vehiculo(self, Slot, Id = None, horas = None):
        if Id:
            e = vehiculosMes(Id)
        elif horas:
            e = vehiculosHora(horas)
        else:
            return None

        self.listadevehiculos.append(e)
    def buscar_por_id(self, id_para_buscar):
        for un_vehiculo in self.listadevehiculos:
            if un_vehiculo.id == id_para_buscar:
                return un_vehiculo
        return None
    def eliminar_vehiculo(self, Slot):
        for vehiculo in self.listadevehiculos:
            if vehiculo == Slot:
                self.listadevehiculos.remove(vehiculo)