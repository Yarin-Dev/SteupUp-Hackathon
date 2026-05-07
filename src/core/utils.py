import pygame

from core.constants import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def mouse_in_button(button, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


def draw_text_box(position, size):
    pygame.draw.rect(screen, WHITE,
                     pygame.Rect(position, size))
    pygame.display.flip()


def read_from_user(position: tuple[int, int], size: tuple[int, int]):
    """
    Read the comment the user type.
    :position: tuple[int, int]
        The cord to place in (x, y)
    :return: string
        return typed comment
    """
    pressed_enter = False
    text = ""
    draw_text_box(position, size)
    while not pressed_enter:
        # get the string for comment
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                draw_text_box(position, size)
                if event.key == pygame.K_RETURN:
                    pressed_enter = True
                # command to add len ! = 0
                elif event.key == pygame.K_BACKSPACE \
                        and not (len(text) == 0):
                    text = text[:-1]
                else:
                    text += event.unicode
                    
                font2 = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=False)
                img2 = font2.render(text, True, (50, 50, 50))
                screen.blit(img2, (position[0] + 10, position[1] + 20))
                
                pygame.display.update()
    return text


def load_and_scale(path: str, width: int, height: int):
    """
    Load and scale an image.

    :param path: str
        Image path on the project folder
    :param width: int
        Image new width
    :param height: int
        Image new height
    :return: Surface
        The element
    """
    image = pygame.image.load(path)
    return pygame.transform.scale(image,
                                        (width, height))


def show_error_popup(message: str):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24, bold=True)
    small_font = pygame.font.SysFont("arial", 20)

    popup_width, popup_height = 400, 200
    screen_rect = screen.get_rect()
    popup_rect = pygame.Rect(
        (screen_rect.centerx - popup_width // 2,
         screen_rect.centery - popup_height // 2),
        (popup_width, popup_height)
    )

    button_width, button_height = 120, 40
    button_rect = pygame.Rect(
        popup_rect.centerx - button_width // 2,
        popup_rect.bottom - button_height - 20,
        button_width,
        button_height
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    running = False


        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 255, 255, 100))  # שחור שקוף
        screen.blit(overlay, (0, 0))


        pygame.draw.rect(screen, (255, 255, 255), popup_rect, border_radius=10)
        pygame.draw.rect(screen, (200, 0, 0), popup_rect, width=3, border_radius=10)


        text_surface = font.render("Error", True, (200, 0, 0))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 20))


        message_lines = message.split("\n")
        for i, line in enumerate(message_lines):
            line_surface = small_font.render(line, True, (0, 0, 0))
            screen.blit(line_surface, (popup_rect.x + 20, popup_rect.y + 60 + i * 25))

        pygame.draw.rect(screen, (220, 220, 220), button_rect, border_radius=8)
        pygame.draw.rect(screen, (120, 120, 120), button_rect, 2, border_radius=8)
        button_text = small_font.render("OK!", True, (0, 0, 0))
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        pygame.display.update()
        clock.tick(30)
