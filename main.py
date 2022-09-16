import pygame
import MineField
import Consts
import Music
import Screen
import Soldier


def main():
    global event
    pygame.init()
    Music.background_music()
    screen_timer = 0
    message_timer = pygame.time.get_ticks()

    was_pressed = False

    soldier_x_location = Consts.SOLIDER_STARTING_PLACE[0]
    soldier_y_location = Consts.SOLIDER_STARTING_PLACE[1]

    MineField.create_empty_mine_field()
    MineField.randomize_mines()
    MineField.randomize_grass()
    MineField.randomize_bushes()
    MineField.randomize_flower()
    MineField.put_flag()

    while True:
        moved = False

        if (pygame.time.get_ticks() - screen_timer) / 1000 < 0.5 and was_pressed:
            Screen.create_dark_surface()
            Soldier.placing_night_soldier((soldier_x_location, soldier_y_location))

        else:
            was_pressed = False
            Screen.create_light_surface()
            Soldier.placing_day_soldier((soldier_x_location, soldier_y_location))

        if (pygame.time.get_ticks() - message_timer) / 1000 < 2:
            Screen.welcome_text()

        pygame.display.flip()
        pygame.display.update()

        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return[]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen_timer = pygame.time.get_ticks()
                    was_pressed = True

                elif event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT,
                                   pygame.K_DOWN] and not moved and not was_pressed:

                    soldier_x_location, soldier_y_location = Soldier.moving_soldier(soldier_x_location,
                                                                                    soldier_y_location, event.key)

                    moved = True
            elif event.type == pygame.KEYUP and not was_pressed:
                if event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]:
                    moved = False

        Screen.create_light_surface()
        Soldier.placing_day_soldier((soldier_x_location, soldier_y_location))
        win_or_lose = MineField.win_or_lose(soldier_x_location, soldier_y_location)
        MineField.put_solider_in_matrix(soldier_x_location, soldier_y_location)

        if win_or_lose != 0:
            message_won_lose_timer = pygame.time.get_ticks()
            if win_or_lose == 2:
                while (pygame.time.get_ticks() - message_won_lose_timer) / 1000 < 3:
                    Screen.win_text()
                break

            elif win_or_lose == 1:
                Soldier.placing_dead_solider((soldier_x_location, soldier_y_location))
                while (pygame.time.get_ticks() - message_won_lose_timer) / 1000 < 3:
                    Screen.lose_text()
                break


if __name__ == '__main__':
    main()
