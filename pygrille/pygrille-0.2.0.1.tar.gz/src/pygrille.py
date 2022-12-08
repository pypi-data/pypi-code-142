try:
    import os
    import random
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Please use a standard Windows version of Python to use Pygrille.")
try:
    import pygame
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Pygame is required for the use of Pygrille. Please install it for Pygrille to work correctly.")
from text import Text


class Pixel:
    def __init__(self, x_pos: int, y_pos: int, colour: tuple, extras: list = None, image: pygame.Surface = None):
        if extras is None:
            extras = []
        self.colour = colour
        self.extras = dict.fromkeys(extras)
        self.label = (x_pos, y_pos)
        self.pos = (x_pos, y_pos)
        self.image = image

    def __repr__(self):
        return str(self.label)


class Grid:
    def __init__(self, pixel_size: int, grid_dimensions: tuple, *, window_name: str = None,
                 default_colour: tuple = None, extras: list = None, framerate: int = None, border_width: int = None,
                 border_colour: tuple = None, default_image: str = None, display_offset_x: int = 0,
                 display_offset_y: int = 0, forced_window_size: tuple = None):
        if window_name is None:
            window_name = "pygrille window"
        if framerate is None:
            framerate = 60
        if border_width is None:
            border_width = 0
        if border_colour is None:
            border_colour = (100, 100, 100)
        if default_image is not None:
            default_image = self.load_image(default_image, pixel_size)
        grid_dimensions = (grid_dimensions[1], grid_dimensions[0])
        pygame.init()
        pygame.display.set_caption(window_name)
        screen_size = [2 * border_width + i * pixel_size + (i - 1) * border_width for i in grid_dimensions]
        if forced_window_size is not None:
            screen = pygame.display.set_mode((forced_window_size[0], forced_window_size[1]))
        else:
            screen = pygame.display.set_mode((screen_size[1], screen_size[0]))
        if extras is None:
            extras = []
        if default_colour is None:
            default_colour = (0, 0, 0)
        self.screen = screen
        self.size = grid_dimensions
        self.default_colour = default_colour
        self.pixel_size = pixel_size
        self.extra_list = extras
        self.framerate = framerate
        self.lastclick = None
        self.newclick = False
        self.lastkey = None
        self.keylist = []
        self.newkey = False
        self.ui = {}
        self.screen_size = screen_size
        self.border_width = border_width
        self.border_colour = border_colour
        self.default_image = default_image
        self.grid = list(
            zip(*[[Pixel(i, j, default_colour, extras, default_image) for i in range(grid_dimensions[1])] for j in
                  range(grid_dimensions[0])]))
        self.clock = pygame.time.Clock()
        self.display_offset_x = display_offset_x
        self.display_offset_y = display_offset_y
        self.images = {}
        self.text = {}
        self.screenrect = pygame.Rect(0, 0, self.screen.get_size()[0], self.screen.get_size()[1])
        self.backgroundimage = None
        self.draw()

    def __repr__(self):
        return "\n".join([str(row) for row in self.grid])

    def __getitem__(self, key):
        return self.grid[key]

    def draw_borders(self):
        for i in range(len(self.grid)):
            pass

    def draw(self, *, flip: bool = None):
        if flip is None:
            flip = True
        if self.backgroundimage is not None:
            self.screen.blit(self.backgroundimage, (0, 0))
        else:
            self.screen.fill(self.border_colour)
        for i, node_row in enumerate(self.grid):
            for j, node in enumerate(node_row):
                rect = pygame.Rect(
                    self.border_width + i * self.pixel_size + i * self.border_width + self.display_offset_x,
                    self.border_width + j * self.pixel_size + + j * self.border_width + self.display_offset_y,
                    self.pixel_size, self.pixel_size)
                pygame.draw.rect(self.screen, node.colour, rect)
                if node.image is not None:
                    rect = node.image.get_rect()
                    rect.x = self.border_width + i * self.pixel_size + i * self.border_width + self.display_offset_x
                    rect.y = self.border_width + j * self.pixel_size + + j * self.border_width + self.display_offset_y
                    self.screen.blit(node.image, rect)
        for i in self.ui.values():
            self.screen.blit(i["image"], i["coords"])
        for i in self.text.values():
            i.draw(self.screen)
        if flip:
            pygame.display.flip()

    def update(self, coords: tuple, *, colour: tuple = None, label: str = None, draw: bool = None,
               border_colour: tuple = None, **kwargs):
        if draw is None:
            draw = False
        if colour is not None:
            self.grid[coords[0]][coords[1]].colour = colour
        if label is not None:
            self.grid[coords[0]][coords[1]].label = label
        if border_colour is not None:
            self.border_colour = border_colour
        for item in kwargs:
            if item in self.extra_list:
                self.grid[coords[0]][coords[1]].extras[item] = kwargs[item]
            else:
                raise KeyError(f"\"{item}\" does not exist in the possible extras for this pixel")
        if draw:
            self.draw()

    def tick(self):
        self.clock.tick(self.framerate)

    def check_open(self):
        self.newclick = False
        self.newkey = False
        self.keylist = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pos[0] - self.border_width - self.display_offset_x) % (
                        self.pixel_size + self.border_width) <= self.pixel_size and (
                        pos[1] - self.border_width - self.display_offset_y) % (
                        self.pixel_size + self.border_width) <= self.pixel_size:
                    self.lastclick = ((pos[0] - self.display_offset_x) // (self.pixel_size + self.border_width),
                                      (pos[1] - self.display_offset_y) // (self.pixel_size + self.border_width))
                    self.newclick = True
            elif event.type == pygame.KEYDOWN:
                self.keylist.append(pygame.key.name(event.key))
                self.lastkey = pygame.key.name(event.key)
                self.newkey = True
        return True

    def set_image(self, pos: tuple, image_path: str):
        if image_path not in self.images.keys():
            self.images[image_path] = self.load_image(image_path, self.pixel_size)
        self.grid[pos[0]][pos[1]].image = self.images[image_path]

    def set_ui(self, name: str, image_path: str, window_coords: tuple, scale: tuple = None):
        if image_path not in self.images.keys():
            self.images[image_path] = pygame.image.load(image_path)
        image = self.images[image_path]
        if scale is not None:
            image = pygame.transform.scale(image, (scale[0], scale[1]))
        self.ui[name] = {
            "image": image,
            "coords": window_coords,
            "path": image_path}

    def set_text(self, name: str, font: str = None, size: int = None, text: str = None, pos: tuple = None,
                 colour: tuple = None):
        if font is None:
            font = "Arial"
        if size is None:
            size = 30
        if text is None:
            text = ""
        if pos is None:
            pos = (0, 0)
        if colour is None:
            colour = (0, 0, 0)
        self.text[name] = Text(font, size, text, pos, colour)

    def get_text(self, name: str):
        if name in self.text.keys():
            return self.text[name]

    def del_text(self, name: str):
        self.text.pop(name)

    def del_ui(self, name: str):
        self.ui.pop(name)

    def set_background_image(self, image_path: str):
        if image_path not in self.images.keys():
            self.images[image_path] = pygame.image.load(image_path)
        image = self.images[image_path]
        scale = self.screen.get_size()
        image = pygame.transform.scale(image, (scale[0], scale[1]))
        self.backgroundimage = image

    def pixel_from_screen_pixel(self, x: int, y: int):
        if (x - self.border_width - self.display_offset_x) % (
                self.pixel_size + self.border_width) <= self.pixel_size and (
                y - self.border_width - self.display_offset_y) % (
                self.pixel_size + self.border_width) <= self.pixel_size:
            pixel = (int((x - self.display_offset_x) // (self.pixel_size + self.border_width)),
                     int((y - self.display_offset_y) // (self.pixel_size + self.border_width)))
            return pixel

    def screen_pixel_from_pixel(self, x: int, y: int):
        x = self.border_width + x * self.pixel_size + x * self.border_width + self.display_offset_x
        y = self.border_width + y * self.pixel_size + y * self.border_width + self.display_offset_y
        return (x, y)

    def load_image(self, image_path, pixel_size):
        return pygame.transform.scale(pygame.image.load(image_path), (pixel_size, pixel_size))

    def quit(self):
        pygame.quit()


def random_colour():
    return [random.randint(0, 255) for i in range(3)]
