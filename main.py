from window import Window
from lines import *

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(100, 100), Point(200,200)))
    win.draw_line(Line(Point(200, 100), Point(100,200)), fill_color="red")
    win.wait_for_close()

if __name__ == "__main__":
    main()