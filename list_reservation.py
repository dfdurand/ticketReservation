from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import Connect



class List:
    def __init__(self):
        self.db = Connect()
        self.root = Tk()
        tv = ttk.Treeview(self.root)
        tv.pack()
        tv.heading("#0", text="ID")
        tv.configure(column=("name", "gender", "comment"))
        tv.heading("name", text="Username")
        tv.heading("gender", text="sexe")
        tv.heading("comment", text="Commentaire")
        cursor = self.db.ListTicket()
        for row in cursor:
            tv.insert("", "end", "#{}".format(row["ID"]), text=row["ID"])
            tv.set("#{}".format(row["ID"]), "name", row["name"])
            tv.set("#{}".format(row["ID"]), "gender", row["gender"])
            tv.set("#{}".format(row["ID"]), "comment", row["comment"])
            #print("ID:{}, gender: {}, comment: {}".format(row["ID"], row["gender"], row["name"]))

        self.root.mainloop()