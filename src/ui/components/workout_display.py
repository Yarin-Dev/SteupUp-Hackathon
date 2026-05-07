import pygame
import time
from core.data_manager import add_coins
from core.utils import load_and_scale
from enum import Enum


class WorkoutState(Enum):
    IDLE = "idle"
    ACTIVE = "active"
    REST = "rest"
    DONE = "done"
    COMPLETED = "completed"

class WorkoutDisplay:
    def __init__(self, screen, workouts, workout_type, screen_manager):
        self.screen = screen
        self.workouts = workouts[workout_type]
        self.current = 0
        self.font = pygame.font.SysFont(None, 32)
        self.state = WorkoutState.IDLE
        self.timer_start = None
        self.workout_type = workout_type
        self.button_rect = pygame.Rect(300, 500, 120, 40)
        self.menu_button_rect = pygame.Rect(700, 500, 190, 50)
        self.screen_manager = screen_manager
        self.completion_time = None

    def draw_text(self, text, pos, color=(0, 0, 0)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, pos)

    def draw_workout(self):
        self.screen.fill((240, 240, 240))
        workout = self.workouts[self.current]

        # Draw box with reduced size
        box_rect = pygame.Rect(100, 100, 500, 300)  # Reduced box size
        pygame.draw.rect(self.screen, (200, 220, 255), box_rect, border_radius=12)

        # Text info (without image)
        x_text = box_rect.x + 20
        y = box_rect.y + 20
        self.draw_text(f"Name: {workout['name']}", (x_text, y))
        coins = workout['coins']
        img_path = workout['image']
        img = load_and_scale(img_path, 500, 300)
        self.screen.blit(img, (624, 100))

        if self.workout_type == "strength":
            self.draw_text(f"Sets: {workout['sets']}", (x_text, y + 40))
            self.draw_text(f"Reps: {workout['reps']}", (x_text, y + 80))
            self.draw_text(f"Rest: {workout['rest_seconds']} sec", (x_text, y + 120))
            self.draw_text(f"Coins: {coins}", (x_text, y + 160))
            duration = 5
            rest = workout['rest_seconds']
        else:
            self.draw_text(f"Duration: {workout['duration']} sec", (x_text, y + 40))
            self.draw_text(f"Rest: {workout['rest']} sec", (x_text, y + 80))
            self.draw_text(f"Coins: {coins}", (x_text, y + 120))
            duration = workout['duration']
            rest = workout['rest']

        # Timer section
        if self.state in [WorkoutState.ACTIVE, WorkoutState.REST]:
            elapsed = int(time.time() - self.timer_start)
            total_time = duration if self.state == WorkoutState.ACTIVE else rest
            remaining = max(0, total_time - elapsed)
            self.draw_text(f"{'Workout' if self.state == 'active' else 'Rest'}: {remaining}s", (x_text, y + 180))
            if remaining == 0:
                if self.state == WorkoutState.ACTIVE:
                    self.state = WorkoutState.REST
                    self.timer_start = time.time()
                else:
                    self.state = WorkoutState.DONE
                    add_coins(self.screen_manager.username, coins)
                    self.completion_time = time.time()
        elif self.state == WorkoutState.DONE:
            self.draw_text(f"Mission done! You earned {coins} coins.", (x_text, y + 200), color=(0, 150, 0))

            # Check if 4 seconds have passed since completion
            if self.completion_time and time.time() - self.completion_time > 4:
                self.current += 1
                if self.current < len(self.workouts):
                    self.state = WorkoutState.IDLE
                    self.button_rect = pygame.Rect(300, 500, 120, 40)
                else:
                    self.state = WorkoutState.COMPLETED

        # Start Button
        if self.state == WorkoutState.IDLE:  # Show button only in idle state
            pygame.draw.rect(self.screen, (100, 200, 100), self.button_rect, border_radius=8)
            self.draw_text("Start", (self.button_rect.x + 32, self.button_rect.y + 10))
        
        # Menu Button (Back to menu)
        pygame.draw.rect(self.screen, (200, 100, 100), self.menu_button_rect, border_radius=8)
        self.draw_text("Back to Menu", (self.menu_button_rect.x + 20, self.menu_button_rect.y + 15))

    def handle_click(self, pos):
        # Start button check
        if self.button_rect.collidepoint(pos) and self.state == WorkoutState.IDLE:
            self.state = WorkoutState.ACTIVE
            self.timer_start = time.time()
            # Hide the button after clicking
            self.button_rect = pygame.Rect(-100, -100, 0, 0)
        
        # Back-to-menu button check
        if self.menu_button_rect.collidepoint(pos):
            self.screen_manager.set_screen("menu")
