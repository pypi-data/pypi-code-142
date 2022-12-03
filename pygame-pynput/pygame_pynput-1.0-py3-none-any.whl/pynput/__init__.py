import pygame
pygame.init()
font = pygame.font.SysFont('sansserif', 32)
from pygame import Surface

class Pynput:
    def __init__(self, 
        display: Surface,  
        x_coord: int, 
        y_coord: int, 
        width: int, 
        height: int, 
        text: str = '', 
        color: int | tuple[int] = 200,
        border: int = 1, 
        border_radius: int = 0
    ):
        self.display = display
        self.x = x_coord
        self.y = y_coord
        self.text = text
        self.width = width
        self.height = height
        self.color = color if type(color) == tuple else (color, color, color)
        self.border = border
        self.border_radius = border_radius
        
        self.selected = False

    def draw(self):

        self.display.fill((0, 0, 0))
        label_text = font.render(self.text, 1, self.color)
        self.display.blit(label_text, (self.x + 10, self.y + self.height / 2 - 8))
        pygame.draw.rect(
            self.display, 
            self.color, 
            (self.x, self.y, self.width, self.height), 
            self.border, 
            self.border_radius
        )

    def click(self):
        self.selected = not self.selected
        
        if self.selected: self.color = tuple(min(i + 70, 255) for i in self.color)
        else:             self.color = tuple(max(i - 70, 0) for i in self.color)

    def handle_input(self, event):
        if self.selected:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pygame.K_RETURN:
                return self.text if len(self.text) > 0 else None
            else:
                self.text += str(event.unicode)
                
        return None
