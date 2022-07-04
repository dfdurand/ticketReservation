import sqlite3


class Connect:
    def __init__(self):
        self.bd = sqlite3.connect("reservation.db")
        self.bd.row_factory = sqlite3.Row
        self.bd.execute("create table if not exists Ticket(ID integer primary key autoincrement, name text, gender text, comment text)")
        self.bd.commit()

    def add(self, name, gender, comment):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute("insert into  Ticket(name ,gender, comment) values(?,?,?)", (str(name), gender, comment))
        self.bd.commit()
        return "add done"

    def ListTicket(self):
        cursor = self.bd.execute("SELECT * FROM Ticket")
        return cursor


    def read(self):
        cursor = self.bd.execute("SELECT * FROM Ticket ")
        for row in cursor:
            print("nom:{}, gender: {}, comment: {}".format(row["name"], row["gender"], row["comment"]))
        return "Données enregistrées"


    def delete(self, ID):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute("delete from Ticket where ID = '{}'".format(ID))
        self.bd.commit()
        return "supprimer"

    def modify(self, comment, ID):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute("update Ticket set comment =? where ID=?", (comment, ID))
        self.bd.commit()
        return "modifier"


