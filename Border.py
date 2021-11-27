from Sprite import Sprite
class Border():
    def __init__(self, w, h):
        self.border_sprites, self.border_matrix = self.new_border(w, h)
    #create 2 matrices, one with the sprites and another who says if a position is valid or not
    def new_border(self, w, h):
        border_sprites = []
        border_matrix = []
        for i in range(8):
            border_sprites.append([])
            border_matrix.append([])
            for j in range(6):
                borderSquare = Sprite(w/6, h/8, w/6*j, h/8*i)
                border_sprites[i].append(borderSquare)
                border_matrix[i].append(0)
        return border_sprites, border_matrix
    def modify_border(self, i, j, is_player_blue):
        self.border_matrix[i][j] = -1
        if(is_player_blue):
            self.border_sprites[i][j].blue()
        else:
            self.border_sprites[i][j].red()
    #reset the two matrices
    def reset(self):
        for i in range(8):
            for j in range(6):
                self.border_matrix[i][j] = 0
                self.border_sprites[i][j].reset()
                
    