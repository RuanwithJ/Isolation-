from Border import Border


class Player():
    def __init__(self):
        self.position = (-1, -1)

    def moves(self, border):
        self.player_moves = self._moves(self.position, border)
    
    def get_moves(self):
        return self.player_moves
    
    #Return all possible moves the player can do
    def _moves(self, position, borderAux):
        y, x = position
        p = []
        if(x==-1 and y==-1):
            for i in range(8):
                for j in range(6):
                    p.append((i, j))
            return p
        for j in range(x+1, 6):
                if(borderAux[y][j] == 0):
                    p.append((y, j))
                else:
                    break
        for j in range(x-1, -1, -1):
                if(borderAux[y][j] == 0):
                    p.append((y, j))
                else:
                    break
        for i in range(y+1, 8):
                if(borderAux[i][x] == 0):
                    p.append((i, x))
                else:
                    break
        for i in range(y-1, -1, -1):
                if(borderAux[i][x] == 0):
                    p.append((i, x))
                else:
                    break
        k = 1
        while True:
                if(y+k == 8 or x+k == 6):
                    break
                if(borderAux[y+k][x+k] == 0):
                        p.append((y+k, x+k))
                else:
                    break
                k+=1
        k = 1
        while True:
                if(y+k == 8 or x-k == -1):
                    break
                if(borderAux[y+k][x-k] == 0):
                        p.append((y+k, x-k))
                else:
                    break
                k+=1
        k = 1 
        while True:
            if(y-k == -1 or x+k == 6):
                break
            if(borderAux[y-k][x+k] == 0):
                    p.append((y-k, x+k))
            else:
                break
            k+=1
        k = 1

        k = 1
        while True:
            if(y-k == -1 or x-k == -1):
                break
            if(borderAux[y-k][x-k] == 0):
                    p.append((y-k, x-k))
            else:
                break
            k+=1
            
        return p
