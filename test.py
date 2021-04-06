from typing import Tuple

import pygame
import sys
import os
import randomFn

'''
Variables
'''

worldx = 960
worldy = 720
fps = 12
world = pygame.display.set_mode([worldx, worldy])
Pixsize = 5 #size of object

'''
Objects
'''
class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join('images', 'hero1.png'))
        self.images.append(img)
        self.image = self.images[0]
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
        if (self.rect.y + self.movey) < 0:
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
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

totalPlayers = 100
player_list = pygame.sprite.Group()
def createPlayers():
    player = Player()  # spawn player
    player.rect.x = randomFn.randInt(0,worldx)  # go to x
    player.rect.y = randomFn.randInt(0,worldy)  # go to y
    x,y = direction[randomFn.randInt(1,8)]
    player.movex = x
    player.movey = y
    player_list.add(player)

steps = 1
direction={1:[steps,0], 2:[-steps,0], 3:[0,steps], 4:[0,-steps]
    ,5:[steps,steps], 6:[-steps,steps], 7:[steps,-steps], 8:[-steps,-steps]}
for x in range(totalPlayers):
    createPlayers()

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
    for player in player_list:
        player.update()

    world.blit(backdrop, backdropbox)
    
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)