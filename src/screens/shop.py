import pygame
from core.utils import load_and_scale, mouse_in_button
from core.data_manager import get_coins
from core.constants import *
from core.ui_config import shop_back_button

class ShopScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_in_button(shop_back_button, mouse_pos):
                    self.screen_manager.set_screen("menu")

    def draw(self, screen):
        """ Draw all the screen elements (Design)"""

        # Main background
        background = load_and_scale('assets/shop-bg.png', WINDOW_WIDTH, WINDOW_HEIGHT)
        screen.blit(background, (0, 0))

        # Coins text
        font = pygame.font.SysFont('chalkduster.ttf', 90, bold=True)
        coins_text = font.render(str(get_coins(self.screen_manager.username)), True, (250, 250, 250))
        screen.blit(coins_text, (COINS_POSITION[0] - 15, COINS_POSITION[1] + 20))
