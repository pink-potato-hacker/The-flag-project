import pygame
import MineField
import Consts
import Screen
import Soldier


def main():
    pygame.init()

    screen_timer = 0
    was_pressed = False
    soldier_x_location = Consts.SOLIDER_STARTING_PLACE[0]
    soldier_y_location = Consts.SOLIDER_STARTING_PLACE[-1]

    while True:

        if (pygame.time.get_ticks() - screen_timer) / 1000 < 0.5 and was_pressed:
            Screen.create_dark_surface()
            Soldier.placing_soldier((soldier_x_location, soldier_y_location))
        else:
            was_pressed = False
            Screen.create_light_surface()
            Soldier.placing_soldier(Soldier.moving_soldier(soldier_x_location, soldier_y_location))
            soldier_x_location = Soldier.moving_soldier(soldier_x_location, soldier_y_location)[0]
            soldier_y_location = Soldier.moving_soldier(soldier_x_location, soldier_y_location)[-1]
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
