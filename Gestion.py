from Vehiculos import vehiculo 
class gestion:
    def __init__(self, listadevehiculos = []):
        self.patentes = listadevehiculos
    def agregar_vehiculo(self, patente, entrada, salida, slot):
        nuevo_vehiculo = vehiculo(patente, entrada, salida, slot)
        self.patentes.append(nuevo_vehiculo)
        return nuevo_vehiculo
    def buscar_por_id(self, id_para_buscar):
        for nuevo_vehiculo in self.patentes:
            if nuevo_vehiculo.patente == un_vehiculo:
                return un_vehiculo
        return None
    def eliminar_vehiculo(self, patente):
        vehiculo = self.buscar_por_id(patente)
        if vehiculo.patente == patente:
            self.patentes.remove(vehiculo)
            return True
        return False