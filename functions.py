from tkinter import Button, Label, messagebox
import random
import configure
import sys


class Cell:
    all = []
    cell_count = configure.CELL_COUNT
    cell_count_button = None

    def __init__(self, x, y, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn = None
        self.is_mine_candidate = False

        Cell.all.append(self)

    def create_button(self, location):
        button = Button(
            location,
            width=15,
            height=7
        )
        self.cell_btn = button
        button.bind('<Button-1>', self.left_click_action)
        button.bind('<Button-3>', self.right_click_action)

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn.configure(bg='orange')
            self.is_mine_candidate = True
        else:
            self.cell_btn.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_lenght == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

        if Cell.cell_count == configure.NUMBER_OF_MINES:
            messagebox.showinfo('game finished', 'CONGRATULATIONS YOU HAVE WON THE GAME')
        self.cell_btn.unbind('<Button-1>')
        self.cell_btn.unbind('<Button-3>')

    def show_mine(self):
        messagebox.showinfo('GAME OVER', 'YOU HAVE CLICKED ON A MINE')
        sys.exit()

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cells_axis(self.x - 1, self.y - 1),
            self.get_cells_axis(self.x - 1, self.y),
            self.get_cells_axis(self.x - 1, self.y + 1),
            self.get_cells_axis(self.x, self.y - 1),
            self.get_cells_axis(self.x + 1, self.y - 1),
            self.get_cells_axis(self.x + 1, self.y),
            self.get_cells_axis(self.x + 1, self.y + 1),
            self.get_cells_axis(self.x, self.y + 1)]

        cells = [b for b in cells if b is not None]
        return cells

    def get_cells_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells_mines_lenght(self):
        cnt = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                cnt += 1
        return cnt

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn.configure(text=self.surrounded_cells_mines_lenght)
            if Cell.cell_count_button:
                Cell.cell_count_button.configure(text=f'CELLS LEFT :{Cell.cell_count}')

            self.cell_btn.configure(bg='SystemButtonFace')
        self.is_opened = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, configure.NUMBER_OF_MINES
        )
        for a in picked_cells:
            a.is_mine = True

    @staticmethod
    def create_cell_count_label(location):
        lab = Label(
            location,
            bg='#5D6D7E',
            fg='white',
            text=f'CELLS LEFT :{Cell.cell_count}',
            font=('bold', 48)
        )
        Cell.cell_count_button = lab
