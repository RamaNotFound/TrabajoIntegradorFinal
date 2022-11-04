class vehiculo:
    def __init__(self, patente, entrada,salida, slot):
        self.patente = patente
        self.slot = slot
        self.entrada = entrada
        self.salida = salida
      
    
    def existeVeiculo(self, busqueda):
        return (busqueda in self.patente) or (busqueda in self.slot)