# Калькулятор

# Импортируем модуль tkinter (для удобства написания назначаем сокращение tk)
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from math import sqrt

# Создаем главное окно
base = tk.Tk()

# Устанавливаем заголовок окна
base.title('My calculator')

# Назначаем размеры окна и начальные координаты
base.geometry('312x379+600+200')

# Меняем иконку заголовка
# base.iconbitmap('pictures/icon.ico')

# Назначаем цвет фона
base.configure(bg='#F6F6F6')

# Создаем поле счета
num = tk.Entry(base, font=('Calibri', 26), justify='right', bg='#F6F6F6', bd=0, fg='#303030', width=17)
num.insert(0, '0')
num.grid(row=0, column=0, columnspan=4, padx=2, pady=20)


# Добавляем переменную в поле счета
def add_digit(digit):
    val = num.get()
    if num['fg'] == 'green':
        val = '0'
    num.config(fg='#303030')
    if val[0] == '0' and len(val) == 1:
        val = val[1:]  # удаляем начальное "0" из поля вывода
    elif len(val) == 15:
        val = 'Нельзя вводить больше 15-ти цифр'
    num.delete(0, tk.END)
    num.insert(0, val + digit)


# Добавляем точку
def add_point(point):
    val = num.get()
    if num['fg'] == 'green':
        val = '0'
    num.config(fg='#303030')
    if val[-1] == '.':
        val = val[:-1]
    elif val[-1] in '+-*/':
        val = val + '0'
    num.delete(0, tk.END)
    num.insert(0, val + point)

    # if val[:ind()].count('.') == 1:
    # print(val)
    # num.delete(0, tk.END)
    # num.insert(0, val)


# Удаляем последнюю цифру
def del_digit():
    val = num.get()
    val = val[:-1]
    if len(val) == 0:
        val = '0'
    num.delete(0, tk.END)
    num.insert(0, val)


# Удаляем последнее значение
def del_last_val():
    val = num.get()
    val = val[:ind() + 1]
    if val[-2] == '(':
        val = val[:-2]
    num.delete(0, tk.END)
    num.insert(0, val)


# Удаляем все
def clean_all():
    val = '0'
    num.delete(0, tk.END)
    num.insert(0, val)


# Добавляем знак операции
def add_operation(operation):
    val = num.get()
    num.config(fg='#303030')
    if val[-1] in '+-*/':
        val = val[:-1]
    num.delete(0, tk.END)
    num.insert(0, val + operation)


# Добавляем знак "-"
def add_minus(minus):
    val = num.get()
    num.config(fg='#303030')
    if val[-1] == '-':
        val = val[:-1]
        # if val[0] == '-':
        # val = val[1:]
        num.delete(0, tk.END)
        num.insert(0, val)
    else:
        val_1 = val[:ind() + 1]
        val_2 = minus + val[ind() + 1:]
        num.delete(0, tk.END)
        val = f'{val_1}({val_2})'
        num.insert(0, val)
    if val[ind() - 3:ind() + 1] == '(-(-':
        val_1 = val[:ind() - 3]
        val_2 = val[ind() + 1:-2]
        num.delete(0, tk.END)
        val = val_1 + val_2
        num.insert(0, val)
    elif val[-1] == '.':
        pass


# Находим индекс последнего знака операции
def ind():
    val = num.get()
    ind_1 = val.rfind('+')
    ind_2 = val.rfind('-')
    ind_3 = val.rfind('*')
    ind_4 = val.rfind('/')
    return max(ind_1, ind_2, ind_3, ind_4)


# Считаем (+-*/)
def calc():
    val = num.get()
    if val[-1] in '+-*/':
        val = val + val[:-1]
    num.delete(0, tk.END)
    val = round(eval(val), 10)
    if type(val) is float and (val - int(val) == 0):
        val = int(val)
    num.insert(0, val)
    num.config(fg='green')


# Процент
def percent():
    val = num.get()
    val_1 = val[:ind()]
    val_2 = val[ind() + 1:]
    val_ind = val[:ind() + 1]
    val_2 = float(val_2) / 100
    val_2 = str(eval(val_1) * val_2)
    val = eval(val_ind + val_2)
    if type(val) is float and (val - int(val) == 0):
        val = int(val)
    num.delete(0, tk.END)
    num.insert(0, val)
    num.config(fg='green')


# Квадрат
def square():
    val = num.get()
    val_1 = val[:ind() + 1]
    val_2 = val[ind() + 1:]
    val_2 = float(val_2) ** 2
    if type(val_2) is float and (val_2 - int(val_2) == 0):
        val_2 = int(val_2)
    val = val_1 + str(val_2)
    num.delete(0, tk.END)
    num.insert(0, val)
    num.config(fg='green')


# Корень квадратный
def root():
    val = num.get()
    val_1 = val[:ind() + 1]
    val_2 = val[ind() + 1:]
    val_2 = sqrt(float(val_2))
    if type(val_2) is float and (val_2 - int(val_2) == 0):
        val_2 = int(val_2)
    val = val_1 + str(val_2)
    num.delete(0, tk.END)
    num.insert(0, val)
    num.config(fg='green')


# Обратная дробь
def recip_fract():
    val = num.get()
    val_1 = val[:ind() + 1]
    val_2 = val[ind() + 1:]
    val_2 = 1 / float(val_2)
    if type(val_2) is float and (val_2 - int(val_2) == 0):
        val_2 = int(val_2)
    val = val_1 + str(val_2)
    num.delete(0, tk.END)
    num.insert(0, val)
    num.config(fg='green')


# Создаем класс наследник, чтобы задать параметры сразу для всех кнопок
class MyButton(tk.Button):
    def __init__(self, master=base, **kwargs):
        super().__init__(master, kwargs)
        self.config(relief='solid', borderwidth=0, activebackground='#E0E0E0', font=('Microsoft JhengHei UI', 13),
                    width=5)
        self.grid(padx=2, pady=2, ipady=5, sticky='ew')


# Создаем кнопки цифр
def btn_d(digit):
    return MyButton(text=digit, bg='white', fg='#404040', command=lambda: add_digit(digit))


# Создаем кнопку точки
def btn_p(point):
    return MyButton(text=point, bg='#E0E0E0', fg='#404040', command=lambda: add_point(point))


# Создаем кнопки операций
def btn_op(operation):
    return MyButton(text=operation, bg='#E9E9E9', fg='#003366', command=lambda: add_operation(operation))


# Создаем кнопку "+/-"
def btn_p_m(minus):
    return MyButton(text='+/-', bg='#E0E0E0', fg='#404040', command=lambda: add_minus(minus))


# Создаем кнопку "="
def btn_eq(operation):
    return MyButton(text=operation, bg='#9999FF', command=calc)


# Создаем кнопку "BS"
def btn_BS(bs):
    return MyButton(text=bs, bg='#E0E0E0', fg='#404040', command=del_digit)


# Создаем кнопку "C (clean all)"
def btn_C(c):
    return MyButton(text=c, bg='#E0E0E0', fg='#CC0000', command=clean_all)


# Создаем кнопку CE:
def btn_CE(ce):
    return MyButton(text=ce, fg='#404040', bg='#E0E0E0', command=del_last_val)


def btn_percent():
    return MyButton(text='%', bg='#E9E9E9', fg='#003366', command=percent)


def btn_un_fr():
    return MyButton(text='1/x', bg='#E9E9E9', fg='#003366', command=recip_fract)


def btn_sq():
    return MyButton(text='x\u00B2', bg='#E9E9E9', fg='#003366', command=square)


def btn_root():
    return MyButton(text='\u221Ax', bg='#E9E9E9', fg='#003366', command=root)


# Размещаем кнопки
btn_d('1').grid(row=5, column=0)
btn_d('2').grid(row=5, column=1)
btn_d('3').grid(row=5, column=2)
btn_d('4').grid(row=4, column=0)
btn_d('5').grid(row=4, column=1)
btn_d('6').grid(row=4, column=2)
btn_d('7').grid(row=3, column=0)
btn_d('8').grid(row=3, column=1)
btn_d('9').grid(row=3, column=2)
btn_d('0').grid(row=6, column=1)

btn_p('.').grid(row=6, column=2)

btn_op('+').grid(row=5, column=3)
btn_op('-').grid(row=4, column=3)
btn_op('*').grid(row=3, column=3)
btn_op('/').grid(row=2, column=3)

btn_percent().grid(row=1, column=0)
btn_un_fr().grid(row=2, column=0)
btn_sq().grid(row=2, column=1)
btn_root().grid(row=2, column=2)

btn_eq('=').grid(row=6, column=3)

btn_BS('\u2190').grid(row=1, column=3)

btn_C('C').grid(row=1, column=1)

btn_p_m('-').grid(row=6, column=0)

btn_CE('CE').grid(row=1, column=2)

base.mainloop()
