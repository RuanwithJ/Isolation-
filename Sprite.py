import pygame
class Sprite:
    def __init__(self, width, height, x, y):
        self.rect = pygame.Rect(x, y, width, height)
        self.s1 = pygame.Surface((width,height))
        self.s2 = pygame.Surface((width-10, height-10))
        self.s1.fill('black')
        self.s2.fill((100, 100, 100))
        self.s1.blit(self.s2, (5, 5))
        self.state = 0
    def surface(self):
        return self.s1
    def rect(self):
        return self.rect
    def is_clicked(self):
        x, y = pygame.mouse.get_pos()
        x -= 125
        y -= 50
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint((x, y))
    def reset(self):
        self.state = 0
        self.s2.fill((100, 100, 100))
        self.s1.blit(self.s2, (5, 5))
    #turn the sprite blue
    def blue(self):
        if self.state == 0:
            self.state = 1
            self.s2.fill('Blue')
            self.s1.blit(self.s2, (5, 5))
    #turn the sprite red
    def red(self):
        if self.state == 0:
            self.state = 2
            self.s2.fill('Red')
            self.s1.blit(self.s2, (5, 5))
    #turn the sprite light grey (means the block is now invalid)
    def eliminated(self):
        self.s2.fill((150, 150, 150))
        self.s1.blit(self.s2, (5, 5))