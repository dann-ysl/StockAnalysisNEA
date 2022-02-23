from tkinter import *

currentRow = 0
def displayScreener():

    for i in range(len(stockArr)):
        global currentRow
        r = 2 + currentRow
        stock = Button(root, text = stockArr[i][0]).grid(row = r, column = 0)
        image = Label(root, text = stockArr[i][1]).grid(row = r, column = 1)
        closePrice = Label(root, text = stockArr[i][2]).grid(row = r, column = 2)
        currentRow += 1
    
def clearScreener():
    for item in root.grid_slaves():
        current = int(item.grid_info()["row"])
        if current > 1:
            item.grid_forget()


stockArr = [["MSFT", "MSFTimg", 1023.32],["AAPL", "AAPLimg", 342.32],["TSLA","TSLAimg",420.45]]




###################################################################################
root = Tk()

root.title("Stock Analysis Assistant")
#root.geometry("500x500")


label_1 = Label(root, text = "Screener").grid(row = 0, column = 0, columnspan=3)
entryBox = Entry(root).grid(row = 1, column = 0)
displayBtn = Button(root, text = "Display", command = displayScreener).grid(row = 1, column = 1)
clearBtn = Button(root, text = 'Clear', command = clearScreener).grid(row = 1, column = 2)
first = len(root.grid_slaves())

#home = mainWindow(root)

root.mainloop()
###################################################################################