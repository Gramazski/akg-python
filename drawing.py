import sdl2
import sdl2.ext
import math


class ApplicationRenderer:
    CLEAR_COLOR = sdl2.ext.Color(255, 255, 255, 0)
    AXIS_COLOR = sdl2.ext.Color(0, 0, 0, 255)

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

    def render(self, drawer):
        self.clear()
        center_to_angle_length = 283
        angle = 0

        for i in range(0, 30):
            drawer.draw(center_to_angle_length, angle)
            center_to_angle_length *= math.sin(math.pi / 3)
            angle += math.pi / 19

        self.update()

    def clear(self):
        self.renderer.clear(ApplicationRenderer.CLEAR_COLOR)

    def draw_line(self, x1, y1, x2, y2, color):
        drawer = Drawer(self)
        drawer.draw_line(int(self.x_scale * (x1 + self.left_offset)),
                         int(self.y_scale * (-y1 + self.top_offset)),
                         int(self.x_scale * (x2 + self.left_offset)),
                         int(self.y_scale * (-y2 + self.top_offset)),
                         color)

    def draw_pixel(self, x, y, color):
        self.renderer.draw_point(points=[int(x), int(y)], color=color)

    def draw_axis(self):
        self.draw_line(-self.left_offset,
                       0,
                       self.native_width - self.left_offset,
                       0,
                       ApplicationRenderer.AXIS_COLOR)
        self.draw_line(0,
                       -self.top_offset,
                       0,
                       self.native_height - self.top_offset,
                       ApplicationRenderer.AXIS_COLOR)

    def update(self):
        self.renderer.present()


class Drawer:
    LINE_COLOR = sdl2.ext.Color(255, 0, 0, 0)

    def __init__(self, renderer):
        self.renderer = renderer

    def draw_square(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.draw_line(x1, y1, x2, y2, self.LINE_COLOR)
        self.draw_line(x2, y2, x3, y3, self.LINE_COLOR)
        self.draw_line(x3, y3, x4, y4, self.LINE_COLOR)
        self.draw_line(x4, y4, x1, y1, self.LINE_COLOR)

    def draw(self, center_to_angle_length, angle):
        x0 = 200
        y0 = 200

        x1 = x0 + center_to_angle_length * math.cos(angle + 1 * math.pi / 4)
        y1 = y0 + center_to_angle_length * math.sin(angle + 1 * math.pi / 4)
        x2 = x0 + center_to_angle_length * math.cos(angle + 3 * math.pi / 4)
        y2 = y0 + center_to_angle_length * math.sin(angle + 3 * math.pi / 4)
        x3 = x0 + center_to_angle_length * math.cos(angle + 5 * math.pi / 4)
        y3 = y0 + center_to_angle_length * math.sin(angle + 5 * math.pi / 4)
        x4 = x0 + center_to_angle_length * math.cos(angle + 7 * math.pi / 4)
        y4 = y0 + center_to_angle_length * math.sin(angle + 7 * math.pi / 4)

        self.draw_square(x1, y1, x2, y2, x3, y3, x4, y4)

    def draw_line(self, x1, y1, x2, y2, color):

        dx = math.fabs(x2 - x1)
        dy = math.fabs(y2 - y1)
        sx = 1 if x2 >= x1 else -1
        sy = 1 if y2 >= y1 else -1

        if dy <= dx:
            d = 2 * dy - dx
            d1 = 2 * dy
            d2 = (dy - dx) * 2

            self.renderer.draw_pixel(x1, y1, color)
            x = x1 + sx
            y = y1
            i = 1
            while i <= dx:
                if d > 0:
                    d += d2
                    y += sy
                else:
                    d += d1

                self.renderer.draw_pixel(x, y, color)

                i += 1
                x += sx
        else:
            d = dx * 2 - dy
            d1 = dx * 2
            d2 = (dx - dy) * 2

            self.renderer.draw_pixel(x1, y1, color)
            x = x1
            y = y1 + sy
            i = 1
            while i <= dy:
                if d > 0:
                    d += d2
                    x += sx
                else:
                    d += d1

                self.renderer.draw_pixel(x, y, color)

                i += 1
                y += sy
        return 0
