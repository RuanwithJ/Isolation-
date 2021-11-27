from sys import maxsize as infinity
from random import randint

import numpy as np

def Max(moves1, moves2):
    if len(moves1) == 0:
        return -(infinity)
    return (len(moves1) - 2*len(moves2))
    
def Min(moves1, moves2):
    if len(moves2) == 0:
        return -(infinity)
    return (len(moves1) - 2*len(moves2))
def possible_movies(red, blue, border):
    border[red.position[0]][red.position[1]] = -1
    border[blue.position[0]][blue.position[1]] = -1
    red.moves(border)
    blue.moves(border)

def min_max(red, blue, depth, border):
    max_depth = depth
    if(red.position == (-1, -1)):
        return ((randint(0, 7), randint(0, 5)))
    def _min_max(red, blue, depth, border, player_max=True, alpha=-infinity, beta=infinity):  
        possible_movies(red, blue, border)
        if depth == 0 or blue.get_moves() == [] or red.get_moves() == []:
            if(player_max):
                return Max(red.get_moves(), blue.get_moves()), red.position
            else:
                return Min(red.get_moves(), blue.get_moves()), red.position
        if player_max:
            max_eval = -infinity
            best_move = red.position
            for m in red.get_moves():
                move_ant = red.position
                red.position = m
                eval, move = _min_max(red, blue, depth-1, np.copy(border),False, alpha, beta)
                red.position = move_ant
                if(depth!=max_depth):
                    move = red.position
                if(eval>max_eval):
                    max_eval = eval
                    best_move = move
                if alpha >= beta:
                    break
                alpha = max(alpha, eval)
            return max_eval, best_move
        else: 
            min_eval = infinity
            best_move = red.position
            for m in blue.get_moves():
                move_ant = blue.position
                blue.position = m
                eval, move = _min_max(red, blue, depth-1, np.copy(border), True, alpha, beta)
                blue.position = move_ant
                if(depth!=max_depth):
                    move = red.position
                if(eval<min_eval):
                   min_eval = eval
                   best_move = move
                if alpha >= beta:
                    break
                beta = min(beta, eval)
            return min_eval, best_move
    return _min_max(red, blue, depth, np.copy(border))[1]
    

