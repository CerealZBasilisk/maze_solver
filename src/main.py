from tkinter import Tk, BOTH, Canvas
import time
from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600) # use 800 by 600 for final

    # Create a maze with a 10x10 grid of cells
    maze = Maze(50, 50, 10, 10, 50, 50, win, 42)

    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    
    win.wait_for_close()


if __name__ == "__main__":

    main()