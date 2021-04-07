#this file creates objects of the game
import pygame
import randomFn

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
        def moveInDirection(d):
            self.control(direction[d][0], direction[d][1])
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

    def changeImage(self, x):
        self.image = images[x]

def createPlayers(totalPlayers):
    playerGroup = pygame.sprite.Group()
    playerList = []
    for x in range(totalPlayers):
        player = Player()  # spawn player
        player.rect.x = randomFn.randInt(0,worldx)  # go to x
        player.rect.y = randomFn.randInt(0,worldy)  # go to y
        player.movex, player.movey = direction[randomFn.randInt(1,8)]
        playerGroup.add(player)
        playerList.append(player)
    return playerList, playerGroup