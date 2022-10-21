from VehiculosAgregar import Agregarvehiculo
from Vehiculos import vehiculo
class RepositorioPatentes:
    def __init__(self, archivo = "patentes.txt"):
        self.archivo = archivo
    def obtener_todo(self):
        patentes = []
        with open(self.archivo, 'r') as fp:
            for patente_como_texto in fp:
                n = self.patente_a_texto(patente_como_texto)
                patentes.append(n)
        return patente
    
    def patente_a_nota(self, patente):
        patente = texto[:-1]
        patente_como_lista = patente.split(',')
        fecha = patente_como_lista[2].split('-')
        n.fecha_creacion = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        return n
    
    def guardar_todo(self, notas):
        with open(self.archivo, 'w') as fp:
            for patente in patentes:
                patente_como_texto = self.patente_a_texto(patente)
                fp.write(patente_como_texto)
        print("Guardado en "+ self.archivo)
        
    def patente_a_texto(self,patente):
        fc = patente.fecha_creacion
        fecha_en_patente = str(fc.year) + '-' + str(fc.month) + '-' + str(fc.day)
        return nota.texto + ',' + patente.etiquetas + ',' + fecha_en_patente + "\n"