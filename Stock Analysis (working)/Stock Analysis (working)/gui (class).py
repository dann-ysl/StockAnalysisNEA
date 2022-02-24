from tkinter import *

class mainWindow:

    def __init__(self, master):
        self.master = master
        self.currentRow = 0

        self.label_1 = Label(self.master, text = "Screener").grid(row = 0, column = 0, columnspan=3)
        self.entryBox = Entry(self.master).grid(row = 1, column = 0)
        self.displayBtn = Button(self.master, text = "Display", command = self.displayScreener).grid(row = 1, column = 1)
        #self.clearBtn = Button(self.master, text = 'Clear', command = self.clearScreener).grid(row = 1, column = 2)

    def displayScreener(self):

        for i in range(len(stockArr)):

            r = 2 + self.currentRow
            self.stock = Button(self.master, text = stockArr[i][0]).grid(row = r, column = 0)
            self.image = Label(self.master, text = stockArr[i][1]).grid(row = r, column = 1)
            self.closePrice = Label(self.master, text = stockArr[i][2]).grid(row = r, column = 2)
            self.currentRow += 1

        print (self.grid_slaves())
    #def clearScreener(self):


stockArr = [["MSFT", "MSFTimg", 1023.32],["AAPL", "AAPLimg", 342.32],["TSLA","TSLAimg",420.45]]




###################################################################################
root = Tk()

root.title("Stock Analysis Assistant")
#root.geometry("500x500")

home = mainWindow(root)

root.mainloop()
###################################################################################