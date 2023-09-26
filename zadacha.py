#Задание для Костяна-коллеги : Сделать три кнопки и расположить их в самом низу,
# у кнопок должен быть какой-либо эффект, либо кнопка меняется либо что-то выходит на экран

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x300+700+200')

def red():
    styles = ttk.Style()
    styles.configure("BW.TLabel", background="red")
    btns['style'] = "BW.TLabel"

btns = ttk.Button(text='Покраска в красный', command=red) #Кнопкав нижнем левом углу
btns.place(relx=.0, rely=1, anchor='sw')

def purple():
    styles = ttk.Style()
    styles.configure("BW.TLabel", background="purple")
    btn['style'] = "BW.TLabel"

btn = ttk.Button(text='Покраска в фиолетовый', command=purple) #Кнопка внизу центра
btn.place(relx=0.5, rely=1, anchor='s')

def black():
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="white", background="black")
    buttonTTK['style'] = "BW.TLabel"

buttonTTK = ttk.Button(text="Покраска в чёрный", command=black) #Кнопка в правом нижнем углу
buttonTTK.place(relx=1, rely=1, anchor='se')

root.mainloop()