from VehiculosAgregar import Agregarvehiculo
from Vehiculos import vehiculo
class RepositorioAnotador:
    def __init__(self, archivo = "patentes.txt"):
        self.archivo = archivo
    def obtener_todo(self):
        patentes = []
        with open(self.archivo, 'r') as fp:
            for patente_como_texto in fp:
                n = self.texto_a_patente(patente_como_texto)
                patentes.append(n)
        return patente
