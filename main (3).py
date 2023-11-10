from tkinter import *
from functions import Cell
import configure
import new

page = Tk()
page.configure(bg='grey')
page.geometry(f'{configure.WIDTH}x{configure.HEIGHT}')
page.title('MineSweeper Game')
page.resizable(False, False)

TOP_FRAME = Frame(
    page,
    bg='#5D6D7E',
    width=configure.WIDTH,
    height=new.height_percentage(25)
)
TOP_FRAME.place(
    x=0,
    y=0
)

GAME_TITLE = Label(
    TOP_FRAME,
    bg='#5D6D7E',
    fg='white',
    text='MineSweeper Game',
    font=('bold', 48)
)
GAME_TITLE.place(
    x=new.width_percentage(36),
    y=0
)

GAME_AREA_FRAME = Frame(
    page,
    bg='#5D6D7E',
    width=new.width_percentage(75),
    height=new.height_percentage(75)
)
GAME_AREA_FRAME.place(
    x=new.width_percentage(36),
    y=new.height_percentage(36)
)
for x in range(configure.GRID_SIZE):
    for y in range(configure.GRID_SIZE):
        c = Cell(x, y)
        c.create_button(GAME_AREA_FRAME)
        c.cell_btn.grid(column=x, row=y)

Cell.create_cell_count_label(TOP_FRAME)
Cell.cell_count_button.place(
    x=new.width_percentage(45),
    y=new.height_percentage(15)
)
Cell.randomize_mines()
page.mainloop()
