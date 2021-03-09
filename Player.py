import pygame
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

pygame.init()


walkRight = pygame.image.load(f'{os.getcwd()}\\images\\Right.png')
walkLeft = pygame.transform.flip(walkRight, True, False) 
playerFireballRight = pygame.image.load(f'{os.getcwd()}\\images\\Fireball.png')
playerFireballLeft = pygame.transform.flip(playerFireballRight, True, False)


class Character(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.health = 100
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.currentDirection = "Right"
        self.hitbox = (self.x + 20, self.y, self.width - 10, self.height)

    def redraw(self, screen):
        if self.walkCount + 1 >= 1:
            self.walkCount = 0

        if self.left:
            self.currentDirection = "Left"
            screen.blit(walkLeft, (self.x, self.y))
            self.walkCount += 1

        elif self.right:
            self.currentDirection = "Right"
            screen.blit(walkRight, (self.x, self.y))
            self.walkCount += 1

        elif not self.left and not self.right:
            if self.currentDirection == "Left":
                screen.blit(walkLeft, (self.x, self.y))
            elif self.currentDirection == "Right":
                screen.blit(walkRight, (self.x, self.y))

        self.hitbox = (self.x + 20, self.y, self.width - 10, self.height)

    def move(self, keys, SCREENWIDTH):
        if keys[pygame.K_LEFT] and self.hitbox[0] > 0:  
            self.x -= self.vel
            self.left = True
            self.right = False

        elif keys[pygame.K_RIGHT] and self.hitbox[0] + self.hitbox[2] < SCREENWIDTH: 
            self.x += self.vel
            self.left = False
            self.right = True

        else:
            self.x += 0
            self.left = False
            self.right = False

        if not self.isJump:
            if keys[pygame.K_SPACE]:
                self.isJump = True
                self.left = False
                self.right = False
                self.walkCount = 0

        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.3 * neg
                self.jumpCount -= 2
            else:
                self.isJump = False
                self.jumpCount = 10

    def update(self, *args, **kargs):
        from __main__ import keys, SCREENWIDTH, screen
        self.move(keys, SCREENWIDTH)
        self.redraw(screen)


class playerAttacks(object):
    def __init__(self, x, y, width, height, direction, vel, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.damage = damage
        self.vel = vel * self.direction

    def redraw(self, screen):
        if self.direction == 1:
            screen.blit(playerFireballRight, (self.x, self.y))
            
        elif self.direction == -1:
            screen.blit(playerFireballLeft, (self.x, self.y))

    def edges(self, attacks, SCREENWIDTH):
        for attack in attacks:
            if 0 < attack.x < SCREENWIDTH:
                attack.x += attack.vel

            else:
                attacks.pop(attacks.index(attack))

    def update(self):
        from __main__ import attacks, SCREENWIDTH, screen
        self.edges(attacks, SCREENWIDTH)
        self.redraw(screen)
