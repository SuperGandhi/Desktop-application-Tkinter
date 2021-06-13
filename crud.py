#Importando librerias
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from nltk import tree


#Desarrollo del GUI

root = Tk()
root.title('Ferreteria El Tornillo Feliz')
root.geometry("600x350")

dni= StringVar()
name =StringVar()
last_name = StringVar()
address = StringVar()
phone = StringVar()

id_product = StringVar()
description = StringVar()
amount = StringVar()
price = StringVar()
total = StringVar()

def conection_bd():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()

    try:
        cursor.execute('''
            CREATE TABLE user(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DNI VARCHAR(60) NOT NULL,
                NAME VARCHAR(100) NOT NULL,
                LAST NAME VARCHAR(100) NOT NULL,
                ADDRES VARCHAR(100) NOT NULL,
                PHONE VARCHAR(30) NOT NULL,
            )

            CREATE TABLE product(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DESCRIPTION VARCHAR(100) NOT NULL,
                AMOUNT INT NOT NULL,
                PRICE VARCHAR(10) NOT NULL,
                TOTAL VARCHAR(10) NOT NULL,
            )
            ''')

        messagebox.showinfo("CONEXION", "Base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

def delete_bd():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    if messagebox.askyesno(message='Los datos se perderán, desea continuar', title= 'Advertencia'):
        cursor.execute('DROP TABLE user')
    else:
        pass

def end_app():
    valor= messagebox.askquestion('Salir', '¿está seguro que desea salir de la aplicación?')
    if valor == "yes":
        root.destroy()

def clean_fields():
    dni.set("")
    name.set("")
    last_name.set("")
    address.set("")
    phone.set("")
    id_product.set("")
    description.set("")
    amount.set("")
    price.set("")
    total.set("")

def message():
    about= '''
    Aplicación CRUD
    Versión 1.0
    Tecnology Python Tkinter
    '''

## Metodos CRUD

def create():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    try:
        data= id_product.get(), amount.get(), price.get()
        cursor.execute('INSERT INTO user VALUES(NULL,?,?,?)', (data))
        conection.commit()
    except:
        messagebox.showwarning('Advertencia', 'Ocurrió un error al crar el registro, verifique la conexión con la base de datos')
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
            tree.insert('',0,text=row[0], values= (row[1], row[2], row[3]))
    except:
        pass

## Table

tree = ttk.Treeview(height=10, columns = ('#0', '#1', '#2'))
tree.place (x=0, y=130)
tree.column('#0', width=100)
tree.heading('#0', text='Código', anchor= CENTER)
tree.heading('#1', text='Descripción', anchor= CENTER)
tree.heading('#2', text='Precio', anchor= CENTER)
tree.column('#3', width=100)
tree.heading('#3', text='Total', anchor= CENTER)
#tree.heading('#5', text='Total', anchor= CENTER)


def update():
    conection=sqlite3.connect('base')
    cursor=conection.cursor()
    try:
        data = id_product.get(), amount.get(), price.get()
        cursor.execute('UPDATE product SET CODIGO=?, CANTIDAD=?, PRECIO=? WHERE ID='+ id_product.get(), (data))
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
            cursor.execute('DELETE FROM product WHERE ID='+ id_product.get())
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

l2 = Label(root, text= 'Dni')
l2.place(x=50, y=10)
e2 = Entry(root, textvariable=dni, width=10)
e2.place(x=100, y=10)

l3= Label(root, text= 'Nombre')
l3.place(x=50, y=40)
e3 = Entry(root, textvariable=name, width=50)
e3.place(x=100, y=40)

l4 = Label(root, text= 'Apellidos')
l4.place(x=210, y=40)
e4 = Entry(root, textvariable=last_name, width=30)
e4.place(x=265, y=40)


l5 = Label(root, text= 'Dirección')
l5.place(x=50, y=70)
e5 = Entry(root, textvariable=address, width=50)
e5.place(x=105, y=70)


l2 = Label(root, text= 'Teléfono')
l2.place(x=50, y=100)
e2 = Entry(root, textvariable=phone, width=50)
e2.place(x=105, y=100)


# Botones 

b1=Button(root, text='Registrar', command=create)
b1.place(x=450, y=90)
# b2=Button(root, text='Modificar Registro', command=update)
# b2.place(x=100 , y=90)
# b3=Button(root, text='Mostrar Lista', command=show)
# b3.place(x=100, y=90)
b4=Button(root, text='Eliminar', bg= 'red', command=delete)
b4.place(x=530, y=90)
# b5=Button(root, text='Crear Registro', command=create)
# b5.place(x=50 , y=90)


root.config(menu=menubar)

root.mainloop()






