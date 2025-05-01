from window import Window
from lines import Line, Point

class Cell:
    def __init__(self, has_left_wall, 
                 has_right_wall,
                 has_top_wall,
                 has_bottom_wall,
                 _x1,
                 _x2,
                 _y1,
                 _y2,
                 _win=None):
        # Initializing the cell with walls and coords
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        # Drawing walls of the cell
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        # if cell wall is not present, color it white
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color="blue")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color="blue")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:  
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color="blue")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)   
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color="blue")

    def draw_move(self, next_cell, undo=False):
        center_current_cell = Point((self._x1 + self._x2) /2, (self._y1 + self._y2) /2)
        center_next_cell = Point((next_cell._x1 + next_cell._x2) /2, (next_cell._y1 + next_cell._y2) /2) 

        if undo:
            Line(center_current_cell, center_next_cell).draw(self._win, fill_color="gray")
        else:
            Line(center_current_cell, center_next_cell).draw(self._win, fill_color="red")