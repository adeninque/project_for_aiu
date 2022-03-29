import random
from tkinter import *
from time import sleep
from cell import Cell
from collections import Counter

class Game:
    def __init__(self, n, m, *tribes):
        self.__generate_field(n, m, tribes)
            
    def __generate_field(self, n, m, tribes):
        self.game_field = [[0 for _ in range(self.__is_int(m))] for _ in range(self.__is_int(n))]
        self.__rows, self.__cols = n, m
        for tribe in tribes:
            for _ in range(int((self.__cols * self.__rows) / 3)):
                while True:
                    i, j = random.randint(0, self.__rows-1), random.randint(0, self.__cols-1)
                    if type(self.game_field[i][j]) != Cell:
                        self.game_field[i][j] = Cell(tribe)
                        break

    @staticmethod
    def __is_int(x):
        if type(x) != int:
            raise TypeError('Check for int not passed')
        return x
    
    def display(self):
        print('\n'.join([' '.join(['*' if col == 1 else '-' for col in row]) for row in self.game_field]))
    
    def step(self):
        changes = []
        for i in range(self.__rows):
            for j in range(self.__cols):
                neighbors = []
                allies = 0
                enemies = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k != i or l != j:
                            if 0 <= k < self.__rows and 0 <= l < self.__cols:
                                if type(self.game_field[k][l]) == Cell and type(self.game_field[i][j]) == Cell:
                                    neighbors.append(self.game_field[k][l].tribe)
                                    if self.game_field[i][j].tribe != self.game_field[k][l].tribe:
                                        enemies += 1
                                    else:
                                        allies += 1
                if self.game_field[i][j] != 0:
                    if allies > enemies:
                        changes.append([0, i, j])
                else:
                    if neighbors:
                        maxim = dict(Counter(neighbors))
                        self.game_field[i][j] = Cell(max(maxim, key = maxim.get))
        for c in changes:
            self.game_field[c[1]][c[2]] = c[0]
    
    def start(self):
        width = self.__cols * 20
        height = self.__rows * 20
        dead_color = '#F1F1F1'
        
        root = Tk()
        root.geometry(f'{width}x{height}')
        canva = Canvas(root, width = width, height = height)
        
        def run():
            canva.delete('all')
            for i in range(self.__rows):
                    for j in range(self.__cols):
                        canva.create_rectangle(0 + (20*j), 0 + (20*i), 20 + (20*j), 20 + (20*i), fill = dead_color if self.game_field[i][j] == 0 else self.game_field[i][j].color)
            self.step()
            canva.after(300, run)
        
        canva.pack()
        run()
        root.mainloop()
        

if __name__ == '__main__':
    Game(30, 40, "#FBCB2D", '#37FB2D', '#2DFBE3').start()