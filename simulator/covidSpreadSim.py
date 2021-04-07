from typing import Tuple

import aStar
import pygame
import sys
import os
import randomFn
import numpy

# global variables
worldx = 720
worldy = 720
fps = 12
world = pygame.display.set_mode([worldx, worldy])
maze = numpy.zeros((int(worldx/20), int(worldy/20)), dtype=int)
images = []
images.append(pygame.image.load(os.path.join('images', 'green20.png')).convert_alpha())
images.append(pygame.image.load(os.path.join('images', 'red20.png')).convert_alpha())
images.append(pygame.image.load(os.path.join('images', 'yellow20.png')).convert_alpha())


# object class
class Player(pygame.sprite.Sprite):
    """
    Spawn a person
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.image = images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        #bounding box
        self.movex = x
        self.movey = y

    def update(self):
        """
        Update sprite position
        """
        if (self.rect.x + self.movex) < 0:
            moveInDirection(randomFn.randInt(1,8))
            return
        elif  (self.rect.x + self.movex) > worldx-20:
            moveInDirection(randomFn.randInt(1,8))
            return
        if (self.rect.y + self.movey) < 0  :
            moveInDirection(randomFn.randInt(1,8))
            return
        elif  (self.rect.y + self.movey) > worldy-20:
            moveInDirection(randomFn.randInt(1,8))
            return
        if (randomFn.randChance(5)):
            moveInDirection(randomFn.randInt(1,8))
            return
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

'''
Setup
'''
backdrop = pygame.image.load(os.path.join('images', 'stage.png')).convert_alpha()
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

totalPlayers = 80
playerList = []
playerGroup = pygame.sprite.Group()

def createPlayers():
    player = Player()  # spawn player
    player.rect.x = randomFn.randInt(0,worldx)  # go to x
    player.rect.y = randomFn.randInt(0,worldy)  # go to y
    player.movex, player.movey = direction[randomFn.randInt(1,8)]
    playerGroup.add(player)
    playerList.append(player)

steps = 5
covidSet = set()
covidSet.add(5)
covidRange = 70
covidChance = 3

direction={1:[steps,0], 2:[-steps,0], 3:[0,steps], 4:[0,-steps]
    ,5:[steps,steps], 6:[-steps,steps], 7:[steps,-steps], 8:[-steps,-steps]}

for x in range(totalPlayers):
    createPlayers()

def changeCoord(x):
    if x != 0 :
        return int(x/20)
    return 0

def covid(covidSet):
    
    newcovidSet = set()
    for x in covidSet:
        player = playerList[x]
        player.image = images[1]

        #gotta check if anyone is close to this guy
        for idx, y in enumerate(playerList):
            if idx == x or idx in covidSet or idx in newcovidSet:
                continue
            if abs(player.rect.x - y.rect.x) > covidRange or  abs(player.rect.y - y.rect.y) > covidRange:
                continue
            else:
                xx = changeCoord(player.rect.x)
                xy = changeCoord(player.rect.y)
                yx = changeCoord(y.rect.x)
                yy = changeCoord(y.rect.y)
                path = aStar.astar(maze, (xx, xy), (yx, yy))
                if path != None and len(path) <= int(covidRange/20) and randomFn.randChance(covidChance):
                    newcovidSet.add(idx)
                else:
                    y.image = images[2]
    return set.union(covidSet, newcovidSet)


def moveInDirection(d):
    player.control(direction[d][0], direction[d][1])
    
'''
Main Loop
'''
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    for player in playerGroup:
        player.update()

    covidSet = covid(covidSet)

    world.blit(backdrop, backdropbox)
    
    playerGroup.draw(world)
    pygame.display.flip()
    clock.tick(fps)


#thonks
#the maze is a 36*36 grid
#to show off a star we shoud have some walls and shit
#but that also means that my guy cant walk through walls and i need to make many bounding boxes
#to make bounding boxes easier i can translate the pixel coords to the grids to determine where they are?
#probably want to come up w a grid first in excel