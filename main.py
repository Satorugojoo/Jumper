import pygame as py
import sys
import time
from pygame.locals import *

mainClock = py.time.Clock()

py.init()
py.display.set_caption('Jumper')
screen = py.display.set_mode((800, 600), 0, 32)
font = py.font.SysFont(None, 40)
font_S = py.font.SysFont(None, 20)
font_B = py.font.SysFont(None, 60)

def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    global click
    while True:

        tlo = py.image.load('tła/tło_menu.png')
        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))

        mx, my = py.mouse.get_pos()

        button_1 = py.Rect(325, 200, 150, 50)
        button_2 = py.Rect(325, 300, 150, 50)
        button_3 = py.Rect(325, 400, 150, 50)
        button_6 = py.Rect(650, 570, 150, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                py.quit()
                sys.exit(0)
        if button_6.collidepoint((mx, my)):
            if click:
                tworcy()

        py.draw.rect(screen, (131, 131, 131), button_1)
        py.draw.rect(screen, (131, 131, 131), button_2)
        py.draw.rect(screen, (131, 131, 131), button_3)
        py.draw.rect(screen, (100, 100, 100), button_6)

        draw_text('GRAJ!', font, (100, 31, 31), screen, 355, 213)
        draw_text('Opcje', font, (100, 31, 31), screen, 355, 311)
        draw_text('Zakończ', font, (100, 31, 31), screen, 345, 412)
        draw_text('Twórcy', font, (120, 30, 30), screen, 675, 573)

        click = False
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    py.quit()
                    sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        py.display.update()
        mainClock.tick(60)


def game():
    global click
    click = False

    running = True

    y_chopek = 480
    x_chopek = 670
    chopek_width = 63
    chopek_height = 64

    level = 0

    y_wrog_1 = 480
    x_wrog_1 = 220
    wrog_width = 46
    wrog_height = 63

    x_nagroda = 20
    y_nagroda = 470
    nagroda_width = 70
    nagroda_height = 50

    move_enemy = 2
    move = 9
    jumpcount = 10
    jump = False

    walk = 0
    left = False
    right = False

    while running:

        mx, my = py.mouse.get_pos()

        if level == 0:
            tlo_1 = py.image.load('tła/tło 1.png')
            chopek = py.image.load('elementy/gracz.png')
            nagroda = py.image.load('elementy/T1.png')
            wrog_1 = py.image.load('elementy/M1.png')
        else:
            chopek = py.image.load('elementy/gracz.png')
            nagroda = py.image.load('elementy/T1.png')
            wrog_1 = py.image.load('elementy/M1.png')
            tlo_1 = py.image.load('tła/tło 2.png')

        button_5 = py.Rect(700, 5, 100, 25)

        screen.fill((0, 0, 0))
        screen.blit(tlo_1, (0, 0))

        py.draw.rect(screen, (168, 177, 217), button_5)
        draw_text('Menu Główne', font_S, (48, 74, 253), screen, 710, 10)

        screen.blit(wrog_1, (x_wrog_1, y_wrog_1, wrog_width, wrog_height))
        screen.blit(chopek, (x_chopek, y_chopek, chopek_width, chopek_height))
        screen.blit(nagroda, (x_nagroda, y_nagroda, nagroda_width, nagroda_height))

        wlewo = [py.image.load('elementy/GL1.png'), py.image.load('elementy/GL2.png'),
                 py.image.load('elementy/GL3.png'), py.image.load('elementy/GL4.png'),
                 py.image.load('elementy/GL5.png'), py.image.load('elementy/GL6.png'),
                 py.image.load('elementy/GL7.png'), py.image.load('elementy/GL8.png'),
                 py.image.load('elementy/GL9.png')]
        wprawo = [py.image.load("elementy/GR1.png"), py.image.load('elementy/GR2.png'),
                  py.image.load('elementy/GR3.png'), py.image.load('elementy/GR4.png'),
                  py.image.load('elementy/GR5.png'), py.image.load('elementy/GR6.png'),
                  py.image.load('elementy/GR7.png'), py.image.load('elementy/GR8.png'),
                  py.image.load('elementy/GR9.png')]

        if walk + 1 >= 27:
            walk = 0
        if left:
            screen.blit(wlewo[walk // 3], (x_chopek, y_chopek))
            walk += 1
        elif right:
            screen.blit(wprawo[walk // 3], (x_chopek, y_chopek))
            walk += 1
        else:
            screen.blit(chopek, (x_chopek, y_chopek))

        py.display.update()
        mainClock.tick(60)

        x_wrog_1 -= move_enemy      # ruch pzeciwnika
        if x_wrog_1 < 200:
            move_enemy *= -1
        elif x_wrog_1 > 600:
            move_enemy *= -1

        keys = py.key.get_pressed()     # ruch gracza
        if (keys[py.K_a] or keys[py.K_LEFT]) and x_chopek > move:
            x_chopek -= move
            left = True
            right = False
        elif (keys[py.K_d] or keys[py.K_RIGHT]) and x_chopek < screen.get_width() - chopek_width:
            x_chopek += move
            right = True
            left = False
        else:
            right = False
            left = False
            walk = move
        if not jump:
            if keys[py.K_SPACE] or keys[py.K_UP] or keys[py.K_w]:
                jump = True
                right = False
                left = False
        else:
            if jumpcount >= -10:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                y_chopek -= (jumpcount ** 2) * 0.5 * neg
                jumpcount -= 1
            else:
                jump = False
                jumpcount = 10

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if (x_chopek < x_wrog_1 + wrog_width) & (x_chopek + chopek_width > x_wrog_1) &\
                (y_chopek + chopek_height >= y_wrog_1):
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(2.0)
            running = False
        if x_chopek < x_nagroda + nagroda_width and x_chopek + chopek_width > x_nagroda \
                and y_chopek >= y_nagroda:

                level = level + 1

                if level == 2:
                    screen.fill((0, 0, 0))
                    draw_text(' Wygrałeś! :) ', font_B, (255, 0, 0), screen, 250, 300)
                    py.display.flip()
                    time.sleep(3.5)
                    running = False
                else:
                    screen.fill((0, 0, 0))
                    x_chopek = 670
                    draw_text(' Gratuluję, kolejny poziom na ciebie czeka  :)', font, (255, 0, 0), screen, 100, 300)
                    py.display.flip()
                    time.sleep(2.0)

                    screen.fill((0, 0, 0))
                    screen.blit(tlo_1, (0, 0))

                    py.draw.rect(screen, (168, 177, 217), button_5)
                    draw_text('Menu Główne', font_S, (48, 74, 253), screen, 710, 10)

                    screen.blit(wrog_1, (x_wrog_1, y_wrog_1, wrog_width, wrog_height))
                    screen.blit(chopek, (x_chopek, y_chopek, chopek_width, chopek_height))
                    screen.blit(nagroda, (x_nagroda, y_nagroda, nagroda_width, nagroda_height))

                    py.display.update()
                    mainClock.tick(60)


                # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

                    if (x_chopek < x_wrog_1 + wrog_width) & (x_chopek + chopek_width > x_wrog_1) & \
                            (y_chopek + chopek_height >= y_wrog_1):
                        screen.fill((0, 0, 0))
                        draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
                        py.display.flip()
                        time.sleep(3.5)
                        running = False
                    if x_chopek < x_nagroda + nagroda_width and x_chopek + chopek_width > x_nagroda \
                        and y_chopek >= y_nagroda:
                        screen.fill((0, 0, 0))
                        draw_text(' Wygrałeś! :) ', font_B, (255, 0, 0), screen, 250, 300)
                        py.display.flip()
                        time.sleep(3.5)
                        running = False

        #obsługa przycisków w tym momencie przycisku Main menu

        if button_5.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        py.display.flip()
        mainClock.tick(60)


def options():
    running = True

    global click
    click = False

    while running:
        mx, my = py.mouse.get_pos()
        screen.fill((0, 0, 0))
        draw_text('Cel gry oraz sterowanie', font, (255, 255, 255), screen, 20, 20)
        button_4 = py.Rect(18, 490, 150, 50)
        py.draw.rect(screen, (255, 0, 0), button_4)
        draw_text(' <-- Powrót ', font, (255, 255, 255), screen, 20, 500)
        draw_text(
            ' Celem gry jest dojście do teleportu, który znajduje się na '
            ' końcu danego poziomu oraz przenisie nas na kolejny.',
            font_S,
            (255, 255, 255), screen, 60, 100)
        draw_text(' Naszą przeprawę urozmaicą przeszkody oraz przeciwnicy z różnymi umiejętnościami. ', font_S,
                  (255, 255, 255), screen, 60, 120)
        draw_text(' Sterowanie: ', font_S, (255, 255, 255), screen, 60, 160)
        draw_text(' A - ruch w lewo', font_S, (255, 255, 255), screen, 60, 190)
        draw_text(' D - ruch w prawo ', font_S, (255, 255, 255), screen, 60, 220)
        draw_text(' W - skok ', font_S, (255, 255, 255), screen, 60, 250)

        if button_4.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        py.display.update()
        mainClock.tick(60)


def tworcy():
    running = True

    global click
    click = False

    while running:
        mx, my = py.mouse.get_pos()
        tlo = py.image.load('tła/tłó_twórcy.png')
        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        draw_text(' PROgramiści: ', font_B, (19, 19, 19), screen, 260, 100)
        draw_text(' Miłosz Kapłanek ', font_B, (155, 69, 29), screen, 230, 200)
        draw_text(' Tomasz Paruzel', font_B, (155, 59, 29), screen, 230, 300)
        button_7 = py.Rect(18, 490, 150, 50)
        py.draw.rect(screen, (148, 176, 255), button_7)
        draw_text(' <-- Powrót ', font, (120, 20, 20), screen, 20, 500)
        if button_7.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        py.display.update()
        mainClock.tick(60)


main_menu()
