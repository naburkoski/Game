from abc import ABC

def spikes(entity):
    entity.health -= 10

def bounce(entity):
    pass

def collide(entity):
    pass

class Platform():
    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = height

    def collision(self):
        pass

class Spikes(Platform):
    def __init__(self, x, y, width, height):
        super().__init__( x, y, width, height)

        self.damage = spikes

    def collision(self, entity):
        self.damage(entity)

class Bounce(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.bounce = bounce

    def collision(self):
        self.bounce(entity)

class Basic(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.collide = Basic

    def collision(entity):
        self.collide()
        
