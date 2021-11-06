from tkinter import *

class Application (Frame):

  def texto(self):
    self.msg.config(text="não é aqui")

  def __init__(self,master=None):
    Frame.__init__(self, master)
    self.msg = Label(self)
    self.msg.pack()
    self.txt=Entry(self)
    self.txt.pack()
    self.bye = Button (self, text="Bye", command=self.texto)
    self.bye.pack()
    self.pack()

app = Application()
app.master.title("Exemplo")
app.master.geometry("200x200+200+200")
mainloop()
