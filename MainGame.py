import pygame
from Player import Player
from Orb import Orb
import random

START_W = 50    #Starting width
START_H = 50
FPS = 60
NUM_ORBS = 10
class MainGame:
    def __init__(self):
        self.winDims = (1000,700)
        self.window = pygame.display.set_mode(self.winDims)
        self.winColor = (75,75,75)
        self.quit = False
        self.clock = pygame.time.Clock()

        self.player = Player(0,0,START_W,START_H)
        self.orbs = []

    def init(self):
        textures = ["green_orb.png","purple_orb.png","blue_orb.png","red_orb.png","yellow_orb.png","orange_orb.png"]

        for i in range(NUM_ORBS):
            randX = random.randint(0,self.winDims[0])
            randY = random.randint(0,self.winDims[1])
            randR = random.randint(10, START_W)

            randTexture = random.choice(textures)
            newOrb = Orb(randX,randY,randR, randTexture)
            self.orbs.append(newOrb)

        self.play()
    def play(self):
        while self.quit == False:
            self.update()
            self.render()

    def update(self):
        self.clock.tick(FPS)  #framerate

        #window events processed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
        #player update
        self.player.update()
        #orb update
        for orb in self.orbs:
            if orb.update(self.player):
                self.orbs.remove(orb)
    def render(self):
        self.window.fill(self.winColor)
        self.player.render(self.window)

        for orb in self.orbs:
            orb.render(self.window)
        pygame.display.update()