#this file creates objects of the game
import pygame
import randomFn
from fileio import file_to_2dlist

worldx = 720
worldy = 720
world = pygame.display.set_mode([worldx, worldy])
images = []
images.append(pygame.image.load('images/green20.png').convert_alpha())
images.append(pygame.image.load('images/red20.png').convert_alpha())
images.append(pygame.image.load('images/yellow20.png').convert_alpha())
steps = 5
direction={1:[steps,0], 2:[-steps,0], 3:[0,steps], 4:[0,-steps]
    ,5:[steps,steps], 6:[-steps,steps], 7:[steps,-steps], 8:[-steps,-steps]}
maze = file_to_2dlist('data/mazeWalls.txt')

def changeCoord(x):
    if x != 0 :
        x = int(x/20)
        if x >= 36:
            x = 35
    else:
        x = 0
    return x

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
        def moveInDirection():
            d = randomFn.randInt(1,8)
            self.control(direction[d][0], direction[d][1])
            return True

        if (randomFn.randChance(5)): #chance to change directions
            moveInDirection()
            return
        
        if maze[changeCoord(self.rect.y + self.movey)][changeCoord(self.rect.x + self.movex)] == 1:
            #print("collide")
            moveInDirection()
            return
        else:
            self.rect.x += self.movex
            self.rect.y += self.movey

    def changeImage(self, x):
        self.image = images[x]

def createPlayers(totalPlayers):
    playerGroup = pygame.sprite.Group()
    playerList = []
    for x in range(totalPlayers):
        player = Player()  # spawn player
        player.rect.x = randomFn.randInt(0,worldx)  # go to x
        player.rect.y = randomFn.randInt(0,worldy)  # go to y
        while maze[changeCoord(player.rect.y)][changeCoord(player.rect.x)] == 1:
            player.rect.x = randomFn.randInt(0,worldx)  # go to x
            player.rect.y = randomFn.randInt(0,worldy)  # go to y
        #player.movex, player.movey = direction[randomFn.randInt(1,8)]
        playerGroup.add(player)
        playerList.append(player)
    return playerList, playerGroup
    