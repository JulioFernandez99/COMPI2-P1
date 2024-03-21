import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import analizador.analizador as g
from procesos.procesar_instrucciones import procesar_instrucciones


from tabla.tablaSimbolos import TablaSimbolos


#funcion para insertar texto en el text


class rootlevel1:
    
    def insertText(self, text):
        self.limpiarData()
        self.text = tk.Text(self.frameData, wrap="none")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.insert(tk.END, text)
        self.text.config(state="disabled")
        
    def on_new(self):
        print("Se seleccionó 'Nuevo'")

    def on_open(self):
        print("Se seleccionó 'Abrir'")

    def on_save(self):
        print("Se seleccionó 'Guardar'")

    def on_exit(self):
       self. root.destroy()

    def on_tool(self):
        print("Se seleccionó 'Analizar'")

    def analizar(self):
        
        input_text = self.textInput.get("1.0", "end-1c")
    
        self.instrucciones = g.parse(input_text)
        self.ts = TablaSimbolos()
        try:
            procesar_instrucciones(self.instrucciones, self.ts, save=True)
            procesar_instrucciones(self.instrucciones,self.ts)
        except Exception as e:
            print("Error", e)
            
        self.insertText(self.ts.salida)
        if len(self.ts.errores) > 0:
            self.errores()
        
        
    def limpiarData(self):
        self.frameData.destroy()
        self.frameData = tk.Frame(self.framePrincipal)
        self.frameData.place(relx=0.018, rely=0.732, relheight=0.242
                , relwidth=0.96)
        self.frameData.configure(relief='groove')
        self.frameData.configure(borderwidth="2")
        self.frameData.configure(relief="groove")
        self.frameData.configure(background="#d9d9d9")
        self.frameData.configure(highlightbackground="#d9d9d9")
        self.frameData.configure(highlightcolor="black")

    def consola(self):
        self.limpiarData()
        self.text = tk.Text(self.frameData, wrap="none")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.insert(tk.END, self.ts.salida)
        self.text.config(state="disabled")
    
    def tablaSimbolos(self):
        self.limpiarData()
        self.text = tk.Text(self.frameData, wrap="none")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.insert(tk.END, "Tabla de Simbolos")
        self.text.config(state="disabled")

    def errores(self):
        self.limpiarData()
        self.text = tk.Text(self.frameData, wrap="none")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.insert(tk.END, self.ts.errores)
        self.text.config(state="disabled")

    def __init__(self):
        self.root = tk.Tk()
        self.instrucciones = None
        self.ts = None

        #--------------------------Menu cascada--------------------------
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        file_archivo = tk.Menu(menu_bar, tearoff=0)
        file_tools = tk.Menu(menu_bar, tearoff=0)
        file_reportes = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_archivo)
        menu_bar.add_cascade(label="Herramientas", menu=file_tools)
        menu_bar.add_cascade(label="Herramientas", menu=file_reportes)

        file_archivo.add_command(label="Crear", command=self.on_new)
        file_archivo.add_command(label="Abrir", command=self.on_open)
        file_archivo.add_command(label="Guardar", command=self.on_save)

        file_tools.add_command(label="Ejecutar", command=self.on_tool)
        file_reportes.add_command(label="Errores", command=self.on_tool)
        file_reportes.add_command(label="Tabla de simmbolos", command=self.on_tool)
        #--------------------------Fin Menu cascada--------------------------
 
        self.root.geometry("1105x677+127+3")
        self.root.minsize(120, 1)
        self.root.maxsize(3290, 984)
        self.root.resizable(1,  1)
        self.root.title("OLCSCRIPT IDE")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")


        self.framePrincipal = tk.Frame(self.root)
        self.framePrincipal.place(relx=0.0, rely=0.0, relheight=1.009
                , relwidth=1.004)
        self.framePrincipal.configure(relief='groove')
        self.framePrincipal.configure(borderwidth="2")
        self.framePrincipal.configure(relief="groove")
        self.framePrincipal.configure(background="#808080")
        self.framePrincipal.configure(highlightbackground="#d9d9d9")
        self.framePrincipal.configure(highlightcolor="black")
        self.btnConsola = tk.Button(self.framePrincipal,command=self.consola)
        self.btnConsola.place(relx=0.018, rely=0.668, height=44, width=87)
        self.btnConsola.configure(activebackground="#0080c0")
        self.btnConsola.configure(activeforeground="black")
        self.btnConsola.configure(background="#0080c0")
        self.btnConsola.configure(compound='left')
        self.btnConsola.configure(disabledforeground="#a3a3a3")
        self.btnConsola.configure(font="-family {Leelawadee UI Semilight} -size 11 -weight bold")
        self.btnConsola.configure(foreground="#ffffff")
        self.btnConsola.configure(highlightbackground="#d9d9d9")
        self.btnConsola.configure(highlightcolor="black")
        self.btnConsola.configure(pady="0")
        self.btnConsola.configure(text='''Consola''')
        self.btnSimbolos = tk.Button(self.framePrincipal,command=self.tablaSimbolos)
        self.btnSimbolos.place(relx=0.099, rely=0.668, height=44, width=137)
        self.btnSimbolos.configure(activebackground="beige")
        self.btnSimbolos.configure(activeforeground="black")
        self.btnSimbolos.configure(background="#004080")
        self.btnSimbolos.configure(compound='left')
        self.btnSimbolos.configure(disabledforeground="#a3a3a3")
        self.btnSimbolos.configure(font="-family {Leelawadee UI} -size 10 -weight bold")
        self.btnSimbolos.configure(foreground="#ffffff") 
        self.btnSimbolos.configure(highlightbackground="#d9d9d9")
        self.btnSimbolos.configure(highlightcolor="black")
        self.btnSimbolos.configure(pady="0")
        self.btnSimbolos.configure(text='''Tabla de Simbolos''')
        self.btnErrores = tk.Button(self.framePrincipal,command=self.errores)
        self.btnErrores.place(relx=0.225, rely=0.666, height=44, width=87)
        self.btnErrores.configure(activebackground="beige")
        self.btnErrores.configure(activeforeground="black")
        self.btnErrores.configure(background="#008080")
        self.btnErrores.configure(compound='left')
        self.btnErrores.configure(disabledforeground="#a3a3a3")
        self.btnErrores.configure(font="-family {Leelawadee UI} -size 10 -weight bold")
        self.btnErrores.configure(foreground="#ffffff")
        self.btnErrores.configure(highlightbackground="#d9d9d9")
        self.btnErrores.configure(highlightcolor="black")
        self.btnErrores.configure(pady="0")
        self.btnErrores.configure(text='''Errores''')

        self.frameData = tk.Frame(self.framePrincipal)
        self.frameData.place(relx=0.018, rely=0.732, relheight=0.242, relwidth=0.96)
        self.frameData.configure(relief='groove')
        self.frameData.configure(borderwidth="2")
        self.frameData.configure(relief="groove")
        self.frameData.configure(background="#d9d9d9")
        self.frameData.configure(highlightbackground="#d9d9d9")
        self.frameData.configure(highlightcolor="black")
        
        
        self.btnEjecutar = tk.Button(self.framePrincipal,command=self.analizar)
        self.btnEjecutar.place(relx=0.794, rely=0.264, height=44, width=157)
        self.btnEjecutar.configure(activebackground="beige")
        self.btnEjecutar.configure(activeforeground="black")
        self.btnEjecutar.configure(background="#00d900")
        self.btnEjecutar.configure(compound='left')
        self.btnEjecutar.configure(disabledforeground="#a3a3a3")
        self.btnEjecutar.configure(font="-family {Leelawadee UI} -size 12 -weight bold")
        self.btnEjecutar.configure(foreground="#000000")
        self.btnEjecutar.configure(highlightbackground="#d9d9d9")
        self.btnEjecutar.configure(highlightcolor="black")
        self.btnEjecutar.configure(pady="0")
        self.btnEjecutar.configure(text='''Ejecutar''')
        self.frameInput = tk.Frame(self.framePrincipal)

        #-----------------------------Input Text------------------------------
        self.frameInput.place(relx=0.018, rely=0.034, relheight=0.608
                , relwidth=0.753)
        self.frameInput.configure(relief='groove')
        self.frameInput.configure(borderwidth="2")
        self.frameInput.configure(relief="groove")
        self.frameInput.configure(background="#d9d9d9")
        self.frameInput.configure(highlightbackground="#d9d9d9")
        self.frameInput.configure(highlightcolor="black")
        
        # Agregar Text en lugar de Entry
        self.textInput = tk.Text(self.frameInput, wrap="none")
        self.textInput.pack(side="left", fill="both", expand=True)

         # Agregar scrollbar vertical
        y_scrollbar = ttk.Scrollbar(self.frameInput, orient="vertical", command=self.textInput.yview)
        y_scrollbar.pack(side="right", fill="y")
        self.textInput.config(yscrollcommand=y_scrollbar.set)

        self.btnReportes = tk.Button(self.framePrincipal)
        self.btnReportes.place(relx=0.794, rely=0.351, height=44, width=157)
        self.btnReportes.configure(activebackground="beige")
        self.btnReportes.configure(activeforeground="black")
        self.btnReportes.configure(background="#fd7e00")
        self.btnReportes.configure(compound='left')
        self.btnReportes.configure(disabledforeground="#a3a3a3")
        self.btnReportes.configure(font="-family {Leelawadee UI} -size 12 -weight bold")
        self.btnReportes.configure(foreground="#000000")
        self.btnReportes.configure(highlightbackground="#d9d9d9")
        self.btnReportes.configure(highlightcolor="black")
        self.btnReportes.configure(pady="0")
        self.btnReportes.configure(text='''Mostrar reportes''')

        
    def run(self):
        self.root.mainloop()

        
        

sf=rootlevel1()
sf.run()


