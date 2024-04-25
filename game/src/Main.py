import sys
import time

import pygame as pg

from utils.button import Button as Btn

pg.init()
pg.mixer.init()

SCREEN_HEIGHT = 1024
SCREEN_WIDTH = 1024
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)
SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.FULLSCREEN)
PLAYER_SIZE = 50
FPS = 60

pg.mixer.music.load("../tools/assets/sounds/music/Ryu's Theme.mp3")
pg.mixer.music.play(loops=-1)


def getFont(size):
    return pg.font.Font("../tools/assets/fonts/font.ttf", size)

def play():
    pg.mixer.music.pause()
    trail_positions = [(SCREEN_WIDTH * 0.3), (SCREEN_WIDTH * 0.5), (SCREEN_HEIGHT * 0.7)]

    player_y = SCREEN_HEIGHT // 3

    clock = pg.time.Clock()

    SCREEN.fill((0, 135, 206))

    player_index = 1
    player_pos = [trail_positions[player_index], player_y]
    last_player_index = player_index

    while True:

        CURSOR_POS = pg.mouse.get_pos()

        PLAY_BACK = Btn(image=None, pos=(512, 460), text_input="BACK", font=getFont(75), base_color="White",
                        hovering_color="Green")

        PLAY_BACK.changeColor(CURSOR_POS)
        PLAY_BACK.update(SCREEN)

        keys = pg.key.get_pressed()

        for event in pg.event.get():
            if keys[pg.K_ESCAPE]:
                pause_game()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(CURSOR_POS):
                    main_menu()

        if keys[pg.K_a]:
            player_index = max(player_index - 1, 0)
        if keys[pg.K_d]:
            player_index = min(player_index + 1, len(trail_positions) - 1)

        if player_index != last_player_index:
            player_pos = [trail_positions[player_index], player_y]
            last_player_index = player_index

        if player_index == last_player_index:
            draw_player(player_pos, SCREEN)

        pg.display.update()
        clock.tick(FPS)

def draw_player(player_pos, screen):
    player_image = pg.image.load('../tools/assets/images/boat.png')
    screen.blit(player_image, (player_pos[0], player_pos[1]))

def pause_game():
    pg.mixer.music.pause()

def options():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = getFont(45).render("OPTIONS Screen", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(512, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Btn(image=None, pos=(512, 460), text_input="BACK", font=getFont(75), base_color="Black",
                           hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pg.display.update()


def loadData():
    while True:
        CURSOR_POS = pg.mouse.get_pos()

        SCREEN.fill("Blue")

        LOAD_DATA_TEXT = getFont(45).render("CREDITS Screen", True, "White")
        LOAD_DATA_RECT = LOAD_DATA_TEXT.get_rect(center=(512, 260))
        SCREEN.blit(LOAD_DATA_TEXT, LOAD_DATA_RECT)

        LOAD_DATA_BACK = Btn(image=None, pos=(512, 460), text_input="BACK", font=getFont(75), base_color="White",
                             hovering_color="Green")

        LOAD_DATA_BACK.changeColor(CURSOR_POS)
        LOAD_DATA_BACK.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if LOAD_DATA_BACK.checkForInput(CURSOR_POS):
                    main_menu()

        pg.display.update()


def credits():
    while True:
        CURSOR_POS = pg.mouse.get_pos()

        SCREEN.fill("Blue")

        CREDITS_TEXT = getFont(45).render("CREDITS Screen", True, "White")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(512, 260))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

        CREDITS_BACK = Btn(image=None, pos=(512, 460), text_input="BACK", font=getFont(75), base_color="White",
                           hovering_color="Green")

        CREDITS_BACK.changeColor(CURSOR_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CURSOR_POS):
                    main_menu()

        pg.display.update()


def main_menu():
    while True:
        BG = pg.image.load('../tools/assets/images/menu/game.jpg').convert()
        SCREEN.blit(BG, (0, 0))

        CURSOR_POS = pg.mouse.get_pos()

        MENU_TEXT = getFont(100).render("Main Menu", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(512, 100))

        PLAY_BUTTON = Btn(image=pg.image.load("../tools/assets/images/menu/rects/h2Rect.png"), pos=(256, 450),
                          text_input="PLAY", font=getFont(50), base_color="#d7fcd4", hovering_color="White")

        LOAD_DATA_BUTTON = Btn(image=pg.image.load("../tools/assets/images/menu/rects/h2Rect.png"), pos=(256, 550),
                               text_input="LOAD DATA", font=getFont(50), base_color="#d7fcd4", hovering_color="White")

        OPTIONS_BUTTON = Btn(image=pg.image.load("../tools/assets/images/menu/rects/h2Rect.png"), pos=(768, 450),
                             text_input="OPTIONS", font=getFont(50), base_color="#d7fcd4", hovering_color="White")

        CREDITS_BUTTON = Btn(image=pg.image.load("../tools/assets/images/menu/rects/h2Rect.png"), pos=(768, 550),
                             text_input="CREDITS", font=getFont(50), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Btn(image=pg.image.load("../tools/assets/images/menu/rects/h1Rect.png"), pos=(512, 750),
                          text_input="QUIT", font=getFont(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, LOAD_DATA_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(CURSOR_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(CURSOR_POS):
                    play()
                if LOAD_DATA_BUTTON.checkForInput(CURSOR_POS):
                    loadData()
                if OPTIONS_BUTTON.checkForInput(CURSOR_POS):
                    options()
                if CREDITS_BUTTON.checkForInput(CURSOR_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(CURSOR_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()


main_menu()
pg.mixer.music.stop()
