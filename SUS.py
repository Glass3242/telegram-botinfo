import tkinter
from tkinter import messagebox
from tkinter import ttk
def start_up():
    import json
    with open('ffsfs.json',"r",encoding='utf-8') as f:
        data=json.load(f)
        return data

data=start_up()
print(data)

window=tkinter.Tk()
window.title('Приложение')
window.geometry('300x300')

tkinter.Label(text='Логин:',font=('Arial',18)).pack()
entry=tkinter.Entry()
entry.pack()
def func():
    if  (entry.get() in data['users'].keys() and entry1.get()==data['users'][entry.get()]):
        return messagebox.showinfo('Warning','Вы успешно вошли')
    else:
        return messagebox.showinfo('Warning','Вы ввели неверный логин или пароль')

tkinter.Label(text='Пароль',font=('Arial',18)).pack()
entry1=tkinter.Entry()
entry1.pack()

button=tkinter.Button(text='Войти',command=func).pack()


window.mainloop()
