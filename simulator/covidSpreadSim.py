from typing import Tuple

import aStar
import pygame
import sys
import randomFn
import json

from objectSim import Player, world, createPlayers, maze, changeCoord

# global variables
worldx = 720
worldy = 720
fps = 12
#maze = numpy.zeros((int(worldx/20), int(worldy/20)), dtype=int)
#maze = file_to_2dlist('data/mazeWalls.txt')

'''
Setup
'''
backdrop = pygame.image.load('images/stage.png').convert()
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True
totalPlayers = 50
playerList, playerGroup = createPlayers(totalPlayers)
covidSet = set()
covidSet.add(0)
covidRange = 50
mazeRange = 3
covidChance = 3
edges = {}
edges["nodes"] = []

def covid(covidSet):
    newcovidSet = set()
    for x in covidSet:
        player = playerList[x]
        player.changeImage(1)

        #gotta check if anyone is close to this guy
        for idx, y in enumerate(playerList):
            if idx == x or idx in covidSet or idx in newcovidSet:
                continue
            if abs(player.rect.x - y.rect.x) > covidRange or abs(player.rect.y - y.rect.y) > covidRange:
                continue #to reduce amount of astar checks required
            else:
                xx = changeCoord(player.rect.x)
                xy = changeCoord(player.rect.y)
                yx = changeCoord(y.rect.x)
                yy = changeCoord(y.rect.y)
                path = aStar.astar(maze, (xy, xx), (yy, yx))
                if path != None and len(path) <= mazeRange:
                    if randomFn.randChance(covidChance):
                        newcovidSet.add(idx)
                        print("Person", x, "infected", "Person", idx)
                        edges["nodes"].append({"from": x, "to": idx})
                    else:
                        y.changeImage(2)
                # else:
                #     if path == None:
                #         print("none")
                #     else:
                #         print(len(path), path)
    return set.union(covidSet, newcovidSet)

'''
Main Loop
'''
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('website/json/infected.json', 'w') as outfile:
                json.dump(edges, outfile)
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