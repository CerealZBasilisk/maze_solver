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

    def draw_line(self, line, fill_color="black"):
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
    def __init__(self, point_01:Point, point_02:Point, window=None):
        self.west = True
        self.east = True
        self.north = True
        self.south = True
        self._win = window
        self._x1 = point_01.x
        self._y1 = point_01.y
        self._x2 = point_02.x
        self._y2 = point_02.y
        self.visited = False
    
    def draw_move(self, to_cell, undo=False):
        if self._win:
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
        if self._win:
            if self.west:
                
                temp_point_01 = Point(self._x1, self._y1)       # Top-left
                temp_point_02 = Point(self._x1, self._y2)       # Bottom-left   
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="black")

            if self.east:

                temp_point_01 = Point(self._x2, self._y1)       # Top-right
                temp_point_02 = Point(self._x2, self._y2)       # Bottom-right
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="black")

            if self.north:

                temp_point_01 = Point(self._x1, self._y1)       # Top-left
                temp_point_02 = Point(self._x2, self._y1)       # Top-right
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="black")

            if self.south:

                temp_point_01 = Point(self._x1, self._y2)       # Bottom-left
                temp_point_02 = Point(self._x2, self._y2)       # Bottom-right
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="black") 

            if not self.west:
                
                temp_point_01 = Point(self._x1, self._y1)       # Top-left
                temp_point_02 = Point(self._x1, self._y2)       # Bottom-left   
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="white")

            if not self.east:

                temp_point_01 = Point(self._x2, self._y1)       # Top-right
                temp_point_02 = Point(self._x2, self._y2)       # Bottom-right
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="white")

            if not self.north:

                temp_point_01 = Point(self._x1, self._y1)       # Top-left
                temp_point_02 = Point(self._x2, self._y1)       # Top-right
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="white")

            if not self.south:

                temp_point_01 = Point(self._x1, self._y2)       # Bottom-left
                temp_point_02 = Point(self._x2, self._y2)       # Bottom-right
                temp_line = Line(temp_point_01, temp_point_02)
                self._win.draw_line(line=temp_line,fill_color="white")