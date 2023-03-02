import pygame
from pygame.locals import *
import sys
import math


WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
SCREEN_W = 500
SCREEN_H = 500
SCREEN_S = (SCREEN_W, SCREEN_H)
C_RADIUS = 200
C_THICKNESS = 1
C_COORD = (SCREEN_W/2, SCREEN_H/2)
INITIAL_LINE_END = [(SCREEN_W/2)+C_RADIUS, SCREEN_H/2]
INITIAL_ANGLE = 0


def compute_line_end(angle: float, origin: list=C_COORD, radius: float=C_RADIUS) -> list:
    """Return a coordinate to be used for drawing the line"""
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    new_x = origin[0] + x
    new_y = origin[1] + y
    return [new_x, new_y]


def origin_to_mouse(origin: list=C_COORD):
    """Get and angle from origin to the mouse position"""
    mouse_pos = pygame.mouse.get_pos()
    dist_x = mouse_pos[0] - origin[0]
    dist_y = mouse_pos[1] - origin[1]
    angle = math.atan2(dist_y, dist_x) * (180/math.pi)
    print(f"angle: {angle % 360}")
    return angle % 360


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_S)


    # Line
    line_end_pos = INITIAL_LINE_END
    angle = INITIAL_ANGLE


    # Font
    font = pygame.font.Font(pygame.font.get_default_font(), 24)
    text_surface = font.render("HELLO", True, GREEN)
    

    # Main loop
    while True:

        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        # draw circle
        pygame.draw.circle(
            screen,
            WHITE,
            C_COORD,
            C_RADIUS,
            C_THICKNESS
        )


        line_end_pos = compute_line_end(angle)
        # Get the new line and angle upon clicking left mouse
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_focused():
            angle = origin_to_mouse()
            line_end_pos = compute_line_end(angle)


        # draw line (antialiased)
        pygame.draw.aaline(
            screen,
            RED,
            C_COORD,
            INITIAL_LINE_END
        )

        pygame.draw.aaline(
            screen,
            GREEN,
            C_COORD,
            line_end_pos
        )


        # render the text to the surface
        text_surface = font.render(f"ANGLE: {angle} DEG", True, GREEN)
        screen.blit(text_surface, (0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()
    