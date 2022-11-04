from Vehiculos import vehiculo
import datetime
class RepositorioPatentes:
    def __init__(self, archivo = "patentes.txt"):
        self.archivo = archivo
    def obtener_todo(self):
        patentes = []
        with open(self.archivo, 'r') as patente_auto:
            for patente_como_texto in patente_auto:
                n = self.texto_a_patente(patente_como_texto)
                patentes.append(n)
        return patentes
    
    def texto_a_patente(self, patente):
        texto = patente[:-1]
        Vehiculo_como_lista = texto.split(',')
        n = vehiculo(Vehiculo_como_lista[0], Vehiculo_como_lista[1],Vehiculo_como_lista[2], Vehiculo_como_lista[3])
        fecha_entrada = Vehiculo_como_lista[1].split('-')
        n.entrada = datetime.date(int(fecha_entrada[0]),int(fecha_entrada[1]),int(fecha_entrada[2])) 
        fecha_salida = Vehiculo_como_lista[2].split('-')
        n.salida = datetime.date(int(fecha_salida[0]),int(fecha_salida[1]),int(fecha_salida[2])) 
        return n
    
    def guardar_todo(self, patentes):
        with open(self.archivo, 'w') as patente_auto:
            for patente in patentes:
                patente_como_texto = self.patente_a_texto(patente)
                patente_auto.write(patente_como_texto)
        print("Guardado en "+ self.archivo)
    def patente_a_texto(self,vehiculo):
        entrada_en_texto = str(vehiculo.entrada.year) + '-' + str(vehiculo.entrada.month) + '-' + str(vehiculo.entrada.day)
        salida_en_texto = str(vehiculo.salida.year) + '-' + str(vehiculo.salida.month) + '-' + str(vehiculo.salida.day)
        return vehiculo.patente  + ',' + entrada_en_texto + ',' + salida_en_texto + ',' + vehiculo.slot + "\n"