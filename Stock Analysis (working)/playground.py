from tkinter import *

ticker = ["AAPL","MSFT","TSLA"]

class mainWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        e = topFrame(self)
        e.grid(row = 0)
        f = middleFrame(self, 5)
        f.grid(row = 1)
        print (f.value)

class topFrame(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.label = Label(self, text="hello")
        self.label.pack()

class middleFrame(Frame):
    def __init__(self, master, value, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.value = value
        self.label = Label(self, text="yo")
        self.label.pack()
        self.addRow()

    def addRow(self):
        global ticker
        for entry in ticker:
            buttonWindow(self, entry).pack()

class buttonWindow(Button):
    def __init__(self, master, name, *args, **kwargs):
        Button.__init__(self, master, *args, **kwargs)
        self.config(text = name, command=lambda: newWindow(self, name))
        #pack in parent

class newWindow(Toplevel):
    def __init__(self, master, name):
        Toplevel.__init__(self, master)
        self.title(name)
        self.label = Label(self, text=name)
        self.label.pack()
        self.quitBtn = Button(self, text="quit", command=self.destroy)
        self.quitBtn.pack()

root = Tk()
home = mainWindow(root)
home.pack()
root.mainloop()
