import tkinter as tk
import datetime as dt
import pandas_datareader.data as web
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def plot():

    today = dt.datetime.today() #assigning today's date
    stock = stockEntry.get() #getting the value from the stockEntry text box
    start = dateEntry.get() #getting the value from the dateEntry text box

    fig = Figure(figsize=(5,5), dpi = 100) #initialising the graph

    df = web.DataReader(stock, "yahoo", start, today) #calling the api for stock's data

    colour = "" #colour of the graph

    dfClose = df["Close"] #extracting one column from the 2D dataframe, essentially returning a 1D array

    if dfClose[0] > dfClose[dfClose.size - 1]: #checking if first close < last close or vice versa
        colour = "red" #red if first close price > last close price
    else:
        colour = "lime" #lime if first close price < last close price

    plot1 = fig.add_subplot(111)
    plot1.plot(dfClose, color = colour) #plots close prices with corresponding colour

    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()

window.title("Stock Analysis")
window.geometry("500x500")

label1 = tk.Label(window, text = "Enter Stock")
label1.pack()
stockEntry = tk.Entry(window)
stockEntry.pack()

label2 = tk.Label(window, text = "Enter Start Date")
label2.pack()
dateEntry = tk.Entry(window)
dateEntry.pack()

plot_button = tk.Button(window, command = plot, height = 2, width = 10, text = "Plot")
plot_button.pack()

delete_button = tk.Button(window, height = 2, width = 10, text = "Delete")
delete_button.pack()

window.mainloop()


