class vehiculo:
    def __init__(self, patente, slot, entrada, salida):
        self.patente = patente
        self.slot = slot
        self.entrada = entrada
        self.salida = salida
    
    def existePlanta(self, busqueda):
        return ((busqueda in self.patente) or (busqueda in self.slot))