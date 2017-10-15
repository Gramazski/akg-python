import sys
import sdl2
import sdl2.ext
import config
import ctypes
import square_new

def run():
    sdl2.ext.init()

    window = create_window()
    window.show()
    """application_renderer = drawing.ApplicationRenderer(window,
                                               200,
                                               200,
                                               250,
                                               250)
                                               """
    some_square = square_new.Square_New(window, 250, 250, 200, 250, 200, 200, 250, 200,
                                        100, 100, 50,
                                        20, 20, 550, 550, 450, 265)

    running = True
    is_moving = False
    mouse_x_prev = 0
    mouse_y_prev = 0
    x, y = ctypes.c_int(0), ctypes.c_int(0)  # Create two ctypes values
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                if some_square.is_in_figure(x.value, y.value):
                    is_moving = True
                    mouse_x_prev = x.value
                    mouse_y_prev = y.value
            if event.type == sdl2.SDL_MOUSEMOTION:
                if is_moving:
                    sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
                    some_square.move(x.value - mouse_x_prev, y.value - mouse_y_prev)
                    mouse_x_prev = x.value
                    mouse_y_prev = y.value
            if event.type == sdl2.SDL_MOUSEBUTTONUP:
                is_moving = False
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_WINDOWEVENT:
                if event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
                    some_square.clear()
                    #application_renderer.update_coordinates(event.window.data1,
                    #                                        event.window.data2)
        #application_renderer.render()
        #some_square.draw()
        some_square.move_themself()
        do_something(some_square)
        #some_square.print_coords()
        sdl2.SDL_Delay(100)
    sdl2.ext.quit()
    return 0

def do_something(squ):
    squ.draw()

def create_window():
    return sdl2.ext.Window(config.WINDOW_TITLE,
                           size=(config.WINDOW_WIDTH,
                                 config.WINDOW_HEIGHT),
                           flags=sdl2.SDL_WINDOW_RESIZABLE)

if __name__ == "__main__":
    sys.exit(run())

