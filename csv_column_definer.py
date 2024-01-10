import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import filedialog as fd
import os
import pandas as pd
import re

# Функция определитель email
def is_email(value):
    return 1

# Функция определитель телефона
def is_phone(value):
    return 1


# Выборка столбца в список
def get_column(df, cnt_rows, column_ix):
    lst = []
    for i in range(cnt_rows):
        lst.append(df.iat[i,column_ix])
    return lst

# Функция для чтения .csv файла
def analze_csv(file_name):
    df = pd.read_csv(file_name, sep=';', dtype=str)
    cnt_rows = df.shape[0] # кол-во строк
    cnt_columns = df.shape[1] # кол-во столбцов
    results = []
    for col_num in range(cnt_columns):
        email_count = 0
        phone_count = 0
        # Получаем список из стобца
        cur_col = get_column(df, cnt_rows, col_num)
        # Перебираем все значения списка
        for item in cur_col:
            if is_email(item): 
                email_count+=1 
                continue
            if is_phone(item): 
                phone_count+=1 
                continue
            column_type = "Не удалось определить"
        
        if email_count > phone_count:
            column_type = "Email"
        elif phone_count > email_count:
            column_type = "Телефон"
        results.append((cur_col[0], column_type, max(email_count, phone_count)))
    return results

# Обработчик для кнопки
def process_button():
    file_name = fd.askopenfilename(initialdir=os.getcwd())
    results = analze_csv(file_name)
    output_text.delete('1.0', tk.END)
    for col, col_type, count in results:
        output_text.insert(tk.END, f"Столбец {col}: Предполагаемый тип - {col_type}, Количество совпадений - {count}\n")

# Создание графического интерфейса
window = tk.Tk()
window.geometry("840x500")
window.title("Программа анализа столбцов .csv файлов")

output_text = st(height=25, width=100)
output_text.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(window, text="Открыть CSV", command=process_button)
button.grid(row=2, column=0)

window.mainloop()
