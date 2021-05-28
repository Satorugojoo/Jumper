import pygame as py
import sys
import time
from pygame.locals import *

mainClock = py.time.Clock()

py.init()
py.display.set_caption('Jumper')
screen = py.display.set_mode((800, 600), 0, 32)
font_A = py.font.SysFont('None', 40)
font_S = py.font.SysFont('None', 20)
font_B = py.font.SysFont('None', 60)
click = False


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


class Flame(object):
    def __init__(self, x, y, width, height, granica):
        super().__init__()
        self.klatki = [py.image.load('elementy/P1.png'), py.image.load('elementy/P2.png'),
                       py.image.load('elementy/P3.png'), py.image.load('elementy/P4.png'),
                       py.image.load('elementy/P5.png'), py.image.load('elementy/P6.png'),
                       py.image.load('elementy/P7.png'), py.image.load('elementy/P1.png'),
                       py.image.load('elementy/P1.png'), py.image.load('elementy/P1.png')]
        self.aktualna_klatka = 0
        self.image = self.klatki[self.aktualna_klatka]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.granica = granica
        self.droga = [self.y, self.granica]
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
            if self.y + self.predkosc < self.droga[1]:
                self.y += self.predkosc
            else:
                self.predkosc = self.predkosc * -1
                self.walk = 0
        else:
            if self.y - self.predkosc > self.droga[0]:
                self.y += self.predkosc
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
        self.jump = 0
        self.jumped = False
        self.left = False
        self.right = False
        self.walk = 0
        self.in_air = False

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

    def ruch(self):
        dy = 0

        keys = py.key.get_pressed()
        if (keys[py.K_a] or keys[py.K_LEFT]) and self.x > self.move:
            self.x -= self.move
            self.left = True
            self.right = False
        elif (keys[py.K_d] or keys[py.K_RIGHT]) and self.x < screen.get_width() - self.width:
            self.x += self.move
            self.left = False
            self.right = True
        else:
            self.right = False
            self.left = False
            self.walk = 0

        # skok gracza i grawitacja

        if (keys[py.K_SPACE] or keys[py.K_UP] or keys[py.K_w]) and self.jumped is False and self.in_air is False:
            self.jump = -25
            self.jumped = True
            self.in_air = True
        if (keys[py.K_SPACE] or keys[py.K_UP] or keys[py.K_w]) and self.jumped is not False:
            self.jumped = False

        self.jump += 2
        if self.jump > 10:
            self.jump = 20
        dy += self.jump

        self.y += dy

        if self.y + self.height > 565:
            self.y = 565 - self.height

        # kolizja z platformami

        if (self.x + self.width) > platforma.x and self.x < (platforma.x + platforma.width)\
                and platforma.y < (self.y + self.height) < (platforma.y + platforma.height):
            #print('jest')
            self.y = platforma.y - self.height
            self.jump = 0
            self.in_air = False

        if (self.x + self.width) > platforma2.x and self.x < (platforma2.x + platforma2.width) \
                and platforma2.y < (self.y + self.height) < (platforma2.y + platforma2.height):
            self.y = platforma2.y - self.height
            self.jump = 0
            self.in_air = False

        if (self.x + self.width) > platforma3.x and self.x < (platforma3.x + platforma3.width) \
                and platforma3.y < (self.y + self.height) < (platforma3.y + platforma3.height):
            self.y = platforma3.y - self.height
            self.jump = 0
            self.in_air = False

        if (self.x + self.width) > platforma4.x and self.x < (platforma4.x + platforma4.width) \
                and platforma4.y < (self.y + self.height) < (platforma4.y + platforma4.height):
            self.y = platforma4.y - self.height
            self.jump = 0
            self.in_air = False

        if (self.x + self.width) > platforma5.x and self.x < (platforma5.x + platforma5.width) \
                and platforma5.y < (self.y + self.height) < (platforma5.y + platforma5.height):
            self.y = platforma5.y - self.height
            self.jump = 0
            self.in_air = False

    def on_the_ground(self):
        if self.y >= 500:
            self.in_air = False


class Blok(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        bloczek = py.Rect(self.x, self.y, self.width, self.height)
        py.draw.rect(screen, (100, 31, 31), bloczek)


def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


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

        draw_text('GRAJ!', font_A, (100, 31, 31), screen, 355, 213)
        draw_text('Opcje', font_A, (100, 31, 31), screen, 355, 311)
        draw_text('Zakończ', font_A, (100, 31, 31), screen, 345, 412)
        draw_text('Twórcy', font_A, (120, 30, 30), screen, 675, 573)

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


def przycisk_main(x, y):
    global click
    mx, my = py.mouse.get_pos()
    button_5 = py.Rect(x, y, 100, 25)
    py.draw.rect(screen, (168, 177, 217), button_5)
    draw_text('Menu Główne', font_S, (48, 74, 253), screen, x + 10, y + 5)

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


# dane pozycji i rozmiaru platformy

x_block_1 = 476
y_block_1 = 430
block_width_1 = 50
block_height_1 = 20

x_block_2 = 280
y_block_2 = 380

x_block_3 = 40
y_block_3 = 300
block_width_3 = 80

global platforma, platforma2, platforma3, platforma4, platforma5, platforma6


def level_1():
    global click, platforma, platforma2, platforma3, platforma4, platforma5, platforma6
    click = False

    # dane pozycji i rozmiaru gracza
    y_chopek = 500
    x_chopek = 640
    chopek_width = 25
    chopek_height = 64

    # dane pozycji i rozmiaru przeciwnika
    y_wrog_1 = 500
    x_wrog_1 = 220
    wrog_width = 46
    wrog_height = 63

    # dane pozycji i rozmiaru portalu
    x_nagroda = 10
    y_nagroda = 190
    nagroda_width = 70
    nagroda_height = 100

    # początki zmian na klasy i animacje wrzucone zostaną do jednej grupy po czym wczytane na ekran

    animacje = py.sprite.Group()
    nagroda = Portal(x_nagroda, y_nagroda, nagroda_width, nagroda_height)
    wrog_1 = Przeciwnik(x_wrog_1, y_wrog_1, wrog_width, wrog_height, 600)
    animacje.add(nagroda)

    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)

    platforma = Blok(x_block_1, y_block_1, block_width_1, block_height_1)
    platforma2 = Blok(x_block_2, y_block_2, block_width_1, block_height_1)
    platforma3 = Blok(x_block_3, y_block_3, block_width_3, block_height_1)
    platforma4 = Blok(0, 0, 0, 0)
    platforma5 = Blok(0, 0, 0, 0)
    platforma6 = Blok(0, 0, 0, 0)

    running = True

    while running:

        tlo = py.image.load('tła/tło 1.png')

        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        animacje.draw(screen)
        animacje.update()
        przycisk_main(700, 5)
        wrog_1.draw()
        platforma.draw()
        platforma2.draw()
        platforma3.draw()
        chopek.draw()

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        chopek.ruch()
        chopek.on_the_ground()

        # platformy

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if chopek.x < wrog_1.x + wrog_1.width and chopek.x + chopek.width > wrog_1.x and chopek.y >= wrog_1.y:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False

        if chopek.x < nagroda.x + nagroda.width and chopek.x + chopek.width > nagroda.x \
                and nagroda.y + nagroda.height > chopek.y >= nagroda.y:
            screen.fill((0, 0, 0))
            draw_text(' Gratuluję, kolejny poziom na ciebie czeka! :) ', font_A, (255, 0, 0), screen, 100, 300)
            py.display.flip()
            time.sleep(3)

            level_2()

        py.display.flip()
        mainClock.tick(60)


def level_2():
    global click, platforma, platforma2, platforma3, platforma4
    click = False

    running = True

    # dane pozycji i rozmiaru gracza
    y_chopek = 500
    x_chopek = 640
    chopek_width = 25
    chopek_height = 64

    # dane pozycji i rozmiaru przeciwnika
    y_wrog_1 = 500
    x_wrog_1 = 220
    wrog_width = 46
    wrog_height = 63

    y_wrog_2 = 310
    x_wrog_2 = 260

    # dane pozycji i rozmiaru portalu
    x_nagroda = 20
    y_nagroda = 210
    nagroda_width = 70
    nagroda_height = 100

    # początki zmian na klasy i animacje wrzucone zostaną do jednej grupy po czym wczytane na ekran
    animacje = py.sprite.Group()
    nagroda = Portal(x_nagroda, y_nagroda, nagroda_width, nagroda_height)
    wrog_1 = Przeciwnik(x_wrog_1, y_wrog_1, wrog_width, wrog_height, 600)
    wrog_2 = Przeciwnik(x_wrog_2, y_wrog_2, wrog_width, wrog_height, 440)
    animacje.add(nagroda)
    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)

    # dane dla platform
    ax_block_1 = 476
    ay_block_1 = 450
    ablock_width_1 = 50
    ablock_height_1 = 20

    ax_block_2 = 280
    ay_block_2 = 380
    ablock_width_2 = 160

    ax_block_3 = 40
    ay_block_3 = 300
    ablock_width_3 = 80

    ax_block_4 = 130
    ay_block_4 = 480
    ablock_width_4 = 60

    # położnie platform
    platforma = Blok(ax_block_1, ay_block_1, ablock_width_1, ablock_height_1)
    platforma2 = Blok(ax_block_2, ay_block_2, ablock_width_2, ablock_height_1)
    platforma3 = Blok(ax_block_3, ay_block_3, ablock_width_3, ablock_height_1)
    platforma4 = Blok(ax_block_4, ay_block_4, ablock_width_4, ablock_height_1)

    while running:

        tlo = py.image.load('tła/tło 1.png')

        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        animacje.draw(screen)
        animacje.update()
        przycisk_main(700, 5)
        platforma.draw()
        platforma2.draw()
        platforma3.draw()
        platforma4.draw()
        wrog_1.draw()
        wrog_2.draw()
        chopek.draw()

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        chopek.ruch()
        chopek.on_the_ground()

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if chopek.x < wrog_1.x + wrog_1.width and chopek.x + chopek.width > wrog_1.x\
                and wrog_1.y <= chopek.y < wrog_1.y + wrog_1.height/2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < wrog_2.x + wrog_2.width and chopek.x + chopek.width > wrog_2.x\
                and wrog_2.y <= chopek.y < wrog_2.y + wrog_2.height/2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < nagroda.x + nagroda.width and chopek.x + chopek.width > nagroda.x \
                and nagroda.y + nagroda.height > chopek.y >= nagroda.y:
            screen.fill((0, 0, 0))
            draw_text('BRAWO!!! Gratuluje przejścia poziomu :D', font_A, (255, 0, 0), screen, 100, 300)
            py.display.flip()
            time.sleep(3)

            level_3()

        py.display.flip()
        mainClock.tick(60)


def level_3():

    global click, platforma, platforma2, platforma3, platforma4, platforma5
    click = False

    running = True

    # dane pozycji i rozmiaru gracza
    y_chopek = 480
    x_chopek = 640
    chopek_width = 25
    chopek_height = 64

    # dane pozycji i rozmiaru przeciwników
    y_wrog_1 = 500
    x_wrog_1 = 360
    wrog_width = 46
    wrog_height = 63

    y_wrog_2 = 500
    x_wrog_2 = 120

    # dane pozycji i rozmiaru portalu
    x_nagroda = 640
    y_nagroda = 100
    nagroda_width = 70
    nagroda_height = 100

    # początki zmian na klasy i animacje wrzucone zostaną do jednej grupy po czym wczytane na ekran
    animacje = py.sprite.Group()
    nagroda = Portal(x_nagroda, y_nagroda, nagroda_width, nagroda_height)
    wrog_1 = Przeciwnik(x_wrog_1, y_wrog_1, wrog_width, wrog_height, 600)
    wrog_2 = Przeciwnik(x_wrog_2, y_wrog_2, wrog_width, wrog_height, 500)
    animacje.add(nagroda)
    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)

    # Dane dla platform

    dx_block_1 = 480
    dy_block_1 = 420
    dblock_width_1 = 60
    dblock_height_1 = 20

    dx_block_2 = 325
    dy_block_2 = 330

    dx_block_3 = 60
    dy_block_3 = 220
    dblock_width_3 = 120

    dx_block_4 = 250
    dy_block_4 = 150

    dx_block_5 = 550
    dy_block_5 = 200
    dblock_width_2 = 110

    platforma = Blok(dx_block_1, dy_block_1, dblock_width_1, dblock_height_1)
    platforma2 = Blok(dx_block_2, dy_block_2, dblock_width_2, dblock_height_1)
    platforma3 = Blok(dx_block_3, dy_block_3, dblock_width_3, dblock_height_1)
    platforma4 = Blok(dx_block_4, dy_block_4, dblock_width_1, dblock_height_1)
    platforma5 = Blok(dx_block_5, dy_block_5, dblock_width_2, dblock_height_1)

    while running:

        tlo = py.image.load('tła/tło 2.png')

        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        animacje.draw(screen)
        animacje.update()
        przycisk_main(700, 5)
        platforma.draw()
        platforma2.draw()
        platforma3.draw()
        platforma4.draw()
        platforma5.draw()
        wrog_1.draw()
        wrog_2.draw()
        chopek.draw()

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        chopek.ruch()
        chopek.on_the_ground()

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if chopek.x < wrog_1.x + wrog_1.width and chopek.x + chopek.width > wrog_1.x\
                and wrog_1.y <= chopek.y < wrog_1.y + wrog_1.height / 2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < wrog_2.x + wrog_2.width and chopek.x + chopek.width > wrog_2.x\
                and wrog_2.y <= chopek.y < wrog_2.y + wrog_2.height / 2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < nagroda.x + nagroda.width and chopek.x + chopek.width > nagroda.x\
                and nagroda.y + nagroda.height > chopek.y >= nagroda.y:
            screen.fill((0, 0, 0))
            draw_text('WOOOW Przeszedłeś kolejny poziom.', font_A, (255, 0, 0), screen, 100, 300)
            py.display.flip()
            time.sleep(3)

            level_4()

        py.display.flip()
        mainClock.tick(60)


def level_4():
    global click
    click = False

    global platforma, platforma2, platforma3, platforma4, platforma5

    running = True

    # dane pozycji i rozmiaru gracza
    y_chopek = 500
    x_chopek = 640
    chopek_width = 25
    chopek_height = 64

    # dane pozycji i rozmiaru przeciwnika
    y_wrog_1 = 500
    x_wrog_1 = 220
    wrog_width = 46
    wrog_height = 63

    x_przeciwnik = 200
    y_przeciwnik = 20
    przeciwnik_width = 50
    przeciwnik_height = 64

    # dane pozycji i rozmiaru portalu
    x_nagroda = 5
    y_nagroda = 55
    nagroda_width = 70
    nagroda_height = 100

    # początki zmian na klasy i animacje wrzucone zostaną do jednej grupy po czym wczytane na ekran
    animacje = py.sprite.Group()
    nagroda = Portal(x_nagroda, y_nagroda, nagroda_width, nagroda_height)
    wrog_1 = Przeciwnik(x_wrog_1, y_wrog_1, wrog_width, wrog_height, 600)
    flame = Flame(x_przeciwnik, y_przeciwnik, przeciwnik_width, przeciwnik_height, 300)
    animacje.add(nagroda)
    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)

    # dane dla platform
    bx_block_1 = 476
    by_block_1 = 450
    bblock_width_1 = 50
    bblock_height_1 = 20

    bx_block_2 = 150
    by_block_2 = 350
    bblock_width_2 = 160

    bx_block_3 = 500
    by_block_3 = 260
    bblock_width_3 = 80

    bx_block_4 = 300
    by_block_4 = 130

    bx_block_5 = 30
    by_block_5 = 150

    # położnie platform
    platforma = Blok(bx_block_1, by_block_1, bblock_width_1, bblock_height_1)
    platforma2 = Blok(bx_block_2, by_block_2, bblock_width_2, bblock_height_1)
    platforma3 = Blok(bx_block_3, by_block_3, bblock_width_3, bblock_height_1)
    platforma4 = Blok(bx_block_4, by_block_4, block_width_3, bblock_height_1)
    platforma5 = Blok(bx_block_5, by_block_5, bblock_width_3, bblock_height_1)

    while running:

        tlo = py.image.load('tła/tło 3.png')

        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        animacje.draw(screen)
        animacje.update()
        przycisk_main(700, 5)
        platforma.draw()
        platforma2.draw()
        platforma3.draw()
        platforma4.draw()
        platforma5.draw()
        wrog_1.draw()
        flame.draw()
        chopek.draw()

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        chopek.ruch()
        chopek.on_the_ground()

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if chopek.x < wrog_1.x + wrog_1.width and chopek.x + chopek.width > wrog_1.x\
                and wrog_1.y <= chopek.y < wrog_1.y + wrog_1.height / 2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < flame.x + flame.width and chopek.x + chopek.width > flame.x\
                and flame.y <= chopek.y < flame.y + flame.height / 2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < nagroda.x + nagroda.width and chopek.x + chopek.width > nagroda.x \
                and nagroda.y + nagroda.height > chopek.y >= nagroda.y:
            screen.fill((0, 0, 0))
            draw_text('BRAWO!!! Gratuluje przejścia kolejnego :D', font_A, (255, 0, 0), screen, 100, 300)
            py.display.flip()
            time.sleep(3)

            level_5()

        py.display.flip()
        mainClock.tick(60)


def level_5():
    global click
    click = False

    global platforma, platforma2, platforma3

    running = True

    # dane pozycji i rozmiaru gracza
    y_chopek = 500
    x_chopek = 640
    chopek_width = 25
    chopek_height = 64

    # dane pozycji i rozmiaru przeciwnika
    y_wrog_1 = 500
    x_wrog_1 = 220
    wrog_width = 46
    wrog_height = 63

    y_wrog_2 = 310
    x_wrog_2 = 260

    # dane pozycji i rozmiaru portalu
    x_nagroda = 20
    y_nagroda = 210
    nagroda_width = 70
    nagroda_height = 100

    # początki zmian na klasy i animacje wrzucone zostaną do jednej grupy po czym wczytane na ekran
    animacje = py.sprite.Group()
    nagroda = Portal(x_nagroda, y_nagroda, nagroda_width, nagroda_height)
    wrog_1 = Przeciwnik(x_wrog_1, y_wrog_1, wrog_width, wrog_height, 600)
    wrog_2 = Przeciwnik(x_wrog_2, y_wrog_2, wrog_width, wrog_height, 440)
    animacje.add(nagroda)
    chopek = Gracz(x_chopek, y_chopek, chopek_width, chopek_height)

    # dane dla platform
    cx_block_1 = 476
    cy_block_1 = 500
    cblock_width_1 = 50
    cblock_height_1 = 20

    cx_block_2 = 280
    cy_block_2 = 380
    cblock_width_2 = 160

    cx_block_3 = 40
    cy_block_3 = 300
    cblock_width_3 = 80

    # położnie platform
    platforma = Blok(cx_block_1, cy_block_1, cblock_width_1, cblock_height_1)
    platforma2 = Blok(cx_block_2, cy_block_2, cblock_width_2, cblock_height_1)
    platforma3 = Blok(cx_block_3, cy_block_3, cblock_width_3, cblock_height_1)

    while running:

        tlo = py.image.load('tła/tło 2.png')

        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        animacje.draw(screen)
        animacje.update()
        przycisk_main(700, 5)
        platforma.draw()
        platforma2.draw()
        platforma3.draw()
        wrog_1.draw()
        wrog_2.draw()
        chopek.draw()

        py.display.update()
        mainClock.tick(60)

        # ruch gracza

        chopek.ruch()
        chopek.on_the_ground()

        # informacje wyskakujące w zależności czy gracz wygrał czy przegrał

        if chopek.x < wrog_1.x + wrog_1.width and chopek.x + chopek.width > wrog_1.x\
                and wrog_1.y <= chopek.y < wrog_1.y + wrog_1.height / 2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < wrog_2.x + wrog_2.width and chopek.x + chopek.width > wrog_2.x\
                and wrog_2.y <= chopek.y < wrog_2.y + wrog_2.height / 2:
            screen.fill((0, 0, 0))
            draw_text(' PRZEGRAŁEŚ :(', font_B, (255, 0, 0), screen, 250, 300)
            py.display.flip()
            time.sleep(3)
            running = False
            main_menu()

        if chopek.x < nagroda.x + nagroda.width and chopek.x + chopek.width > nagroda.x \
                and nagroda.y + nagroda.height > chopek.y >= nagroda.y:
            screen.fill((0, 0, 0))
            draw_text('SUPER!! Gratulacje ukończenia gry!! :D', font_A, (255, 0, 0), screen, 100, 300)
            py.display.flip()
            time.sleep(3)

            main_menu()

        py.display.flip()
        mainClock.tick(60)


def options():
    running = True

    global click
    click = False

    while running:

        screen.fill((0, 0, 0))
        draw_text('Cel gry oraz sterowanie', font_A, (255, 255, 255), screen, 20, 20)

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

        # przycisk Main Menu

        przycisk_main(700, 5)

        py.display.update()
        mainClock.tick(60)


def tworcy():
    running = True

    global click
    click = False

    while running:
        tlo = py.image.load('tła/tło_twórcy.png')
        screen.fill((0, 0, 0))
        screen.blit(tlo, (0, 0))
        draw_text(' Miłosz Kapłanek ', font_B, (15, 69, 29), screen, 230, 200)
        draw_text(' Tomasz Paruzel', font_B, (15, 59, 29), screen, 230, 300)

        # przycisk Main Menu

        przycisk_main(700, 5)

        py.display.update()
        mainClock.tick(60)


main_menu()
