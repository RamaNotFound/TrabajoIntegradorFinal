from VehiculosAgregar import Agregarvehiculo
from repositoriovehiculo import RepositorioPatentes
from Vehiculos import vehiculo
import tkinter
from tkinter import ttk
from tkinter import messagebox
class Gui():
    def __init__(self):
        self.ventana_principal = tkinter.Tk()
        self.vehiculo = vehiculo()
        self.repositorio = RepositorioPatentes()
        patentes = self.repositorio.obtener_todo()
        self.ventana_principal.title("vehiculo")
        botonAgregar=tkinter.Button(self.ventana_principal,text="Agregar un vehiculo", 
                           command = self.agregar_vehiculo).grid(row=0, column=0)
        botonEliminar=tkinter.Button(self.ventana_principal, text = "Eliminar",
                command = self.eliminar_vehiculo).grid(row=0, column=2)
        tkinter.Label(self.ventana_principal,text="Buscar").grid(row=1,column=0)
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text = "Buscar",
                           command = self.buscar_Patente).grid(row=1, column=2)
        self.treeview = ttk.Treeview(self.ventana_principal)
        self.treeview = ttk.Treeview(self.ventana_principal, 
                                     columns=("Patentes", "Entradas"))
        self.treeview.heading("#0", text="id")
        self.treeview.column("#0", minwidth=0, width="40")
        self.treeview.heading("Patentes", text="Patentes")
        self.treeview.heading("Entradas", text="Entradas")
        self.treeview.grid(row=10, columnspan=3)
        self.poblar_tabla()
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)
        self.cajaBuscar.focus()

    def poblar_tabla(self, Patente = None):

        for i in self.treeview.get_children():
            self.treeview.delete(i)
        if not Patente:
            Patente = self.vehiculo.Patente
        for nota in Patente:
            item = self.treeview.insert("", tkinter.END, text=nota.id,
                              values=(nota.texto, nota.etiquetas), iid=nota.id)
        
    def agregar_vehiculo(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Patente: ").grid()
        self.texto = tkinter.Entry(self.modalAgregar)
        self.texto.grid(row=0,column=1,columnspan=2)
        self.texto.focus()
        tkinter.Label(self.modalAgregar, text = "Entrada: ").grid(row=1)
        self.Entrada = tkinter.Entry(self.modalAgregar)
        self.Entrada.grid(row=1, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=2)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=2,column=2)

    def agregar_ok(self, event=None):
        vehiculo = self.Agregarvehiculo.agregar_vehiculo(self.texto.get(), self.etiquetas.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=nota.id,
                                        values=(nota.texto, nota.etiquetas))

    def eliminar_vehiculo(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                "Seleccione primero el vehiculo a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                "¿Está seguro de eliminar el vehiculo?")
            if resp:
                id_nota = int(self.treeview.selection()[0][1:])
                if self.Agregarvehiculo.eliminar_vehiculo(id_nota):
                    self.treeview.delete(self.treeview.selection()[0])
                    return True
            return False

    def buscar_Patente(self):
        filtro = self.cajaBuscar.get()
        Patente = self.Agregarvehiculo.buscar(filtro)
        if patentes:
            self.poblar_tabla(patentes)
        else:
            messagebox.showwarning("Sin resultados",
                                "Ninguna nota coincide con la búsqueda")
            
    def salir():
        self.repositorio.guardar_todo(self.Agregarvehiculo.patente)
        self.ventana_principal.destroy()
    
if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()