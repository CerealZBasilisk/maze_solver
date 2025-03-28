from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.geometry(f"{self.width}x{self.height}")
        self.canvas = Canvas(self.root, 
                             width=self.width, 
                             height=self.height, 
                             bg="white")
        self.canvas.pack(side="top")
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color=fill_color)
        

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_01:Point, point_02:Point):
        self.x1 = point_01.x
        self.y1 = point_01.y
        self.x2 = point_02.x
        self.y2 = point_02.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
    self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2
)

class Cell:
    def __init__(self, point_01:Point, point_02:Point, window=Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window
        self._x1 = point_01.x
        self._y1 = point_01.y
        self._x2 = point_02.x
        self._y2 = point_02.y
    
    def draw_move(self, to_cell, undo=False):
        temp_point_01 = Point((self._x1 + self._x2) / 2,
                              (self._y1 + self._y2) / 2)
        temp_point_02 = Point((to_cell._x1 + to_cell._x2) / 2,
                              (to_cell._y1 + to_cell._y2) / 2)

            
        temp_line = Line(temp_point_01, temp_point_02)
        if not undo:
            self._win.draw_line(line=temp_line,fill_color="red")
        else: 
            self._win.draw_line(line=temp_line,fill_color="grey")
        
            

    def draw(self):
        if self.has_left_wall:
            
            temp_point_01 = Point(self._x1, self._y1)       # Top-left
            temp_point_02 = Point(self._x1, self._y2)       # Bottom-left   
            temp_line = Line(temp_point_01, temp_point_02)
            self._win.draw_line(line=temp_line,fill_color="black")

        if self.has_right_wall:

            temp_point_01 = Point(self._x2, self._y1)       # Top-right
            temp_point_02 = Point(self._x2, self._y2)       # Bottom-right
            temp_line = Line(temp_point_01, temp_point_02)
            self._win.draw_line(line=temp_line,fill_color="black")

        if self.has_top_wall:

            temp_point_01 = Point(self._x1, self._y1)       # Top-left
            temp_point_02 = Point(self._x2, self._y1)       # Top-right
            temp_line = Line(temp_point_01, temp_point_02)
            self._win.draw_line(line=temp_line,fill_color="black")

        if self.has_bottom_wall:

            temp_point_01 = Point(self._x1, self._y2)       # Bottom-left
            temp_point_02 = Point(self._x2, self._y2)       # Bottom-right
            temp_line = Line(temp_point_01, temp_point_02)
            self._win.draw_line(line=temp_line,fill_color="black")

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._cells = []
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._create_cells()

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
    
        # Draw all cells after the grid is created
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)


        pass
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)


def main():
    win = Window(800, 600) # use 800 by 600 for final

    # Create a maze with a 10x10 grid of cells
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    
    win.wait_for_close()


if __name__ == "__main__":

    main()