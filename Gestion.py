from Vehiculos import vehiculo
from repositoriovehiculo import RepositorioPatentes
class gestion:
    def __init__(self, listadevehiculos = []):
        self.patentes = listadevehiculos
    def agregar_vehiculo(self, patente, entrada, salida, slot):
        nuevo_vehiculo = vehiculo(patente, entrada, salida, slot)
        self.patentes.append(nuevo_vehiculo)
        repo = RepositorioPatentes()
        repo.guardar_todo(self.patentes)
        return nuevo_vehiculo
    
    def buscar_vehiculo(self,busqueda):
        for vehiculo in self.patentes:
            if str(vehiculo.patente) == str(busqueda):
                return vehiculo
        return None
    
    def buscar_por_id(self,busqueda):
        patente_coincide = []
        for nuevo_vehiculo in self.patentes:
            if vehiculo.existeVeiculo(busqueda):
                patente_coincide.append(nuevo_vehiculo)
        return patente_coincide
    
    def eliminar_vehiculo(self, busqueda):
        vehiculo_existe = self.buscar_vehiculo(busqueda)
        print(vehiculo_existe.patente)
        if vehiculo_existe:
            self.patentes.remove(vehiculo_existe)
            repo = RepositorioPatentes()
            repo.guardar_todo(self.patentes)
            return True
        return False