import pygame
from core.utils import load_and_scale, mouse_in_button, read_from_user, show_error_popup
from core.data_manager import get_all_tasks
from core.constants import *
from ui.components.workout_display import WorkoutDisplay

class AerobicsScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        data = get_all_tasks()
        self.display = WorkoutDisplay(screen_manager.screen, data, "cardio", self.screen_manager)
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.display.handle_click(event.pos)

    def draw(self, screen):
        """ Draw all the screen elements (Design)"""
        self.display.draw_workout()
        
        