import pygame
from core.constants import *
from ui.screen_manager import ScreenManager


def main():
    # Set up the game display, clock and headline
    pygame.init()

    pygame.display.set_caption(TITLE_NAME)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    clock = pygame.time.Clock()
    screen_manager = ScreenManager(screen)
    index = 0
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        # Draw screen & events.
        screen_manager.handle_events(events)
        screen_manager.draw()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)

    pygame.quit()
    quit()


main()
