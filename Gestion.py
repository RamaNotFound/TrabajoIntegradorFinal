from Vehiculos import vehiculo
class gestion:
    def __init__(self, listadevehiculos = []):
        self.patentes = listadevehiculos
    def agregar_vehiculo(self, patente, entrada, salida, slot):
        nuevo_vehiculo = vehiculo(patente, entrada, salida, slot)
        self.patentes.append(nuevo_vehiculo)
        return nuevo_vehiculo
    
    def buscar_por_id(self, busqueda):
        patente_coincide = []
        for patente in self.patentes:
            if vehiculo.existeVeiculo(busqueda):
                patente_coincide.append(patente)
        return patente_coincide
    
    def eliminar_vehiculo(self, patente):
        vehiculo_existe = self.buscar_por_id(patente)
        if vehiculo_existe.patente == patente:
            self.patentes.remove(vehiculo)
            return True
        return False