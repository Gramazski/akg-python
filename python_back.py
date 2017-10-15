import sdl2
import sdl2.ext
import math

class Square_New:
    LINE_COLOR = sdl2.ext.Color(255, 0, 0, 0)
    CLEAR_COLOR = sdl2.ext.Color(255, 255, 255, 0)

    def __init__(self, window, init_x1_coord, init_y1_coord, init_x2_coord, init_y2_coord,
                 init_triangle_x1, init_triangle_y1, init_triangle_x2, init_triangle_y2,
                 init_triangle_x3, init_triangle_y3):
        self.renderer = sdl2.ext.Renderer(window)
        self.x1_coord = init_x1_coord
        self.y1_coord = init_y1_coord
        self.x2_coord = init_x2_coord
        self.y2_coord = init_y2_coord
        self.triangle_x1 = init_triangle_x1
        self.triangle_x2 = init_triangle_x2
        self.triangle_x3 = init_triangle_x3
        self.triangle_y1 = init_triangle_y1
        self.triangle_y2 = init_triangle_y2
        self.triangle_y3 = init_triangle_y3
        self.z_circle = False
        self.z_square = False
        self.renderer.present()

    """def update_coordinates(self, width, height):
        self.x_scale = width / float(self.native_width)
        self.y_scale = height / float(self.native_height)"""

    def draw(self):
        self.clear()
        #self.draw_circle()
        self.draw_rect()
        """self.renderer.draw_line((self.x1_coord, self.y1_coord, self.x1_coord, self.y2_coord),
                                Square.LINE_COLOR)
        self.renderer.draw_line((self.x1_coord, self.y2_coord, self.x2_coord, self.y2_coord),
                                Square.LINE_COLOR)
        self.renderer.draw_line((self.x2_coord, self.y2_coord, self.x2_coord, self.y1_coord),
                                Square.LINE_COLOR)
        self.renderer.draw_line((self.x2_coord, self.y1_coord, self.x1_coord, self.y1_coord),
                                Square.LINE_COLOR)"""
        #self.renderer.draw_rect((self.x1_coord, self.y1_coord, self.x2_coord, self.y2_coord),
        #                        Square.LINE_COLOR)
        self.update()

    def draw_circle(self):
        angle = 1
        while angle < 360:
            if self.z_square:
                if not self.is_in_figure_square(self.circle_x + long(self.circle_r * math.sin(angle)),
                                     self.circle_y + long(self.circle_r * math.cos(angle))):
                    self.renderer.draw_line((self.circle_x + long(self.circle_r * math.sin(angle - 1)),
                                             self.circle_y + long(self.circle_r * math.cos(angle - 1)),
                                             self.circle_x + long(self.circle_r * math.sin(angle)),
                                             self.circle_y + long(self.circle_r * math.cos(angle))),
                                            Square_New.LINE_COLOR)
            else:
                self.renderer.draw_line((self.circle_x + long(self.circle_r * math.sin(angle - 1)),
                                         self.circle_y + long(self.circle_r * math.cos(angle - 1)),
                                         self.circle_x + long(self.circle_r * math.sin(angle)),
                                         self.circle_y + long(self.circle_r * math.cos(angle))),
                                        Square_New.LINE_COLOR)

            angle += 1

    def draw_rect(self):
        self.draw_line_y(self.y1_coord, self.x1_coord, self.y2_coord)
        self.draw_line_x(self.x1_coord, self.y1_coord, self.x2_coord)
        self.draw_line_y(self.y1_coord, self.x2_coord, self.y2_coord)
        self.draw_line_x(self.x1_coord, self.y2_coord, self.x2_coord)

    def draw_line_x(self, x1, y1, x2):
        n = 0
        step = 1
        while x1 + n * step < x2:
            if self.z_circle:
                if not self.is_in_figure_circle(x1 + (n + 1) * step, y1):
                    self.renderer.draw_line((x1 + n * step, y1, x1 + (n + 1) * step, y1),
                                            Square_New.LINE_COLOR)
            else:
                self.renderer.draw_line((x1 + n * step, y1, x1 + (n + 1) * step, y1),
                                        Square_New.LINE_COLOR)
            n += 1

    def draw_line_y(self, y1, x1, y2):
        n = 0
        step = 1
        while y1 + n * step < y2:
            if self.z_circle:
                if not self.is_in_figure_circle(x1, y1 + (n + 1) * step):
                    self.renderer.draw_line((x1, y1 + n * step, x1, y1 + (n + 1) * step),
                                            Square_New.LINE_COLOR)
            else:
                self.renderer.draw_line((x1, y1 + n * step, x1, y1 + (n + 1) * step),
                                        Square_New.LINE_COLOR)
            n += 1

    def clear(self):
        self.renderer.clear(Square_New.CLEAR_COLOR)

    def update(self):
        self.renderer.present()

    def move(self, del_x, del_y):
        if self.z_circle:
            self.move_circle(del_x, del_y)

        if self.z_square:
            self.move_square(del_x, del_y)

    def move_square(self, del_x, del_y):
        self.x1_coord += del_x
        self.x2_coord += del_x
        self.y1_coord += del_y
        self.y2_coord += del_y

    def move_circle(self, del_x, del_y):
        self.circle_x += del_x
        self.circle_y += del_y

    def is_in_figure_circle(self, x1, y1):
        return (x1 - self.circle_x) * (x1 - self.circle_x) + (y1 - self.circle_y) * (y1 - self.circle_y) < self.circle_r * self.circle_r

    def is_in_figure(self, x1, y1):
        if self.is_in_figure_square(x1, y1):
            self.z_square = True
            self.z_circle = False
            return True

        if self.is_in_figure_circle(x1, y1):
            self.z_circle = True
            self.z_square = False
            return True

        return False

    def is_in_figure_square(self, x1, y1):
        if self.is_in_figure_square_self(x1, self.x1_coord, self.x2_coord):
            if self.is_in_figure_square_self(y1, self.y1_coord, self.y2_coord):
                return True

        return False

    def is_in_figure_square_self(self, coord, f_coord, s_coord):
        if coord > f_coord:
            if coord < s_coord:
                return True

        return False

    def print_coords(self):
        print self.x1_coord
        print self.x2_coord
        print self.y1_coord
        print self.y2_coord


class ApplicationRenderer:
    def __init__(self, window, native_width, native_height, left_offset, right_offset):
        self.renderer = sdl2.ext.Renderer(window)

        self.native_width = native_width
        self.native_height = native_height

        self.left_offset = left_offset
        self.top_offset = right_offset

        self.x_scale = 1
        self.y_scale = 1

        self.update_coordinates(native_width, native_height)

    def update_coordinates(self, width, height):
        self.x_scale = width / float(self.native_width)
        self.y_scale = height / float(self.native_height)

