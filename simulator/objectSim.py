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