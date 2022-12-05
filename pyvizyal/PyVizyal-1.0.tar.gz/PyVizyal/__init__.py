from tkinter import *
from PIL import Image, ImageTk
import pygame
from googletrans import Translator
from tkinter import ttk
import time

Name = Tk()
def title():
    Name.title(input("Name: "))
def size():
    Name.geometry(input("width, heigth: "))
def label():
    text = input("Text: ")
    color = input("Color: ")
    nax_x = input("Нахождение по x: ")
    nax_y = input("Нахождение по y: ")
    label = Label(Name, text=text, background=color)
    label.pack()
    label.place(x=nax_x, y=nax_y)
def canvas():
    canvas = Canvas(Name, width=size(), height=size())
    canvas.pack()
def frame():
    frame2 = input("Расположение по x: ")
    frame3 = input("Расположение по y: ")
    frame1 = Frame(Name)
    frame1.pack()
    frame1.place(x=frame2, y=frame3)
def trans():
    time.sleep(1000000)
    def translate():
        for launguage, suffix in languages.items():
            if comboTwo.get() == launguage:
                text = t_input.get('1.0', END)
                translation = translator.translate(text, dest=suffix)
                t_output.delete('1.0', END)
                t_output.insert('1.0', translation.text)


    tk = Tk()
    tk.geometry('500x350')
    tk.title('Переводчик')
    tk.resizable(False, False)
    tk['bg'] = 'black'
    translator = Translator()

    languages = {'Русский': 'ru', 'Английский': 'en', 'Француский': 'fr'}

    header_frame = Frame(tk, bg='black')
    header_frame.pack(fill=X)

    header_frame.grid_columnconfigure(0, weight=1)
    header_frame.grid_columnconfigure(1, weight=1)
    header_frame.grid_columnconfigure(2, weight=1)

    comboOne = ttk.Combobox(header_frame,
                            values=[lang for lang in languages], state='readonly')
    comboOne.current(0)
    comboOne.grid(row=0, column=0)

    label = Label(header_frame, fg='white', bg='black', font='Arial 17 bold', text='->')
    label.grid(row=0, column=1)

    comboTwo = ttk.Combobox(header_frame,
                            values=[lang for lang in languages], state='readonly')
    comboTwo.current(1)
    comboTwo.grid(row=0, column=2)

    t_input = Text(tk, width=35, height=5, font='Arial 12 bold')
    t_input.pack(pady=20)

    btn = Button(tk, width=45, text='Перевести', command=translate)
    btn.pack()

    t_output = Text(tk, width=35, height=5, font='Arial 12 bold')
    t_output.pack(pady=20)

    tk.mainloop()

def button():
    text = input("Text: ")
    color = input("Color: ")
    nax_x = input("Нахождение по x: ")
    nax_y = input("Нахождение по y: ")
    size_x = input("Ширина: ")
    size_y = input("Высота: ")
    button = Button(Name, text=text, background=color)
    button.pack()
    button.place(x=nax_x, y=nax_y, width=size_x, height=size_y)
def musical():
    myz2 = input("Путь или Название: ")
    pygame.mixer.init()
    pygame.mixer.music.load(myz2)
    pygame.mixer.music.play()
def command():
    com = input("Exit:  ")
    if com == "Yes":
        exit()
    if com == "No":
        com = input("Window:")
    if com == "Yes":
        Name1 = Tk()
        Name1.title(input("Name: "))
        Name1.geometry(input("width, heigth: "))
        button = input("Button: ")
        if button == "Yes":
            text = input("Text: ")
            color = input("Color: ")
            nax_x = input("Нахождение по x: ")
            nax_y = input("Нахождение по y:")
            size_x = input("Ширина: ")
            size_y = input("Высота: ")
            button1 = Button(Name1, text=text, background=color)
            button1.pack()
            button1.place(x=nax_x, y=nax_y, width=size_x, height=size_y)
            label = input("Label: ")
            if label == "Yes":
               text1 = input("Text: ")
               color1 = input("Color: ")
               nax_x1 = input("Нахождение по x: ")
               nax_y1 = input("Нахождение по y:")
               label1 = Label(Name1, text=text1, background=color1)
               label1.pack()
               label1.place(x=nax_x1, y=nax_y1)
               myz = input("Muzical: ")
               if myz == "Yes":
                   myz2 = input("Name Muzical: ")
                   pygame.mixer.init()
                   pygame.mixer.music.load(myz2)
                   pygame.mixer.music.play()
                   canvas1 = input("Canvas color: ")
                   if canvas1 == "Yes":
                      canvas2 = input("Color: ")
                      canvas = Canvas(Name, width=size(), height=size(), background=canvas2)
                      canvas.pack()

def button_command():
    text = input("Text: ")
    color = input("Color: ")
    nax_x = input("Нахождение по x: ")
    nax_y = input("Нахождение по y:")
    size_x = input("Ширина: ")
    size_y = input("Высота: ")
    com = input("Command: ")
    button = Button(Name, text=text, background=color, command=command)
    button.pack()
    button.place(x=nax_x, y=nax_y, width=size_x, height=size_y)
def run():
    Name.mainloop()

