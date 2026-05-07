import pygame
from core.data_manager import get_all_tasks
from ui.components.workout_display import WorkoutDisplay


class StrengthScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        data = get_all_tasks()
        self.display = WorkoutDisplay(screen_manager.screen, data, "strength", self.screen_manager)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.display.handle_click(event.pos)

    def draw(self, screen):
        """ Draw all the screen elements (Design)"""
        self.display.draw_workout()

