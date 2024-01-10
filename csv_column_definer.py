import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd 
import os
import pandas as pd


# Создание главного окна
window = tk.Tk()
window.geometry("550x550")
window.title("Программа анализа столбцов .csv файлов")

# Запуск цикла mainloop 
window.mainloop()
