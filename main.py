import pygame
import MineField
import Consts
import Screen

def main():
    pygame.init()

    screen_timer = 0
    was_pressed = False

    while True:

        if (pygame.time.get_ticks() - screen_timer)/1000 < 0.5 and was_pressed:
            Screen.create_dark_surface()
        else:
            was_pressed = False
            Screen.create_light_surface()
        pygame.display.flip()
        pygame.display.update()

        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen_timer = pygame.time.get_ticks()
                    was_pressed = True


if __name__ == '__main__':
    main()
