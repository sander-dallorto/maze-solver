from tkinter import Tk, BOTH, Canvas
from lines import Line

class Window:
    def __init__(self, width, height):
        # Initializes window properties and creates a Tkinter window
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack()
        self.running = False

    def redraw(self):
        # Redraws the window
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Waits for the window to close
        self.running = True
        while self.running == True:
            self.redraw()
    
    def close(self):
        # Closes the window
        self.running = False
    
    def draw_line(self, Line, fill_color="black"):
        # Draws a line on the window
        Line.draw(self.__canvas, fill_color)


    