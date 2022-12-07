import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
import sys
import time
import tkinter as tk

#Colors used in the program 
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTRED = (255, 153, 153)
GREEN = (0, 204, 0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
MELLONCOL = (0, 102, 204)
LIGHTGREEN = (153, 255, 153)
LIGHTPURPLE = (15, 153,255)
PINK = (155,153,204)
PURPLE = (185, 58, 142)
LIGHTPINK = (243, 92, 157)
TAN = (208, 134, 112)
AQUA = (139, 191, 185)



def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

"""class hide(tk.Tk):
  def __init__(self):
    super().__init__()
    canvas = tk.Canvas(self)
    canvas.pack()
    self.level_3 = tk.Button(canvas, text = "Hello", background = 'white', font = ("Helvetica"), command = lambda: self.hide_me(self.level_3))
    self.levle_3.place(x=150, y=100)

  def hide_me(self, event):
    print('hide me')
    event.place_forget()
"""
class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

class Player:
    """ Stores information about a player """

    def __init__(self, score=0, lives=3, current_level=1):
        self.score = score
        self.lives = lives
        self.current_level = current_level


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            player = Player()
            game_state = level_1(screen, player)

        if game_state == GameState.NEXT_LEVEL_2:
            player.current_level += 1
            game_state = level_2(screen, player)

        if game_state == GameState.NEXT_LEVEL_3:
          player.current_level += 1
          game_state = level_3(screen, player)

        if game_state == GameState.FINAL:
          player.score = 50
          game_state = final(screen, player)
        
        if game_state == GameState.BETWEEN1_2:
          player.score += 10
          game_state = between_level1_2(screen, player)

        if game_state == GameState.BETWEEN2_3: 
          player.score += 20
          game_state = between_level2_3(screen, player)

        if game_state == GameState.FAIL_SCREEN1:
          game_state = fail_screen1(screen)

        if game_state == GameState.FAIL_SCREEN2:
          game_state = fail_screen2(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return


def title_screen(screen): # Title Screen 
    title_btn = UIElement(
      center_position = (400,200),
      font_size = 50,
      bg_rgb = BLUE,
      text_rgb = WHITE,
      text = "The World's Easiest Game",
      action = None,
    )
    start_btn = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(title_btn, start_btn, quit_btn)

    return game_loop(screen, buttons)

def fail_screen1(screen): # Fail Screen for Level 1
    title_btn = UIElement(
      center_position = (400,200),
      font_size = 23,
      bg_rgb = RED,
      text_rgb = WHITE,
      text = "You utterly obliterated the entire human race.",
      action = None,
    )
    startAgain_btn = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb= BLUE,
        text_rgb= WHITE,
        text="Restart",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb= BLUE,
        text_rgb= WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    return_btn = UIElement(
        center_position = (400, 400),
        font_size = 30, 
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "Return to Home",
        action = GameState.TITLE,
    )

    buttons = RenderUpdates(title_btn, startAgain_btn, quit_btn, return_btn)

    return game_loop(screen, buttons)

def fail_screen2(screen): # Fail Screen for Level 2
    title_btn = UIElement(
      center_position = (400,200),
      font_size = 30,
      bg_rgb = RED,
      text_rgb = WHITE,
      text = "Really Dig Deep... You Can Do It",
      action = None,
    )
    startAgain_btn = UIElement(
        center_position=(400, 350),
        font_size=30,
        bg_rgb= BLUE,
        text_rgb= WHITE,
        text="Restart",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb= BLUE,
        text_rgb= WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    return_btn = UIElement(
        center_position = (400, 400),
        font_size = 30, 
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "Return to Home",
        action = GameState.TITLE,
    )

    buttons = RenderUpdates(title_btn, startAgain_btn, quit_btn, return_btn)

    return game_loop(screen, buttons)


def level_1(screen, player): # Level 1
    return_btn = UIElement(
        center_position=(50, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return",
        action=GameState.TITLE,
    )
    
    nextlevel_btn = UIElement(
        center_position=(670, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL_2,
    )
  
    currentlevel_btn = UIElement(
        center_position = (120,20),
        font_size = 20,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = f"Current level ({player.current_level})",
        action = None,
    )
    score = UIElement(
        center_position = (670, 20),
        font_size = 20,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = f"Score: {player.score}",
        action = None,
  )

    q1_btn = UIElement(
        center_position = (400, 100),
        font_size = 20,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = "The world is being invaded by ruthless aliens.",
        action = None,
  )

    q2_btn = UIElement(
        center_position = (400, 140),
        font_size = 19,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = "You are the President. The Department of Defense gives you two buttons.",
        action = None,
  )
    q3_btn = UIElement(
        center_position = (400, 180),
        font_size = 20,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = "What do you do?",
        action = None,
  )
  
    red_btn = UIElement(
        center_position = (400,300),
        font_size = 40,
        bg_rgb = RED,
        text_rgb = WHITE,
        text = "PRESS THE BIG RED BUTTON",
        action = GameState.FAIL_SCREEN1,
    )
    
    green_btn = UIElement(
      center_position = (400,400),
      font_size = 40,
      bg_rgb = GREEN,
      text_rgb = WHITE,
      text = "PRESS THE GREEN BUTTON",
      action = GameState.BETWEEN1_2,
    )
   # for i in range(0,1):
      #play_level.green_btn.hide()#print(green_btn) #button.hide()???
     # time.sleep(1)

    buttons = RenderUpdates(return_btn, nextlevel_btn, q1_btn, q2_btn, q3_btn, currentlevel_btn, score, red_btn, green_btn)

    return game_loop(screen, buttons)

def level_2(screen, player): # Level 2
  return_btn = UIElement(
        center_position=(50, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return",
        action=GameState.TITLE,
    )
  nextlevel_btn = UIElement(
        center_position=(670, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL_3,
    )
  currentlevel_btn = UIElement(
        center_position = (120,20),
        font_size = 20,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = f"Current level ({player.current_level})",
        action = None,
    )

  score = UIElement(
        center_position = (670, 20),
        font_size = 20,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = f"Score: {player.score}",
        action = None,
  )
  
  answer_btn = UIElement(
        center_position = (300, 150),
        font_size = 40,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = "Click the answer: ",
        action = GameState.BETWEEN2_3,
  )
  equation_btn = UIElement(
        center_position = (350, 250),
        font_size = 30,
        bg_rgb = BLUE, 
        text_rgb = WHITE, 
        text = "1 + 2 + 3 - 5 * 20 = _____",
        action = None,
  )
  eqAnswer1_btn = UIElement(
        center_position = (150, 375),
        font_size = 30,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "94",
        action = GameState.FAIL_SCREEN2,
  )
  eqAnswer2_btn = UIElement(
        center_position = (250, 350),
        font_size = 30,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "61",
        action = GameState.FAIL_SCREEN2,
  )
  eqAnswer3_btn = UIElement(
        center_position = (350, 375),
        font_size = 30,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "-95",
        action = GameState.FAIL_SCREEN2,
  )
  eqAnswer4_btn = UIElement(
        center_position = (450, 350),
        font_size = 30,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "-94",
        action = GameState.FAIL_SCREEN2,
  )
  eqAnswer5_btn = UIElement(
        center_position = (550, 375),
        font_size = 30,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "20",
        action = GameState.FAIL_SCREEN2,
  )
  
  buttons = RenderUpdates(return_btn, nextlevel_btn, currentlevel_btn, score, answer_btn, equation_btn, eqAnswer1_btn, eqAnswer2_btn,eqAnswer3_btn, eqAnswer4_btn, eqAnswer5_btn)

  return game_loop(screen, buttons)

def level_3(screen, player): # Level 3
  return_btn = UIElement(
        center_position=(50, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return",
        action=GameState.TITLE,
    )
  finish_btn = UIElement(
        center_position=(720, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Finish",
        action=GameState.FINAL,
    )
  currentlevel_btn = UIElement(
        center_position = (120,20),
        font_size = 20,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = f"Current level ({player.current_level})",
        action = None,
    )
  score = UIElement(
        center_position = (670, 20),
        font_size = 20,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = f"Score: {player.score}",
        action = None,
  )
  
  questionButton = UIElement(
        center_position = (400, 120),
        font_size = 30,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "How are you feeling? ",
        action = None,
  )
  face1 = UIElement (
        center_position = (120, 250), 
        font_size = 40, 
        bg_rgb = MELLONCOL,
        text_rgb = WHITE,
        text = "('_')",
        action = GameState.FINAL,
  )
  face2 = UIElement (
        center_position = (650, 400),
        font_size = 40,
        bg_rgb = TAN, 
        text_rgb = WHITE, 
        text = "¯\_('')_/¯",
        action = GameState.FINAL,
  )
  face3 = UIElement (
        center_position = (350, 200),
        font_size = 40,
        bg_rgb = AQUA, 
        text_rgb = WHITE,
        text = "( ._.)",
        action = GameState.FINAL,
  )
  face4 = UIElement (
        center_position = (500, 500), 
        font_size = 40,
        bg_rgb = LIGHTPINK, 
        text_rgb = WHITE, 
        text = "(-_-)",
        action = GameState.FINAL, 
  )
  face5 = UIElement (
        center_position = (240, 500), 
        font_size = 40,
        bg_rgb = LIGHTPURPLE, 
        text_rgb = WHITE, 
        text = "(>'-')>",
        action = GameState.FINAL, 
  )
  face6 = UIElement (
        center_position = (375, 325), 
        font_size = 40,
        bg_rgb = LIGHTRED, 
        text_rgb = WHITE, 
        text = "(╯°□°)╯~ ┻━┻",
        action = GameState.FINAL, 
  )
  face7 = UIElement (
        center_position = (600, 250), 
        font_size = 40,
        bg_rgb = PURPLE, 
        text_rgb = WHITE, 
        text = "(:P )",
        action = GameState.FINAL, 
  )
  face8 = UIElement (
        center_position = (100, 400), 
        font_size = 40,
        bg_rgb = PINK, 
        text_rgb = WHITE, 
        text = "(^ - ^)",
        action = GameState.FINAL, 
  )
  
  buttons = RenderUpdates(return_btn, finish_btn, currentlevel_btn, questionButton,score, face1, face2, face3, face4, face5, face6, face7, face8)

  return game_loop(screen, buttons)

def final(screen, player):
    title_btn = UIElement(
      center_position = (400,100),
      font_size = 50,
      bg_rgb = BLUE,
      text_rgb = WHITE,
      text = "The World's Easiest Game",
      action = None,
    )
    thanks_btn = UIElement(
      center_position = (400,250),
      font_size = 30,
      bg_rgb = BLUE,
      text_rgb = WHITE,
      text = "Thanks for Playing!",
      action = None,
    )
    startAgain_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb= BLUE,
        text_rgb= WHITE,
        text="Restart",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb= BLUE,
        text_rgb= WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    return_btn = UIElement(
        center_position = (400, 450),
        font_size = 30, 
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = "Return to Home",
        action = GameState.TITLE,
    )
    score_btn = UIElement(
        center_position = (400, 300),
        font_size = 30, 
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = f"Final Score: {player.score}",
        action = GameState.TITLE,
    )
  
    buttons = RenderUpdates(return_btn, quit_btn, startAgain_btn, thanks_btn, title_btn, score_btn)

    return game_loop(screen, buttons)

def between_level1_2(screen, player):
  continue_btn = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Continue",
        action=GameState.NEXT_LEVEL_2,
  )
 
  level_comp = UIElement (
        center_position = (400,150),
        font_size = 50,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = f"Level {player.current_level} Complete! ",
        action = None,
  )

  quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
  score = UIElement(
        center_position = (400, 300),
        font_size = 40,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = f"Score: {player.score}",
        action = None,
  )

  buttons = RenderUpdates(continue_btn, quit_btn, score, level_comp)

  return game_loop(screen, buttons)

def between_level2_3(screen, player):
    continue_btn = UIElement(
        center_position=(400, 450),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Continue",
        action=GameState.NEXT_LEVEL_3,
  )
 
    level_comp = UIElement (
        center_position = (400,150),
        font_size = 50,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = f"Level {player.current_level} Complete! ",
        action = None,
  )

    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    score = UIElement(
        center_position = (400, 300),
        font_size = 40,
        bg_rgb = BLUE, 
        text_rgb = WHITE,
        text = f"Score: {player.score}",
        action = None,
  )

    buttons = RenderUpdates(continue_btn, quit_btn, score, level_comp)

    return game_loop(screen, buttons)

def game_loop(screen, buttons):
    """ Handles game loop until an action is return by a button in the
        buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    NEXT_LEVEL_2 = 2
    NEXT_LEVEL_3 = 3
    FAIL_SCREEN1 = 4
    FAIL_SCREEN2 = 5
    BETWEEN1_2 = 6
    BETWEEN2_3 = 7
    FINAL = 8

if __name__ == "__main__":
    main()