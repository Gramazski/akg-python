import sys
import sdl2
import sdl2.ext
import config
import drawing


def run():
    sdl2.ext.init()

    window = create_window()
    window.show()
    application_renderer = drawing.ApplicationRenderer(window,
                                               config.WINDOW_WIDTH,
                                               config.WINDOW_HEIGHT,
                                               config.WINDOW_WIDTH / 5,
                                               config.WINDOW_HEIGHT / 2)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_WINDOWEVENT:
                if event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
                    application_renderer.update_coordinates(event.window.data1,
                                                            event.window.data2)
        application_renderer.render()
        sdl2.SDL_Delay(100)
    sdl2.ext.quit()
    return 0


def create_window():
    return sdl2.ext.Window(config.WINDOW_TITLE,
                           size=(config.WINDOW_WIDTH,
                                 config.WINDOW_HEIGHT),
                           flags=sdl2.SDL_WINDOW_RESIZABLE)

if __name__ == "__main__":
    sys.exit(run())

