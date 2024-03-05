from tkinter import*

root = Tk()
root.title("Calculadora de edad en años a horas")
root.geometry("400x600")
root.config(bg = "cadetblue")

label_1 = Label(root,text="Calculadora de edad en años a horas")
label_1.config(bg="lightgreen", fg="black", font=("Verdana",14))

label_2 = Label(root,text="Ingresa tu edad en años: ")
label_2.config(bg="pink", fg="black",font=("Verdana",10))

entrada_1 = Entry(root)

def calcular():
    edad = int(entrada_1.get())
    print(edad)
    horas = int(edad*365*24)
    print(horas)
    label_4["text"] = horas
    
boton_1 = Button(root,text="Calcular",bg="red",width=10,height=2,fg="white",command=calcular)

label_3 = Label(root,text="Tu edad aproximada en horas es:")
label_3.config(bg="peru", fg="black",font=("Verdana",16))

label_4 = Label(root)
label_4.config(fg="black")



label_1.pack()
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)

label_2.pack()
label_2.place(relx=0.5,rely=0.2,anchor=CENTER)

entrada_1.pack()
entrada_1.place(relx=0.5,rely=0.3,anchor=CENTER)

boton_1.pack()
boton_1.place(relx=0.5,rely=0.4,anchor=CENTER)

label_3.pack()
label_3.place(relx=0.5,rely=0.6,anchor=CENTER)

label_4.pack()
label_4.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()