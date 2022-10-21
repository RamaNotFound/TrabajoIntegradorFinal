class vehiculo:
    def __init__(self, patente, entrada, slot=None):
        self.patente = patente
        self.slot = slot
        self.entrada = entrada
      
    
    def existeVeiculo(self, busqueda):
        return ((busqueda in self.patente) or (busqueda in self.slot))