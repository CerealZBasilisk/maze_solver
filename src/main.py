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

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False


    
def main():
    win = Window(1920, 1080) # use 800 by 600 for final
    win.wait_for_close()


if __name__ == "__main__":

    main()