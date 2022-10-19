from VeiculosMes import VeiculosMes
from VeiculosHora import VeiculosHora
class AgregarVeiculo:
    def __init__(self):
        self.listadeveiculos = []
    def agregar_Veiculo(self, Slot, Id = None, horas = None):
        if Id:
            e = VeiculosMes(Id)
        elif horas:
            e = VeiculosHora(horas)
        else:
            return None

        self.listadeveiculos.append(e)
    def buscar_por_id(self, id_para_buscar):
        for un_Veiculo in self.listadeveiculos:
            if un_Veiculo.id == id_para_buscar:
                return un_Veiculo
        return None
    def eliminar_veiculo(self, Slot):
        for veiculo in self.listadeveiculos:
            if nota == id_nota:
                self.notas.remove(nota)