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


class Portal(py.sprite.Sprite):                     # klasa odpowiedzialna za pozycje naszego portalu
    def __init__(self, x, y, width, height):
        super().__init__()
        self.klatki = []
        self.klatki.append(py.image.load('elementy/T1.png'))
        self.klatki.append(py.image.load('elementy/T2.png'))
        self.klatki.append(py.image.load('elementy/T3.png'))
        self.klatki.append(py.image.load('elementy/T4.png'))
        self.klatki.append(py.image.load('elementy/T5.png'))
        self.klatki.append(py.image.load('elementy/T6.png'))
        self.klatki.append(py.image.load('elementy/T7.png'))
        self.klatki.append(py.image.load('elementy/T8.png'))
        self.klatki.append(py.image.load('elementy/T9.png'))
        self.aktualna_klatka = 0
        self.image = self.klatki[self.aktualna_klatka]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        self.aktualna_klatka += 0.35

        if self.aktualna_klatka >= len(self.klatki):
            self.aktualna_klatka = 0

        self.image = self.klatki[int(self.aktualna_klatka)]


class Przeciwnik(py.sprite.Sprite):             # klasa odpowiedzialna za działanie przeciwnika
    def __init__(self, x, y, width, height, granica):
        super().__init__()
        self.klatki = [py.image.load('elementy/M1.png'), py.image.load('elementy/M2.png'),
                       py.image.load('elementy/M3.png'), py.image.load('elementy/M4.png'),
                       py.image.load('elementy/M5.png'), py.image.load('elementy/M6.png'),
                       py.image.load('elementy/M7.png'), py.image.load('elementy/M8.png'),
                       py.image.load('elementy/M9.png'), py.image.load('elementy/M10.png')]
        self.aktualna_klatka = 0
        self.image = self.klatki[self.aktualna_klatka]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.granica = granica
        self.droga = [self.x, self.granica]
        self.walk = 0
        self.predkosc = 2

    def draw(self):
        self.move()
        self.aktualna_klatka += 0.7
        if self.aktualna_klatka >= len(self.klatki):
            self.aktualna_klatka = 0
        if self.walk + 1 >= 60:
            self.walk = 0

        if self.predkosc > 0:
            screen.blit(self.klatki[int(self.aktualna_klatka // 3)], (self.x, self.y))
            self.walk += 1
        else:
            screen.blit(self.klatki[int(self.aktualna_klatka // 3)], (self.x, self.y))
            self.walk += 1

    def move(self):
        if self.predkosc > 0:
            if self.x + self.predkosc < self.droga[1]:
                self.x += self.predkosc
            else:
                self.predkosc = self.predkosc * -1
                self.walk = 0
        else:
            if self.x-self.predkosc > self.droga[0]:
                self.x += self.predkosc
            else:
                self.predkosc = self.predkosc * -1
                self.walk = 0


class Gracz(object):
    def __init__(self, x, y, width, height):
        self.wlewo = [py.image.load('elementy/GL1.png'), py.image.load('elementy/GL2.png'),
                      py.image.load('elementy/GL3.png'), py.image.load('elementy/GL4.png'),
                      py.image.load('elementy/GL5.png'), py.image.load('elementy/GL6.png'),
                      py.image.load('elementy/GL7.png'), py.image.load('elementy/GL8.png'),
                      py.image.load('elementy/GL9.png')]

        self.wprawo = [py.image.load("elementy/GR1.png"), py.image.load('elementy/GR2.png'),
                       py.image.load('elementy/GR3.png'), py.image.load('elementy/GR4.png'),
                       py.image.load('elementy/GR5.png'), py.image.load('elementy/GR6.png'),
                       py.image.load('elementy/GR7.png'), py.image.load('elementy/GR8.png'),
                       py.image.load('elementy/GR9.png')]

        self.stoi = py.image.load('elementy/gracz.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = 9
        self.jump = False
        self.jumpcount = 8
        self.left = False
        self.right = False
        self.walk = 0

    def draw(self):
        if self.walk + 1 >= 27:
            self.walk = 0
        if self.left:
            screen.blit(self.wlewo[self.walk//3], (self.x, self.y))
            self.walk += 1
        elif self.right:
            screen.blit(self.wprawo[self.walk//3], (self.x, self.y))
            self.walk += 1
        else:
            screen.blit(self.stoi, (self.x, self.y))


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
                level_1()
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


def level_1():
    global click
    click = False

    running = True

    # dane pozycji i rozmiaru gracza
    y_chopek = 480
    x_chopek = 640
    chopek_width = 25
    chopek_height = 64

    # dane pozycji i rozmiaru przeciwnika
    y_wrog_1 = 480
    x_wrog_1 = 220
    wrog_width = 46
    wrog_height = 63

    # dane pozycji i rozmiaru portalu
    x_nagroda = 20
    y_nagroda = 450
    nagroda_width = 70
    nagroda_height = 100

    # początki zmian na klasy i animacje wrzucone zostaną do jednej grupy po czym wczytane na ekran
    animacje = py.sprite.Group()
    nagroda = Portal(x_nagroda, y_nagroda, nagroda_width, nagroda_height)
    wrog_1 = Przeciwnik(x_wrog_1, y_wrog_1, wrog_width, wrog_height, 600)
    animacje.add(nagroda)
    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)

    while running:

        mx, my = py.mouse.get_pos()

        tlo = py.image.load('tła/tło 1.png')

        button_5 = py.Rect(700, 5, 100, 25)

        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        animacje.draw(screen)
        animacje.update()
        wrog_1.draw()
        chopek.draw()

        py.draw.rect(screen, (168, 177, 217), button_5)
        draw_text('Menu Główne', font_S, (48, 74, 253), screen, 710, 10)

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        keys = py.key.get_pressed()
        if (keys[py.K_a] or keys[py.K_LEFT]) and chopek.x > chopek.move:
            chopek.x -= chopek.move
            chopek.left = True
            chopek.right = False
        elif (keys[py.K_d] or keys[py.K_RIGHT]) and chopek.x < screen.get_width() - chopek.width:
            chopek.x += chopek.move
            chopek.left = False
            chopek.right = True
        else:
            chopek.right = False
            chopek.left = False
            chopek.walk = 0

        # skok gracza

        if not chopek.jump:
            if keys[py.K_SPACE] or keys[py.K_UP] or keys[py.K_w]:
                chopek.jump = True
                chopek.right = False
                chopek.left = False
        else:
            if chopek.jumpcount >= -8:
                neg = 1
                if chopek.jumpcount < 0:
                    neg = -1
                chopek.y -= (chopek.jumpcount ** 2) * 0.5 * neg
                chopek.jumpcount -= 1
            else:
                chopek.jump = False
                chopek.jumpcount = 8

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if chopek.x < wrog_1.x + wrog_1.width and chopek.x + chopek.width > wrog_1.x and chopek.y >= wrog_1.y:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False

        if chopek.x < nagroda.x + nagroda.width and chopek.x + chopek.width > nagroda.x and chopek.y >= nagroda.y:
            screen.fill((0, 0, 0))
            draw_text(' Gratuluję, kolejny poziom na ciebie czeka! :) ', font, (255, 0, 0), screen, 100, 300)
            py.display.flip()
            time.sleep(3)

            level_2()

            # obsługa przycisków w tym momencie przycisku Main menu

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


def level_2():
    global click
    click = False

    running = True

    # dane pozycji i rozmiaru gracza
    y_chopek = 480
    x_chopek = 640
    chopek_width = 25
    chopek_height = 64

    # dane pozycji i rozmiaru przeciwników
    y_wrog_1 = 480
    x_wrog_1 = 360
    wrog_width = 46
    wrog_height = 63

    y_wrog_2 = 480
    x_wrog_2 = 220

    # dane pozycji i rozmiaru portalu
    x_nagroda = 20
    y_nagroda = 450
    nagroda_width = 70
    nagroda_height = 100

    # początki zmian na klasy i animacje wrzucone zostaną do jednej grupy po czym wczytane na ekran
    animacje = py.sprite.Group()
    nagroda = Portal(x_nagroda, y_nagroda, nagroda_width, nagroda_height)
    wrog_1 = Przeciwnik(x_wrog_1, y_wrog_1, wrog_width, wrog_height, 600)
    wrog_2 = Przeciwnik(x_wrog_2, y_wrog_2, wrog_width, wrog_height, 500)
    animacje.add(nagroda)
    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)

   # x_block_1 = 475
   # y_block_1 = 400
   # block_width_1 = 50
   # block_height_1 = 20

   # x_block_2 = 275
   # y_block_2 = 400
   # block_width_2 = 50
   # block_height_2 = 20

    while running:

        mx, my = py.mouse.get_pos()

        tlo = py.image.load('tła/tło 2.png')

        button_5 = py.Rect(700, 5, 100, 25)
        Block_1 = py.Rect(275, 460, 50, 20)

        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        animacje.draw(screen)
        animacje.update()
        wrog_1.draw()
        wrog_2.draw()
        chopek.draw()

      #  Block_1 = py.Rect(x_block_1, y_block_1, block_width_1, block_height_1)
      #  Block_2 = py.Rect(x_block_2, y_block_2, block_width_2, block_height_2)

        py.draw.rect(screen, (168, 177, 217), button_5)
        py.draw.rect(screen, (19,33, 161), Block_1)
        draw_text('Menu Główne', font_S, (48, 74, 253), screen, 710, 10)

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        keys = py.key.get_pressed()
        if (keys[py.K_a] or keys[py.K_LEFT]) and chopek.x > chopek.move:
            chopek.x -= chopek.move
            chopek.left = True
            chopek.right = False
        elif (keys[py.K_d] or keys[py.K_RIGHT]) and chopek.x < screen.get_width() - chopek.width:
            chopek.x += chopek.move
            chopek.left = False
            chopek.right = True
        else:
            chopek.right = False
            chopek.left = False
            chopek.walk = 0

        # skok gracza

        if not chopek.jump:
            if keys[py.K_SPACE] or keys[py.K_UP] or keys[py.K_w]:
                chopek.jump = True
                chopek.right = False
                chopek.left = False
        else:
            if chopek.jumpcount >= -8:
                neg = 1
                if chopek.jumpcount < 0:
                    neg = -1
                chopek.y -= (chopek.jumpcount ** 2) * 0.5 * neg
                chopek.jumpcount -= 1
            else:
                chopek.jump = False
                chopek.jumpcount = 8

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if chopek.x < wrog_1.x + wrog_1.width and chopek.x + chopek.width > wrog_1.x and chopek.y >= wrog_1.y:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < wrog_2.x + wrog_2.width and chopek.x + chopek.width > wrog_2.x and chopek.y >= wrog_2.y:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x > 275 and chopek.x + chopek.width < 325 and chopek.y + chopek_height < 470:
            chopek.y = 386
        else:
            chopek.y = chopek.y


        if chopek.x < nagroda.x + nagroda.width and chopek.x + chopek.width > nagroda.x and chopek.y >= nagroda.y:
            screen.fill((0, 0, 0))
            draw_text('BRAWO!!! Gratuluje przejścia poziomu :D', font, (255, 0, 0), screen, 100, 300)
            py.display.flip()
            time.sleep(3)

            main_menu()

            # obsługa przycisków w tym momencie przycisku Main menu

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

        # obsługa przycisków w tym momencie przycisku Main menu

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
        tlo = py.image.load('tła/tło_twórcy.png')
        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        draw_text(' Miłosz Kapłanek ', font_B, (15, 69, 29), screen, 230, 200)
        draw_text(' Tomasz Paruzel', font_B, (15, 59, 29), screen, 230, 300)
        button_7 = py.Rect(18, 490, 150, 50)
        py.draw.rect(screen, (148, 176, 255), button_7)
        draw_text(' <-- Powrót ', font, (120, 20, 20), screen, 20, 500)

        # obsługa przycisków w tym momencie przycisku powrót do Main menu

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
