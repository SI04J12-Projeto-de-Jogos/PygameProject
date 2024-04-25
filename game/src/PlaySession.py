import pygame as pg
import utils.button as Btn

from game.src.Main import getFont

# Initialize Pygame
pg.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Ocean background function
def draw_ocean_background():
    ocean_image = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    ocean_image.fill((0, 135, 206))  # Light blue color for the ocean
    wave_image = pg.image.load('wave.png')  # Load wave image
    wave_image = pg.transform.scale(wave_image, (SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.5)))

    for x in range(0, SCREEN_WIDTH, wave_image.get_width()):
        SCREEN.blit(wave_image, (x, int(SCREEN_HEIGHT * 0.25)))

# Player settings
PLAYER_SIZE = 50
PLAYER_SPEED = 5

# Player function
def draw_player(x, y):
    player_image = pg.Surface((PLAYER_SIZE, PLAYER_SIZE))
    player_image.fill((255, 255, 255))
    pg.draw.rect(player_image, (255, 0, 0), pg.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE), 3)
    SCREEN.blit(player_image, (x, y))

# Player movement function
def move_player(direction, x, y):
    if direction == 'left':
        x -= PLAYER_SPEED
    elif direction == 'right':
        x += PLAYER_SPEED

    # Limit player position to three trails
    if x < PLAYER_SIZE:
        x = PLAYER_SIZE
    elif x + PLAYER_SIZE > SCREEN_WIDTH - PLAYER_SIZE:
        x = SCREEN_WIDTH - PLAYER_SIZE - PLAYER_SIZE

    return x, y

def play():
    clock = pg.time.Clock()
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    while True:
        CURSOR_POS = pg.mouse.get_pos()

        SCREEN.fill("black")

        draw_ocean_background()

        PLAY_TEXT = getFont(45).render("PLAY Screen", True, "Blue")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(512, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Btn(image=None, pos=(512, 460), text_input="BACK", font=getFont(75), base_color="White",
                        hovering_color="Green")

        PLAY_BACK.changeColor(CURSOR_POS)
        PLAY_BACK.update(SCREEN)

        # Handle player movement
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            x, y = move_player('left', x, y)
        elif keys[pg.K_RIGHT]:
            x, y = move_player('right', x, y)

        draw_player(x, y)

        pg.display.update()
        clock.tick(60)