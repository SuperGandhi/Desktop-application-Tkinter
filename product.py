#Importando librerias
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from nltk import tree


#Desarrollo del GUI

root = Tk()
root.title('Ferreteria El Tornillo Feliz')
root.geometry("620x350")

id = StringVar()
codproduct = StringVar()
description= StringVar()
price = StringVar()
total = StringVar()

def conection_bd():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    try:
        cursor.execute('''
            CREATE TABLE product(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CODPRODUCT VARCHAR(10) NOT NULL,
            DESCRIPTION VARCHAR(100) NOT NULL,
            PRICE FLOAT NOT NULL,
            TOTAL FLOAT NOT NULL)
            ''')

        messagebox.showinfo("CONEXION", "Base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

def delete_bd():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    if messagebox.askyesno(message='Los datos se perderán, desea continuar', title= 'Advertencia'):
        cursor.execute('DROP TABLE product')
    else:
        pass


def end_app():
    valor= messagebox.askquestion('Salir', '¿está seguro que desea salir de la aplicación?')
    if valor == "yes":
        root.destroy()

def clean_fields():
    codproduct.set("")
    description.set("")
    price.set("")
    total.set("")

def message():
    about= '''
    Aplicación de Escritorio
    Tecnology Python Tkinter
    '''
    messagebox.showinfo(title='Información', message=about)
## Metodos CRUD

def create():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    try:
        data= codproduct.get(), description.get(), price.get(), total.get()
        cursor.execute('INSERT INTO product VALUES(NULL,?,?,?,?)', (data))
        conection.commit()
    except:
        messagebox.showwarning('Advertencia', 'Ocurrió un error al crear el registro, verifique la conexión con la base de datos')
        pass
    clean_fields()
    show()

def show():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    register = tree.get_children()
    for element in register:
        tree.delete(element)

    try:
        cursor.execute('SELECT * FROM product')
        for row in cursor:
            tree.insert('',0,text=row[0], values= (row[1], row[2], row[3], row[4]))
    except:
        pass

## Table

tree = ttk.Treeview(height=10, columns = ('#0', '#1', '#2', '#3'))
tree.place (x=0, y=130)
tree.column('#0', width=50)
tree.heading('#0', text='Id', anchor= CENTER)
tree.heading('#1', text='Código Producto', anchor= CENTER)
tree.column('#1', width=100)
tree.heading('#2', text='Descripción', anchor= CENTER)
tree.column('#2', width=230)
tree.heading('#3', text='Precio', anchor= CENTER)
tree.column('#3', width=100)
tree.heading('#4', text='Total', anchor= CENTER)
tree.column('#4', width=150)

def select_on_click(event):
    item= tree.identify('item', event.x, event.y)
    id.set(tree.item(item,'text'))
    codproduct.set(tree.item(item,'values')[0])
    description.set(tree.item(item,'values')[1])
    price.set(tree.item(item,'values')[2])
    total.set(tree.item(item,'values')[3])

tree.bind('<Double-1>', select_on_click)


def update():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    try:
        data = codproduct.get(), description.get(), price.get(), total.get()
        cursor.execute('UPDATE user SET CODPRODUCT=?, DESCRIPTION=?, PRICE=?, TOTAL=? WHERE ID='+ id.get(), (data))
        conection.commit()
    except:
        messagebox.showwarning('Advertencia', 'Ocurrio un error al actualizar el registro')
        pass
    clean_fields()
    show()

def delete():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    try:
        if messagebox.askyesno(message='¿Quiere eliminar el registros?', title='Advertencia'):
            cursor.execute('DELETE FROM product WHERE ID='+ id.get())
            conection.commit()
    except:
        messagebox.showwarning('Advertencia','Ocurrio un error al tratar de eliminar el registro')
        pass
    clean_fields()
    show()

## Colocar widgets en la VISTA

# Menú
menubar= Menu(root)
menubasedat = Menu(menubar,tearoff=0)
menubasedat.add_command(label='Crear/Conectar Base de Datos', command=conection_bd)
menubasedat.add_command(label='Eliminar Base de Datos', command=delete_bd)
menubasedat.add_command(label='Salir', command=exit)
menubar.add_cascade(label='Inicio', menu=menubasedat)

help=Menu(menubar, tearoff=0)
help.add_command(label='Limpiar campos', command=clean_fields)
help.add_command(label= 'Acerca', command= message)
menubar.add_cascade(label='Ayuda', menu=help)

# Etiqueta y caja de texto

e1 = Entry(root, textvariable= id)

l2 = Label(root, text= 'Código :')
l2.place(x=50, y=10)
e2 = Entry(root, textvariable=codproduct, width=20)
e2.place(x=100, y=10)

l3= Label(root, text= 'Descripción :')
l3.place(x=50, y=40)
e3 = Entry(root, textvariable=description, width=50)
e3.place(x=125, y=40)


l5 = Label(root, text= 'Precio :')
l5.place(x=50, y=70)
e5 = Entry(root, textvariable=price, width=10)
e5.place(x=95, y=70)


l2 = Label(root, text= 'Total :')
l2.place(x=50, y=100)
e2 = Entry(root, textvariable=total, width=10)
e2.place(x=90, y=100)


# Botones

b1=Button(root, text='Registrar', command=create)
b1.place(x=360, y=90)

b2=Button(root, text='Mostrar Lista', bg= 'grey', command=show)
b2.place(x=500, y=90)


b3=Button(root, text='Eliminar', bg= 'red', command=delete)
b3.place(x=430, y=90)



root.config(menu=menubar)

root.mainloop()