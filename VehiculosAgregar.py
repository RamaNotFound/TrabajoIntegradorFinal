from vehiculos import veiculo 
class Agregarvehiculo:
    def __init__(self, listadevehiculos = []):
        self.listadevehiculos = []
    def agregar_vehiculo(self, patente, entrada, salida, slot):
        if patente:
            e = vehiculo(patente)
        else:
            return None

        self.listadevehiculos.append(e)
    def buscar_por_id(self, id_para_buscar):
        for un_vehiculo in self.listadevehiculos:
            if un_vehiculo.id == id_para_buscar:
                return un_vehiculo
        return None
    def eliminar_vehiculo(self, patente):
        vehiculo = self.buscar_por_id(patente)
        if vehiculo.patente == patente:
            self.listadevehiculos.remove(vehiculo)
            return True
        return False