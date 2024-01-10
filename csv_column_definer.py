import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import filedialog as fd
import os
import pandas as pd
import re

# Обработчик для кнопки
def process_button():
    file_name = fd.askopenfilename(initialdir=os.getcwd())

# Создание графического интерфейса
window = tk.Tk()
window.geometry("840x500")
window.title("Программа анализа столбцов .csv файлов")

output_text = st(height=25, width=100)
output_text.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(window, text="Открыть CSV", command=process_button)
button.grid(row=2, column=0)

window.mainloop()
