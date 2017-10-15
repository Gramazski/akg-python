import sdl2
import sdl2.ext
import math


class ApplicationRenderer:
    RED_COLOR = sdl2.ext.Color(255, 0, 0, 0)
    BLUE_COLOR = sdl2.ext.Color(0, 255, 0, 0)
    CLEAR_COLOR = sdl2.ext.Color(255, 255, 255, 0)
    AXIS_COLOR = sdl2.ext.Color(0, 0, 0, 255)
    X_CENTER = 400
    Y_CENTER = 300
    SIDE_LENGTH = 400
    SQ_COUNT = 20

    def __init__(self, window, native_width, native_height):
        self.renderer = sdl2.ext.Renderer(window)

        self.native_width = native_width
        self.native_height = native_height

        self.x_scale = 1
        self.y_scale = 1

        self.update_coordinates(native_width, native_height)

    def update_coordinates(self, width, height):
        self.x_scale = width / float(self.native_width)
        self.y_scale = height / float(self.native_height)

    def render(self):
        self.clear()
        self.draw_tracery()
        self.update()

    def clear(self):
        self.renderer.clear(ApplicationRenderer.CLEAR_COLOR)

    def set_sq_count(self, count):
        self.SQ_COUNT = count * 10

    def draw_tracery(self):
        x1, y1 = self.X_CENTER - self.SIDE_LENGTH / 2, self.Y_CENTER - self.SIDE_LENGTH / 2
        x2, y2 = self.X_CENTER + self.SIDE_LENGTH / 2, self.Y_CENTER - self.SIDE_LENGTH / 2
        x3, y3 = self.X_CENTER + self.SIDE_LENGTH / 2, self.Y_CENTER + self.SIDE_LENGTH / 2
        x4, y4 = self.X_CENTER - self.SIDE_LENGTH / 2, self.Y_CENTER + self.SIDE_LENGTH / 2

        self.draw_square(x1, y1, x2, y2, x3, y3, x4, y4, self.RED_COLOR)

        k = 1
        n = 10
        for i in range(0, self.SQ_COUNT):
            mu = math.tan(k * math.pi / (4 * n)) / (math.tan(k * math.pi / (4 * n)) + 1)

            x1, x2, x3, x4 = (1 - mu) * x1 + mu * x2, \
                             (1 - mu) * x2 + mu * x3, \
                             (1 - mu) * x3 + mu * x4, \
                             (1 - mu) * x4 + mu * x1
            y1, y2, y3, y4 = (1 - mu) * y1 + mu * y2, \
                             (1 - mu) * y2 + mu * y3, \
                             (1 - mu) * y3 + mu * y4, \
                             (1 - mu) * y4 + mu * y1

            if (mu / (1 - mu) - 1) < 0.0001:
                self.draw_square(x1, y1, x2, y2, x3, y3, x4, y4, self.BLUE_COLOR)
            else:
                self.draw_square(x1, y1, x2, y2, x3, y3, x4, y4, self.RED_COLOR)
            n += 1

    def draw_square(self, x1, y1, x2, y2, x3, y3, x4, y4, color):
        self.draw_line(self.x_scale * x1,
                       self.y_scale * y1,
                       self.x_scale * x2,
                       self.y_scale * y2,
                       color)
        self.draw_line(self.x_scale * x2,
                       self.y_scale * y2,
                       self.x_scale * x3,
                       self.y_scale * y3,
                       color)
        self.draw_line(self.x_scale * x3,
                       self.y_scale * y3,
                       self.x_scale * x4,
                       self.y_scale * y4,
                       color)
        self.draw_line(self.x_scale * x4,
                       self.y_scale * y4,
                       self.x_scale * x1,
                       self.y_scale * y1,
                       color)

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

    def draw_pixel(self, x, y, color):
        self.renderer.draw_point(points=[int(x), int(y)], color=color)

    def update(self):
        self.renderer.present()
