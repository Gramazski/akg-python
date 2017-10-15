import sdl2
import sdl2.ext
import math

class Square_New:
    LINE_COLOR = sdl2.ext.Color(255, 0, 0, 0)
    CLEAR_COLOR = sdl2.ext.Color(255, 255, 255, 0)
    BORDER_COLOR = sdl2.ext.Color(255, 0, 255, 0)

    def __init__(self, window, init_x1_coord, init_y1_coord, init_x2_coord, init_y2_coord,
                 init_x3_coord, init_y3_coord, init_x4_coord, init_y4_coord,
                 init_circle_x, init_circle_y, init_circle_r,
                 contr_x1, contr_y1, contr_x2, contr_y2, contr_x3, contr_y3):
        self.renderer = sdl2.ext.Renderer(window)
        self.x1_coord = init_x1_coord
        self.y1_coord = init_y1_coord
        self.x2_coord = init_x2_coord
        self.y2_coord = init_y2_coord

        self.x3_coord = init_x3_coord
        self.y3_coord = init_y3_coord
        self.x4_coord = init_x4_coord
        self.y4_coord = init_y4_coord

        self.circle_x = init_circle_x
        self.circle_y = init_circle_y
        self.circle_r = init_circle_r
        self.contr_x1 = contr_x1
        self.contr_x2 = contr_x2
        self.contr_y1 = contr_y1
        self.contr_y2 = contr_y2
        self.contr_x3 = contr_x3
        self.contr_y3 = contr_y3
        self.z_circle = True
        self.z_square = False
        self.renderer.present()

    """def update_coordinates(self, width, height):
        self.x_scale = width / float(self.native_width)
        self.y_scale = height / float(self.native_height)"""

    def draw(self):
        self.clear()
        self.draw_contr()
        self.draw_circle()
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
        angle = 0
        while angle < 2 * math.pi:
            if self.is_out_of_field(self.circle_x + long(self.circle_r * math.cos(angle)),
                                     self.circle_y + long(self.circle_r * math.sin(angle))):
                if self.z_square:
                    if not self.is_in_figure_square(self.circle_x + long(self.circle_r * math.cos(angle)),
                                                    self.circle_y + long(self.circle_r * math.sin(angle))):
                        self.renderer.draw_line((self.circle_x + long(self.circle_r * math.cos(angle - 0.07)),
                                                 self.circle_y + long(self.circle_r * math.sin(angle - 0.07)),
                                                 self.circle_x + long(self.circle_r * math.cos(angle)),
                                                 self.circle_y + long(self.circle_r * math.sin(angle))),
                                                Square_New.LINE_COLOR)
                    else:
                        self.renderer.draw_point((self.circle_x + long(self.circle_r * math.cos(angle - 0.07)),
                                                 self.circle_y + long(self.circle_r * math.sin(angle - 0.07))),
                                                Square_New.LINE_COLOR)
                        #print "haha"
                else:
                    self.renderer.draw_line((self.circle_x + long(self.circle_r * math.cos(angle - 0.07)),
                                             self.circle_y + long(self.circle_r * math.sin(angle - 0.07)),
                                             self.circle_x + long(self.circle_r * math.cos(angle)),
                                             self.circle_y + long(self.circle_r * math.sin(angle))),
                                            Square_New.LINE_COLOR)
            else:
                self.renderer.draw_point((self.circle_x + long(self.circle_r * math.cos(angle - 0.07)),
                                          self.circle_y + long(self.circle_r * math.sin(angle - 0.07))),
                                         Square_New.LINE_COLOR)

            angle += 0.07

    def move_themself(self):
        self.x1_coord, self.y1_coord = self.magic(self.x1_coord, self.y1_coord)
        self.x2_coord, self.y2_coord = self.magic(self.x2_coord, self.y2_coord)
        self.x3_coord, self.y3_coord = self.magic(self.x3_coord, self.y3_coord)
        self.x4_coord, self.y4_coord = self.magic(self.x4_coord, self.y4_coord)
        # self.x1_coord += 1
        # self.y1_coord += 1
        # self.x2_coord += 1
        # self.y2_coord += 2
        # self.x3_coord -= 1
        # self.y3_coord += 2
        # self.x4_coord -= 1
        # self.y4_coord -= 1
        self.circle_x += 2
        self.circle_y += 2

    def magic(self, x, y):
        x1 = x * math.cos(math.pi / 250) - y * math.sin(math.pi / 250)
        y1 = y * math.cos(math.pi / 250) + x * math.sin(math.pi / 250)
        #print y1

        return x1, y1
        #return x, y

    def draw_contr(self):
        # self.draw_line_contr_y(self.contr_y1, self.contr_x1, self.contr_y2)
        # self.draw_line_contr_x(self.contr_x1, self.contr_y1, self.contr_x2)
        # self.draw_line_contr_y(self.contr_y1, self.contr_x2, self.contr_y2)
        # self.draw_line_contr_x(self.contr_x1, self.contr_y2, self.contr_x2)
        self.renderer.draw_line((self.contr_x1, self.contr_y1, self.contr_x2, self.contr_y1), Square_New.LINE_COLOR)
        self.renderer.draw_line((self.contr_x2, self.contr_y1, self.contr_x3, self.contr_y3), Square_New.LINE_COLOR)
        self.renderer.draw_line((self.contr_x3, self.contr_y3, self.contr_x2, self.contr_y2), Square_New.LINE_COLOR)
        self.renderer.draw_line((self.contr_x1, self.contr_y2, self.contr_x2, self.contr_y2), Square_New.LINE_COLOR)
        self.renderer.draw_line((self.contr_x1, self.contr_y1, self.contr_x1, self.contr_y2), Square_New.LINE_COLOR)

    def draw_rect(self):
        # self.renderer.draw_line((self.x1_coord, self.y1_coord, self.x2_coord, self.y2_coord), Square_New.LINE_COLOR)
        # self.renderer.draw_line((self.x2_coord, self.y2_coord, self.x3_coord, self.y3_coord), Square_New.LINE_COLOR)
        # self.renderer.draw_line((self.x3_coord, self.y3_coord, self.x4_coord, self.y4_coord), Square_New.LINE_COLOR)
        # self.renderer.draw_line((self.x4_coord, self.y4_coord, self.x1_coord, self.y1_coord), Square_New.LINE_COLOR)
        self.draw_line(self.x1_coord, self.y1_coord, self.x2_coord, self.y2_coord, Square_New.LINE_COLOR)
        self.draw_line(self.x2_coord, self.y2_coord, self.x3_coord, self.y3_coord, Square_New.LINE_COLOR)
        self.draw_line(self.x3_coord, self.y3_coord, self.x4_coord, self.y4_coord, Square_New.LINE_COLOR)
        self.draw_line(self.x4_coord, self.y4_coord, self.x1_coord, self.y1_coord, Square_New.LINE_COLOR)
        #self.draw_line_y(self.y1_coord, self.x1_coord, self.y2_coord)
        #self.draw_line_x(self.x1_coord, self.y1_coord, self.x2_coord)
        #self.draw_line_y(self.y1_coord, self.x2_coord, self.y2_coord)
        #self.draw_line_x(self.x1_coord, self.y2_coord, self.x2_coord)

    def draw_line(self, x1, y1, x2, y2, color):

        dx = math.fabs(x2 - x1)
        dy = math.fabs(y2 - y1)
        sx = 1 if x2 >= x1 else -1
        sy = 1 if y2 >= y1 else -1

        if dy <= dx:
            d = 2 * dy - dx
            d1 = 2 * dy
            d2 = (dy - dx) * 2

            self.draw_pixel(x1, y1, color)

            x = x1 + sx
            y = y1
            i = 1
            while i <= dx:
                if d > 0:
                    d += d2
                    y += sy
                else:
                    d += d1

                self.draw_pixel(x, y, color)

                i += 1
                x += sx
        else:
            d = dx * 2 - dy
            d1 = dx * 2
            d2 = (dx - dy) * 2

            self.draw_pixel(x1, y1, color)
            x = x1
            y = y1 + sy
            i = 1
            while i <= dy:
                if d > 0:
                    d += d2
                    x += sx
                else:
                    d += d1

                self.draw_pixel(x, y, color)

                i += 1
                y += sy

    counter = 0

    def draw_pixel(self, x, y, color):
        if self.is_out_of_field(x, y) and self.z_square or (self.is_out_of_field(x, y) and self.z_circle and not self.is_in_figure_circle(x, y)):
            self.counter = 0
            self.renderer.draw_point(points=[int(x), int(y)], color=color)
        else:
            if self.counter < 5:
                self.renderer.draw_point(points=[int(x), int(y)], color=color)
            self.counter += 1
            if self.counter == 9:
                self.counter = 0

    def draw_line_x(self, x1, y1, x2):
        n = 0
        step = 1
        while x1 + n * step < x2:
            if self.is_out_of_field(x1 + (n + 1) * step, y1):
                if self.z_circle:
                    if not self.is_in_figure_circle(x1 + (n + 1) * step, y1):
                        self.renderer.draw_line((x1 + n * step, y1, x1 + (n + 1) * step, y1),
                                                Square_New.LINE_COLOR)
                    else:
                        self.renderer.draw_point((x1 + n * step, y1),
                                                Square_New.LINE_COLOR)
                else:
                    self.renderer.draw_line((x1 + n * step, y1, x1 + (n + 1) * step, y1),
                                            Square_New.LINE_COLOR)
            #else:
                #print "haha"

            n += 2

    def draw_line_contr_x(self, x1, y1, x2):
        n = 0
        step = 1
        while x1 + n * step < x2:
            self.renderer.draw_line((x1 + n * step, y1, x1 + (n + 1) * step, y1),
                                    Square_New.BORDER_COLOR)

            n += 1

    def draw_line_contr_y(self, y1, x1, y2):
        n = 0
        step = 1
        while y1 + n * step < y2:
            self.renderer.draw_line((x1, y1 + n * step, x1, y1 + (n + 1) * step),
                                    Square_New.BORDER_COLOR)

            n += 1

    def draw_line_y(self, y1, x1, y2):
        n = 0
        step = 1
        while y1 + n * step < y2:
            if self.is_out_of_field(x1, y1 + (n + 1) * step):
                if self.z_circle:
                    if not self.is_in_figure_circle(x1, y1 + (n + 1) * step):
                        self.renderer.draw_line((x1, y1 + n * step, x1, y1 + (n + 1) * step),
                                                Square_New.LINE_COLOR)
                    else:
                        self.renderer.draw_point((x1, y1 + n * step),
                                                Square_New.LINE_COLOR)
                else:
                    self.renderer.draw_line((x1, y1 + n * step, x1, y1 + (n + 1) * step),
                                            Square_New.LINE_COLOR)
            #else:
                #
                    # print "haha"

            n += 2

    def is_out_of_field(self, x, y):
        if self.is_in_figure_square_self(x, self.contr_x1, self.contr_x3):
            if self.is_in_figure_square_self(y, self.contr_y1, self.contr_y3):
                return True

        if (y > self.contr_y3 and y > 2.85 * x - 1017.5):#550 550
            return True

        if (y < self.contr_y3 and y < -2.45 * x + 1367.5): #550 20
            return True

        return False

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
        self.x3_coord += del_x
        self.x4_coord += del_x
        self.y3_coord += del_y
        self.y4_coord += del_y

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
        center_x = (self.x1_coord + self.x3_coord) / 2
        center_y = (self.y3_coord + self.y1_coord) / 2

        return math.sqrt(math.pow(center_x - x1, 2) + math.pow(center_y - y1, 2)) < 25
        # if self.is_in_figure_square_self(x1, self.x3_coord, self.x1_coord):
        #     if self.is_in_figure_square_self(y1, self.y3_coord, self.y1_coord):
        #         return True
        #
        # return False

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

