from typing import Tuple

import aStar
import pygame
import sys
import randomFn
import numpy
from objectSim import Player, world, createPlayers

# global variables
worldx = 720
worldy = 720
fps = 12
maze = numpy.zeros((int(worldx/20), int(worldy/20)), dtype=int)

'''
Setup
'''
backdrop = pygame.image.load('images/stage.png').convert_alpha()
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True
totalPlayers = 80
playerList, playerGroup = createPlayers(totalPlayers)
covidSet = set()
covidSet.add(5)
covidRange = 70
covidChance = 3

def changeCoord(x):
    if x != 0 :
        return int(x/20)
    return 0

def covid(covidSet):
    newcovidSet = set()
    for x in covidSet:
        player = playerList[x]
        player.changeImage(1)

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
                    print("Person", x, "infected", "Person", idx)
                else:
                    y.changeImage(2)
    return set.union(covidSet, newcovidSet)

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