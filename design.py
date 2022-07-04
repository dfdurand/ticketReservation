from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import Connect
from list_reservation import List

save = Connect()

window = Tk()
window.title("TICKET DE RESERVATION")
window.configure(background="#e1d8b2")
style= ttk.Style()
style.theme_use("classic")
style.configure("Tlabel", background="#e1d8b2")
style.configure("Tbutton", background="#e1d8b2")
style.configure("TRadiobutton", background="#e1d8b2")

ttk.Label(window, text="Username :").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(window, text="gender :").grid(row=1, column=0, padx=5, pady=5)
ttk.Label(window, text="comment:").grid(row=3, column=0, padx=5, pady=5)

name = ttk.Entry(window, width=40, font=("Arial", 15))
name.grid(row=0, column=1)
hash = Text(window, width=40, height=10, font=("Arial", 15))
hash.grid(row=3, column=1)

rbVar = StringVar()
rbVar.set("male")
rb1 = ttk.Radiobutton(window, text="male", variable=rbVar, value="male").grid(row=1, column=1)

rb2 = ttk.Radiobutton(window, text="female", variable=rbVar, value="femelle").grid(row=1, column=2)


btn = ttk.Button(window, text="SUBMIT")
btn.grid(row=4, column=4)
btn1 = ttk.Button(window, text="LIST")
btn1.grid(row=4, column=3)

def clic():
    print("username: ", name.get())
    print("gender : ", rbVar.get())
    print("texte : ", hash.get(1.0, END))
    msg = save.add(name.get(), rbVar.get(), hash.get(1.0, END))
    messagebox.showinfo(title="ENREGISTREMENT", message=msg)
    name.delete(0, END)
    hash.delete(1.0, END)
def btn_list():
    list_des_tickets = List()




btn.config(command= clic)
btn1.config(command= btn_list)

window.mainloop()

