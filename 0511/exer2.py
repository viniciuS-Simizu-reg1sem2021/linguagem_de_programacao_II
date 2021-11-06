from tkinter import *

class Application(Frame):

  def muda_texto(self):
    self.msg.config(text="aqui")

  def __init__ (self, master=None):
    Frame.__init__(self, master)
    self.msg = Label(self, text="Nome: ")
    self.msg.pack()
    self.txt = Entry(self)
    self.txt.pack()
    self.msg = Label(self, text="Endereço: ")
    self.msg.pack()
    self.txt = Entry(self)
    self.txt.pack()
    self.msg = Label(self, text="Telefone: ")
    self.msg.pack()
    self.txt = Entry(self)
    self.txt.pack()
    self.bye = Button(self, text="incluir")
    self.bye.pack()
    self.bye = Button(self, text="Fechar", command=self.muda_texto)
    self.bye.pack()
    self.pack()

app = Application()
app.master.title("AGENDA")
app.master.geometry("600x200")
mainloop()
