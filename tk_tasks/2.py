import tkinter as tk
import tkinter.ttk as ttk


class MakingWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.spis = []

        lbl = ttk.Label(self, text='Введите желаемые элементы списка (через пробел)').grid(row=0)
        self.ent = ttk.Entry(self)
        self.ent.grid(row=1)

        self.approv_btn = ttk.Button(self, text='Подтвердить', command=self.add_to_spis).grid(row=3)

    def add_to_spis(self):
        spis = self.ent.get().split()

        self.spis.extend(spis)
        self.destroy()


class LengthWindow(tk.Toplevel):
    def __init__(self, spis):
        super().__init__()

        lbl = ttk.Label(self, text=f'Количество элементов в списке: {len(spis)}').pack()

        self.mainloop()


class AddWindow(tk.Toplevel):
    def __init__(self, spis):
        super().__init__()
        self.spis = spis

        lbl = ttk.Label(self, text='Введите элемент, который хотите добавить').grid(row=0)
        self.ent = ttk.Entry(self)
        self.ent.grid(row=1)

        approv_btn = ttk.Button(self, text='Подтвердить', command=self.approve).grid(row=2)

    def approve(self):
        self.spis += [self.ent.get()]
        self.destroy()


class SearchWindow(tk.Toplevel):
    def __init__(self, spis):
        super().__init__()
        self.spis = spis

        lbl = ttk.Label(self, text='Введите элемент, который хотите найти').grid(row=0)
        self.ent = ttk.Entry(self)
        self.ent.grid(row=1)

        approv_btn = ttk.Button(self, text='Подтвердить', command=self.find).grid(row=2)

    def find(self):
        search = self.ent.get()

        if search in self.spis:
            print(f'Искомый элемент находится под номером {self.spis.index(search) + 1} в списке')
        else:
            print('Искомый элемент в списке не найден')


class DeletionWindow(tk.Toplevel):
    def __init__(self, spis):
        super().__init__()
        self.spis = spis

        lbl = ttk.Label(self, text='Выберите элемент для удаления').grid(row=0, columnspan=3)


        col = 0
        line = 1
        for i in range(len(self.spis)):
            if col > 3:
                col = 0
                line += 1

            btn = ttk.Button(self, text=f'{spis[i]}', command=lambda: self.delete(i))
            btn.grid(row=line, column=col)
            col += 1

    def delete(self, indx):
        self.spis.pop(indx)
        self.destroy()





class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.spis = None

        btn1 = ttk.Button(self, text='Создание списка', command=self.make_spis).grid(row=0)
        btn2 = ttk.Button(self, text='Вывод списка в консоль', command=self.spis_to_console).grid(row=1)
        btn3 = ttk.Button(self, text='Запись списка в файл', command=self.spis_to_file).grid(row=2)
        btn4 = ttk.Button(self, text='Количество элементов в списке', command=self.spis_len).grid(row=3)
        btn5 = ttk.Button(self, text='Добавление элемента в список', command=self.add_to_spis).grid(row=4)
        btn6 = ttk.Button(self, text='Поиск элемента в списке', command=self.find_el).grid(row=5)
        btn7 = ttk.Button(self, text='Удаление элемента из списка', command=self.delete_el).grid(row=6)
        btn8 = ttk.Button(self, text='Выход', command=self.exit).grid(row=7)

        self.mainloop()

    def make_spis(self):
        make = MakingWindow()
        print(make.spis)
        self.spis = make.spis

    def spis_to_console(self):
        print(self.spis)

    def spis_to_file(self):
        with open('file.txt', 'w') as f:
            f.write(str(self.spis))

    def spis_len(self):
        LengthWindow(self.spis)

    def add_to_spis(self):
        add = AddWindow(self.spis)
        print(add.spis)
        self.spis = add.spis

    def find_el(self):
        SearchWindow(self.spis)

    def delete_el(self):
        delete = DeletionWindow(self.spis)
        self.spis = delete.spis

    def exit(self):
        self.destroy()


if __name__ == '__main__':
    MainWindow()
