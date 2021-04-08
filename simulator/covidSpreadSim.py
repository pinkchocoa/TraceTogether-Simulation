## @file aStar.py
#
# @brief this file contains the a star algorithm to find shortest path
#
# @section libraries_main Libraries/Modules
# - sys standard library
#   - required to do sys.ext
# - pygame
#   - used to run the simulation
# - json
#   - json dump to a json file
# - aStar
#   - contains aStar algorithm for finding the shortest path
# - general
#   - using it to determine if covid spreads
# - objectSim
#   - objects required for the simulation

import pygame
import sys #sys.exit
import json
import aStar
from general import randChance
from objectSim import Player, world, createPlayers, maze, changeCoord, worldx, worldy

'''
setup
'''
# global variables
fps = 12
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
edges["edges"] = []

def covid(covidSet):
    """! This method runs through all covid patients to check who is near them
    @param covidSet covidSet contains the identifier of covid patients
    @return an updated covidSet
    """
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
                    if randChance(covidChance):
                        newcovidSet.add(idx)
                        print("Person", x, "infected", "Person", idx)
                        edges["edges"].append({"from": x, "to": idx})
                    else:
                        y.changeImage(2)
                # uncomment to see astar algo (that was too far apart)
                else:
                    if path == None:
                        print("none")
                #     else:
                #         print(len(path), path)
    return set.union(covidSet, newcovidSet)

'''
main Loop
'''
while main: #while game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #upon exiting game
            with open('docs/json/infected.json', 'w') as outfile:
                json.dump(edges, outfile)
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    for player in playerGroup: #update every person
        player.update()

    covidSet = covid(covidSet) #check through covid patients
    world.blit(backdrop, backdropbox) #draw world
    playerGroup.draw(world) #draw people
    pygame.display.flip()
    clock.tick(fps) #limit fps
