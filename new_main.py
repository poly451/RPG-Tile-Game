from settings import *
import pygame
import os, sys
from sprites import Player, Wall
from tilemap import Map, Camera

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        # __file__ is the location the game is running from.
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        self.player_img = pygame.image.load(os.path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.map = Map(os.path.join(game_folder, 'map3.txt'))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        #self.player = Player(self, 2, 2)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)
    # ----------------------------------------------------------------------

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    #self.player.move(dx=-1)
                    if self.player.direction == LEFT:
                        self.player.image = pygame.transform.rotate(self.player.image, 0)
                    else:
                        if self.player.direction == UP:
                            self.player.image = pygame.transform.rotate(self.player.image, 90)
                        if self.player.direction == RIGHT:
                            self.player.image = pygame.transform.rotate(self.player.image, 180)
                        if self.player.direction == DOWN:
                            self.player.image = pygame.transform.rotate(self.player.image, -90)
                        self.player.direction = LEFT
                    #self.player.x += -1
                    self.player.move(dx = -1)
                if event.key == pygame.K_RIGHT:
                    #self.player.move(dx=1)
                    if self.player.direction == RIGHT:
                        self.player.image = pygame.transform.rotate(self.player.image, 0)
                    else:
                        if self.player.direction == UP:
                            self.player.image = pygame.transform.rotate(self.player.image, -90)
                        if self.player.direction == LEFT:
                            self.player.image = pygame.transform.rotate(self.player.image, -180)
                        if self.player.direction == DOWN:
                            self.player.image = pygame.transform.rotate(self.player.image, 90)
                        self.player.direction = RIGHT
                    #self.player.x += 1
                    self.player.move(dx=1)
                if event.key == pygame.K_UP:
                    #self.player.move(dy=-1)
                    if self.player.direction == UP:
                        self.player.image = pygame.transform.rotate(self.player.image, 0)
                    else:
                        if self.player.direction == DOWN:
                            self.player.image = pygame.transform.rotate(self.player.image, 180)
                        if self.player.direction == RIGHT:
                            self.player.image = pygame.transform.rotate(self.player.image, 90)
                        if self.player.direction == LEFT:
                            self.player.image = pygame.transform.rotate(self.player.image, -90)
                        self.player.direction = UP
                    #self.player.y += -1
                    self.player.move(dy = -1)
                if event.key == pygame.K_DOWN:
                    #self.player.move(dy=1)
                    if self.player.direction == DOWN:
                        self.player.image = pygame.transform.rotate(self.player.image, 0)
                    else:
                        if self.player.direction == UP:
                            self.player.image = pygame.transform.rotate(self.player.image, -180)
                        if self.player.direction == RIGHT:
                            self.player.image = pygame.transform.rotate(self.player.image, -90)
                        if self.player.direction == LEFT:
                            self.player.image = pygame.transform.rotate(self.player.image, 90)
                        self.player.direction = DOWN
                    #self.player.y += 1
                    self.player.move(dy=1)

    def all_sprites(self):
        pass

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        pass

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_player(self):
        pass

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        #self.draw_player()
        # self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    # ----------------------------------------------------------------------

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

# create the game object
g = Game()
while True:
    g.new()
    g.run()
