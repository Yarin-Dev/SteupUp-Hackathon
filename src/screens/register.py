import pygame
from core.utils import load_and_scale, mouse_in_button, read_from_user, show_error_popup
from core.data_manager import sign_up
from core.constants import *
from core.ui_config import login_button, move_to_signup_button, username_input, password_input

class RegisterScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.username = None
        self.password = None
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    # Login button click check
                    if mouse_in_button(login_button, mouse_pos):
                        
                        # If username or password not provided, raise an error.
                        if self.username is None or self.password is None:
                            show_error_popup("Please provide password and username to sign-up.")
                        
                        else:
                            # Trying to sign-in
                            success, data = sign_up(self.username, self.password)
                            print(success, data)
                            
                            # If failed, fetch an error message
                            if success is False:
                                show_error_popup(data)
                            
                            # If success, move user to another screen
                            else:
                                self.screen_manager.set_screen("login")

                    # Move-to-sign-up button click check
                    elif mouse_in_button(move_to_signup_button, mouse_pos):
                        self.screen_manager.set_screen("login")
                    
                    # Username text box check
                    elif mouse_in_button(username_input, mouse_pos):
                        self.username = read_from_user((LOGIN_USERNAME_X, LOGIN_USERNAME_Y), (LOGIN_INPUT_WIDTH, LOGIN_INPUT_HEIGHT))
                    
                    # Password text box check
                    elif mouse_in_button(password_input, mouse_pos):
                        self.password = read_from_user((LOGIN_PASSWORD_X, LOGIN_PASSWORD_Y), (LOGIN_INPUT_WIDTH, LOGIN_INPUT_HEIGHT))

    def draw(self, screen):
        """ Draw all the screen elements (Design)"""
        
        # Main background
        background = load_and_scale('assets/signup-bg.png', WINDOW_WIDTH, WINDOW_HEIGHT)
        screen.blit(background, (0, 0))
        
        # Username & Password text
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=False)
        username_text = font.render(self.username, True, (50, 50, 50))
        screen.blit(username_text, (LOGIN_USERNAME_X + 10, LOGIN_USERNAME_Y + 20))

        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=False)
        password_text = font.render(self.password, True, (50, 50, 50))
        screen.blit(password_text, (LOGIN_PASSWORD_X + 10, LOGIN_PASSWORD_Y + 20))
