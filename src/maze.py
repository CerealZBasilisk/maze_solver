from tkinter import Tk, BOTH, Canvas
import time
from graphics import *
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self.seed = seed

    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                # Calculate cell position relative to maze position
                x1 = self.x1 + (i * self.cell_size_x)
                y1 = self.y1 + (j * self.cell_size_y)
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                # Create cell with the calculated position
                cell = Cell(Point(x1, y1), Point(x2, y2), window=self.win)
                column.append(cell)
            self._cells.append(column)
        if self.win:
            # Draw all cells after the grid is created
            for i in range(self.num_cols):
                for j in range(self.num_rows):
                    self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    
    def _break_entrance_and_exit(self):
        self._cells[0][0].north = False  # Instead of has_top_wall
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].south = False  # Instead of has_bottom_wall
        self._draw_cell(self.num_cols-1, self.num_rows-1)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while True:
            neighbors = [] # neighbors = self.get_neighbors(i, j)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # Check if this neighbor is within the maze bounds
                if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
                    if not self._cells[ni][nj].visited:
                        neighbors.append((di, dj))
            if len(neighbors) == 0:
                self._draw_cell(i, j)
                return
            direction = random.choice(neighbors)
            di,dj = direction
            ni, nj = i + di, j + dj
            if direction == (-1, 0):  # This is West
                self._cells[i][j].west = False
                self._cells[ni][nj].east = False
            elif direction == (0, 1):  # This is South
                self._cells[i][j].south = False
                self._cells[ni][nj].north = False
            elif direction == (1, 0):  # This is East
                self._cells[i][j].east = False
                self._cells[ni][nj].west = False
            else:  # direction == (0, -1), This is North
                self._cells[i][j].north = False
                self._cells[ni][nj].south = False
            
            self._break_walls_r(ni,nj)




def get_neighbors(self, i, j): #alternate method for finding neighbors
    # Potential directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbors = []
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # Check if this neighbor is within the maze bounds
        if 0 <= ni < self.num_cols and 0 <= nj < self.num_rows:
            neighbors.append((ni, nj))
    
    return neighbors    



{(-1, 0):"current north wall break, next south wall break", 
(0, 1):"current east wall break, next cell west wall break", 
(1, 0):"current south wall break, next cell north wall break", 
(0, -1):"current west wall break, next cell east wall break"}