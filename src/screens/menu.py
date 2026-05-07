import pygame
from core.utils import load_and_scale, mouse_in_button, read_from_user, show_error_popup
from core.data_manager import get_coins
from core.constants import *
from core.ui_config import aerobics_button, strength_button, shop_button


class MenuScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if mouse_in_button(aerobics_button, mouse_pos):
                        self.screen_manager.set_screen("aerobics")
                        
                    elif mouse_in_button(strength_button, mouse_pos):
                        self.screen_manager.set_screen("strength")
                    
                    elif mouse_in_button(shop_button, mouse_pos):
                        self.screen_manager.set_screen("shop")

    def draw(self, screen):
        """ Draw all the screen elements (Design)"""
        
        # Main background
        background = load_and_scale('assets/menu-bg.png', WINDOW_WIDTH, WINDOW_HEIGHT)
        screen.blit(background, (0, 0))

        # Coins text
        font = pygame.font.SysFont('chalkduster.ttf', 60, bold=True)
        coins_text = font.render(str(get_coins(self.screen_manager.username)), True, (250, 250, 250))
        screen.blit(coins_text, COINS_POSITION)

        # Username text
        username_text = font.render(self.screen_manager.username, True, (250, 250, 250))
        screen.blit(username_text, USERNAME_POSITION)
