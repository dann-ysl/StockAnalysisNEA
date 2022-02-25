import tkinter as tk
import datetime as dt
import pandas_datareader.data as web
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()

frame = tk.Frame(root, width=500, bg="#000000").pack()
label = tk.Label(frame, text="hello")
label.pack(side="right")


root.mainloop()

