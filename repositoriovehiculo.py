from VehiculosAgregar import Agregarvehiculo
from Vehiculos import vehiculo
import datetime
class RepositorioPatentes:
    def __init__(self, archivo = "patentes.txt"):
        self.archivo = archivo
    def obtener_todo(self):
        patentes = []
        with open(self.archivo, 'r') as patente_auto:
            for patente_como_texto in patente_auto:
                n = self.patente_a_texto(patente_como_texto)
                patentes.append(n)
        return patente
    
    def patente_a_texto(self, patente):
        texto = patente[:-1]
        patente_como_lista = patente.split(',')
        n = vehiculo(vehiculo_como_lista[0], vehiculo_como_lista[1])
        fecha = vehiculo_como_lista[2].split('-')
        n.fecha_creacion = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        return n
    
    def guardar_todo(self, notas):
        with open(self.archivo, 'w') as patente_auto:
            for patente in patentes:
                patente_como_texto = self.patente_a_texto(patente)
                patente_auto.write(patente_como_texto)
        print("Guardado en "+ self.archivo)
        
    def texto_a_patente(self,patente):
        entrada = vehiculo().fecha_creacion
        fecha_en_texto = str(entrada.year) + '-' + str(entrada.month) + '-' + str(entrada.day)
        return vehiculo.patente + ',' + fecha_en_texto + "\n"