from Gestion import gestion
from repositoriovehiculo import RepositorioPatentes
from Vehiculos import vehiculo
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from datetime import date
class Gui():
    def __init__(self):
        self.iniciar_gestion()
        self.iniciar_gui()

    def iniciar_gestion(self):
        self.repositorio = RepositorioPatentes()
        patentes = self.repositorio.obtener_todo()
        self.gestion = gestion(patentes)

    def iniciar_gui(self):
        self.ventana_principal = tkinter.Tk()
        self.vehiculos = gestion()
        self.repositorio = RepositorioPatentes()
        patente = self.repositorio.obtener_todo()
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
                                     columns=("Entradas","Salidas","slot"))
        self.treeview.heading("#0", text="Patentes")
        self.treeview.column("#0", minwidth=0, width="60")
        self.treeview.heading("Entradas", text="Entradas")
        self.treeview.heading("Salidas", text="Salidas")
        self.treeview.heading("slot", text="slot")
        self.treeview.grid(row=10, columnspan=3)
        self.poblar_tabla()
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.salir).grid(row=11,column=1)
        self.cajaBuscar.focus()

    def poblar_tabla(self, vehiculos = None):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        if not vehiculos:
            vehiculos = self.gestion.patentes
        for vehiculo in vehiculos:
            item = self.treeview.insert("", tkinter.END, text=vehiculo.patente,
                              values=(vehiculo.entrada, vehiculo.salida, vehiculo.slot), iid=vehiculo.patente)
        
    def agregar_vehiculo(self):
        self.modalAgregar = tkinter.Toplevel(self.ventana_principal)
        self.modalAgregar.grab_set()
        tkinter.Label(self.modalAgregar, text = "Patente: ").grid()
        self.patente = tkinter.Entry(self.modalAgregar)
        self.patente.grid(row=0,column=1,columnspan=2)
        self.patente.focus()
        tkinter.Label(self.modalAgregar, text = "Salida: ").grid(row=1)
        self.Salida = tkinter.Entry(self.modalAgregar)
        self.Salida.grid(row=1, column=1, columnspan=2)
        tkinter.Label(self.modalAgregar, text = "Slot: ").grid(row=2)
        self.slot = tkinter.Entry(self.modalAgregar)
        self.slot.grid(row=2, column=1, columnspan=2)
        botonOK = tkinter.Button(self.modalAgregar, text="Guardar",
                command=self.agregar_ok)
        self.modalAgregar.bind("<Return>", self.agregar_ok)
        botonOK.grid(row=3)
        botonCancelar = tkinter.Button(self.modalAgregar, text = "Cancelar",
                command = self.modalAgregar.destroy)
        botonCancelar.grid(row=3,column=2)

    def agregar_ok(self, event=None):
        salida = self.Salida.get()
        if salida == '':
            salida = date.today()
        else:
            salida_temp = salida.split("-")
            salida = datetime.date(int(salida_temp[0]),int(salida_temp[1]),int(salida_temp[2]))
        nuevo_vehiculo = self.gestion.agregar_vehiculo(self.patente.get(), date.today(),salida ,self.slot.get())
        self.modalAgregar.destroy()
        item = self.treeview.insert("", tkinter.END, text=nuevo_vehiculo.patente,
                                        values=(nuevo_vehiculo.entrada, nuevo_vehiculo.salida, nuevo_vehiculo.slot))

    def eliminar_vehiculo(self):
        if not self.treeview.selection():
            messagebox.showwarning("Sin selección",
                "Seleccione primero el vehiculo a eliminar")
            return False
        else:
            resp = messagebox.askokcancel("Confirmar",
                "¿Está seguro de eliminar el vehiculo?")
            if resp:
                patente = str(self.treeview.selection()[0])
                print(patente)
                if self.gestion.eliminar_vehiculo(patente):
                    self.treeview.delete(patente)
                    return True
                else:
                    messagebox.showwarning("Error al eliminar",
                "No se pudo eliminar el vehiculo")
            return False

    def buscar_Patente(self):
        filtro = self.cajaBuscar.get()
        patente = self.gestion.buscar_vehiculo(filtro)
        if patente:
            self.poblar_tabla([patente])
        else:
            messagebox.showwarning("Sin resultados",
                                "Ninguna nota coincide con la búsqueda")
            
    def salir(self):
        self.repositorio.guardar_todo(self.gestion.patentes)
        self.ventana_principal.destroy()
    
if __name__ == "__main__":
    gui = Gui()
    gui.ventana_principal.mainloop()