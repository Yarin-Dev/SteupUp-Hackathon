from src.screens.login import LoginScreen
from src.screens.register import RegisterScreen
from src.screens.menu import MenuScreen
from src.screens.aerobics import AerobicsScreen
from src.screens.strength import StrengthScreen
from src.screens.shop import ShopScreen


class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.screens = {
            "login": LoginScreen(self),
            "register": RegisterScreen(self),
            "menu": MenuScreen(self),
            "aerobics": AerobicsScreen(self),
            "strength": StrengthScreen(self),
            "shop": ShopScreen(self)
        }
        self.current_screen = self.screens["login"]
        self.username = None

    def set_screen(self, screen_name):
        self.current_screen = self.screens.get(screen_name, self.current_screen)

    def handle_events(self, events):
        self.current_screen.handle_events(events)

    def update(self):
        self.current_screen.update()

    def draw(self):
        self.current_screen.draw(self.screen)
