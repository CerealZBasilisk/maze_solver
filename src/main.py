from tkinter import Tk, BOTH, Canvas


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


    def run(self):
        pass

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
        
    
def main():
    win = Window(800, 600) # use 800 by 600 for final

    # Create two cells side by side
    cell_1 = Cell(Point(100, 100), Point(150, 150), window=win)
    cell_2 = Cell(Point(150, 100), Point(200, 150), window=win)

    # Draw both cells
    cell_1.draw()
    cell_2.draw()

    # Draw a move from cell_1 to cell_2 (red line)
    cell_1.draw_move(to_cell=cell_2)

    # Optional: draw a move back (gray undo line)
    cell_2.draw_move(to_cell=cell_1, undo=True)




    win.wait_for_close()


if __name__ == "__main__":

    main()