import pygame
import Database
import MineField
import Consts
import Music
import Screen
import Soldier
import KeyInputs
import Teleport


def main():
    # starting the game
    pygame.init()
    Music.background_music()
    screen_timer = 0
    message_timer = pygame.time.get_ticks()

    was_pressed = False

    soldier_x = Consts.SOLIDER_STARTING_PLACE[0]
    soldier_y = Consts.SOLIDER_STARTING_PLACE[1]

    guard_x = Consts.GUARD_STARTING_PLACE[0]
    guard_y = Consts.GUARD_STARTING_PLACE[1]

    MineField.create_empty()
    MineField.randomize_mines()
    MineField.get_cords_for_elements()
    MineField.put_flag()
    Teleport.randomize_teleports()
    print(Teleport.teleports)

    while True:
        moved = False

        if (pygame.time.get_ticks() - screen_timer) / 1000 < 0.5 and was_pressed:  # dark surface
            Screen.create_dark_surface()
            Soldier.place_soldier((soldier_x, soldier_y), 'night')
        else:  # light surface
            was_pressed = False
            Screen.create_light_surface()
            Soldier.place_soldier((soldier_x, soldier_y))

        if (pygame.time.get_ticks() - message_timer) / 1000 < 2:  # welcome text
            Screen.welcome_text()

        pygame.display.flip()
        pygame.display.update()

        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return []

            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                                 pygame.K_8, pygame.K_9]:  # CSV - (1-9)

                    key = KeyInputs.key_press_timer(event.key)

                    if Database.add_to_file(key):  # load a new game
                        soldier_x = MineField.soldier_locations[0][1] * Consts.SIZE
                        soldier_y = MineField.soldier_locations[0][0] * Consts.SIZE
                    moved = True

                if event.key == pygame.K_RETURN:  # dark surface
                    screen_timer = pygame.time.get_ticks()
                    was_pressed = True

                elif event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT,
                                   pygame.K_DOWN] and not moved and not was_pressed:  # arrows

                    soldier_x, soldier_y = KeyInputs.move_soldier(soldier_x,
                                                                  soldier_y, event.key)
                    is_teleported = Teleport.step_on_teleport(soldier_x, soldier_y)
                    if is_teleported:
                        tel_coords = Teleport.pick_teleport(soldier_x, soldier_y)
                        soldier_x = (tel_coords[1]) * Consts.SIZE
                        soldier_y = (tel_coords[0] - 3) * Consts.SIZE

            elif event.type == pygame.KEYUP and not was_pressed:  # nothing was pressed
                if event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]:
                    moved = False

        # update
        Screen.create_light_surface()
        Soldier.place_soldier((soldier_x, soldier_y), 'day')
        win_or_lose = MineField.win_or_lose(soldier_x, soldier_y)
        MineField.put_solider_in_matrix(soldier_x, soldier_y)

        # win or lose
        if win_or_lose != 0:
            message_won_lose_timer = pygame.time.get_ticks()
            if win_or_lose == 2:
                while (pygame.time.get_ticks() - message_won_lose_timer) / 1000 < 3:
                    Screen.win_text()
                    Music.victory_sound()
                break

            elif win_or_lose == 1:
                Soldier.place_soldier((soldier_x, soldier_y), 'dead')
                while (pygame.time.get_ticks() - message_won_lose_timer) / 1000 < 3:
                    Screen.lose_text()
                    Music.bomb_sound()
                break


if __name__ == '__main__':
    main()
