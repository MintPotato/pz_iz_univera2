import tkinter as tk
import tkinter.ttk as ttk
from math import pi
from tkinter import Canvas


class Circle:
    def __init__(self, cm=1):
        self.r = cm * 38  # 38 - kоличество пикселей в одном сантиметре как утверждает какой-то сайт

    def find_surface(self):
        return pi * (self.r // 38) ** 2


class Square:
    def __init__(self, cm=1):
        self.side = cm * 38

    def find_surface(self):
        return (self.side // 38) ** 2


class Polygon:
    def __init__(self, a_cm=1, b_cm=2):
        self.a_side = a_cm * 38
        self.b_side = b_cm * 38

    def find_surface(self):
        return (self.a_side * self.b_side) // 38 ** 2


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('100x200')

        self.lbl = ttk.Label(self, text='Chose your hero').grid(row=0, pady=10)
        self.btn_c = ttk.Button(self, text='Circle', command=self.c_chosen).grid(row=1, pady=6)
        self.btn_s = ttk.Button(self, text='Square', command=self.s_chosen).grid(row=2, pady=6)
        self.btn_p = ttk.Button(self, text='Polygon', command=self.p_chosen).grid(row=3, pady=6)

    def c_chosen(self):
        DrawWindow('c')

    def s_chosen(self):
        DrawWindow('s')

    def p_chosen(self):
        DrawWindow('p')


class DrawWindow(tk.Toplevel):
    def __init__(self, figure):
        super().__init__()
        self.geometry('200x200')
        self.lbl = ttk.Label(self, text='')
        self.lbl.pack()  # .place(x=0, y=0, height=20)
        self.canvas = Canvas(self)

        if figure == 'c':
            self.draw_circle()
        elif figure == 's':
            self.draw_square()
        else:
            self.draw_polygon()

    def draw_circle(self):
        circle = Circle()
        self.canvas.create_oval(2, 10, circle.r * 2, 10 + circle.r * 2, fill='#1f1')
        self.canvas.pack()
        self.lbl.config(text=f'Площадь фигуры равна: {circle.find_surface()}')

    def draw_square(self):
        square = Square()
        self.canvas.create_rectangle(2, 10, square.side, 10 + square.side, fill='#1f1')
        self.lbl.config(text=f'Площадь фигуры равна: {square.find_surface()}')
        self.canvas.pack()

    def draw_polygon(self):
        polygon = Polygon()
        self.canvas.create_rectangle(2, 10, polygon.a_side, 10 + polygon.b_side, fill='#1f1')
        self.lbl.config(text=f'Площадь фигуры равна: {polygon.find_surface()}')
        self.canvas.pack()


if __name__ == '__main__':
    start = MainWindow()
    start.mainloop()
