import tkinter as tk
import tkinter.ttk as ttk
from random import randint


class GuessWindow(tk.Tk):
    def __init__(self, number, tries):
        super().__init__()
        self.geometry('350x150')

        self.number = number
        self.tries = tries

        vcmd = (self.register(self.validate), '%P')

        lbl = ttk.Label(self, text='Введите Вашу догадку').grid(row=0, column=1, padx=5, pady=5)
        self.ent = ttk.Entry(self, validate='key', validatecommand=vcmd)
        self.ent.grid(row=1, column=1, padx=5, pady=5)

        btn_vvod = ttk.Button(self, text='Ввод значения', command=self.input_number).grid(row=2, column=0,  pady=5)
        btn_restart = ttk.Button(self, text='Начать заново', command=self.restart).grid(row=2, column=1,  pady=5)
        btn_tries = ttk.Button(self, text='Количество попыток', command=self.num_of_tries).grid(row=2, column=2, pady=5)

        self.hint_lbl = ttk.Label(self, text='')
        self.hint_lbl.grid(row=3, column=1)
        self.mainloop()

    def validate(self, string):
        if string == '':
            return True

        try:
            string = int(string)
            if 0 <= string <= 100:
                return True
            else:
                return False
        except:
            return False

    def restart(self):
        self.destroy()
        GuessGame()

    def input_number(self):
        num = int(self.ent.get())

        self.tries += 1

        if num == self.number:
            print('pobeda', f'Kolvo popitok {self.tries}', sep='\n')
            self.destroy()
        elif num < self.number:
            self.hint_lbl.config(text='Искомое число больше')
        else:
            self.hint_lbl.config(text='Искомое число меньше')

    def num_of_tries(self):
        print(f'Kolvo popitok: {self.tries}')



class GuessGame:
    def __init__(self):
        self.number = randint(0, 101)
        self.tries = 0
        print(self.number)

        GuessWindow(self.number, self.tries)


if __name__ == '__main__':
    GuessGame()
