from Player import Player
from Border import Border
from Min_Max import min_max
import pygame
class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.score = [0, 0]
        self.graph_init()
        self.border = Border(self.width, self.high)
        self.red = Player()
        self.blue = Player()
    #start the screen
    def graph_init(self):
        pygame.init()
        self.width,self.high = (450, 600)
        self.screen = pygame.display.set_mode((700, 700))
        self.border_surface = pygame.Surface((self.width, self.high))
        self.border_surface.fill((230, 220, 210))

    def start(self):
        blue_turn = True
        while True:
            self.red.moves(self.border.border_matrix)
            self.blue.moves(self.border.border_matrix)
            if(self.red.player_moves == [] or self.blue.player_moves == []):
                if(self.red.get_moves() == []):
                    self.score[0] +=1
                elif(self.blue.get_moves() == []):
                    self.score[1] +=1
                self.border.reset()
                self.blue.position = (-1, -1)
                self.red.position = (-1, -1)
                self.red.moves(self.border.border_matrix)
                self.blue.moves(self.border.border_matrix)
                print(self.score)
            if(not blue_turn):
                r = self.red.position
                b = self.blue.position
                play = min_max(self.red, self.blue, 5, self.border.border_matrix)
                self.blue.position = b
                self.red.position =  play
                self.border.modify_border(play[0], play[1], False)
                if(r[0]!=-1):                   
                   self.border.border_sprites[r[0]][r[1]].eliminated()
                blue_turn = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(8):
                        for j in range(6):
                            sprite = self.border.border_sprites[i][j]
                            if(sprite.is_clicked()):
                                    if(blue_turn):      
                                        if (i, j) in self.blue.get_moves():
                                            sprite.blue()
                                            y, x = self.blue.position
                                            if(x!=-1):
                                                self.border.border_sprites[y][x].eliminated()
                                            self.blue.position = (i, j)
                                            blue_turn = False
                                            self.border.border_matrix[i][j] = -1
                            

            self.screen.blit(self.border_surface, (100,50))
            for i in range(8):
                for j in range(6):
                    self.border_surface.blit(self.border.border_sprites[i][j].surface(),self.border.border_sprites[i][j].rect)
            pygame.display.update()
            self.clock.tick(60)