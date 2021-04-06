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
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

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
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        if (self.rect.x + self.movex) < 0:
            self.rect.x = 0
            return
        elif  (self.rect.x + self.movex) > worldx:
            self.rect.x = worldx-20
            return
        if (self.rect.y + self.movey) < 0:
            self.rect.y = 0
            return
        elif  (self.rect.y + self.movey) > worldy:
            self.rect.y = worldy-20
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

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 1

def moveInDirection(d):
    direction={1:[steps,0], 2:[-steps,0], 3:[0,steps], 4:[0,-steps]}
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
    prevx,prevy = player.rect.x, player.rect.y
    while(prevx == player.rect.x and prevy == player.rect.y):
        moveInDirection(randomFn.randInt(1,4))
        player.update()


    world.blit(backdrop, backdropbox)
    
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)