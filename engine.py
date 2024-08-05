from enginegame import engine_find_possible,engine_move_piece
from Evaluate import staticeval
import copy
from board import test
import constants
from threading import Thread

def minimax(state,maxlocation,minlocation,depth,alpha,beta,turn,piece):
    if turn%2 == 1:#maximising
        maxEva= -100000000000#start at -infinity
        possible = engine_find_possible(state,turn,maxlocation,piece)#generate possibl moves
        if depth ==0 or possible[0]==[0,0,False]:
            if possible[0]==[0,0,False]:#if game is lost, position set to -infinity
                return -10000000000 *(constants.depth-depth)
            return staticeval(state,maxlocation,minlocation)#returns static evaluation if depth limit
        i=0
        while i < len(possible) and possible[i][0]!=0:
            state0=copy.deepcopy(state)
            maxlocation0 = copy.deepcopy(maxlocation)
            minlocation0 = copy.deepcopy(minlocation)
            turn0,maxlocation0,minlocation0,piece0 = engine_move_piece(possible[i][0],possible[i][1],state0,turn,possible[i][2],maxlocation0,minlocation0)
            eva_temp= minimax(state0,maxlocation0,minlocation0, depth-1, alpha, beta, turn0,piece0)
            #eva= [eva_temp,possible[i][0],possible[i][1]]
            
            if depth == constants.depth:
                if type(maxEva)==int:
                    maxEva=[maxEva,0,0]
                if maxEva[0]<eva_temp:
        
                    maxEva= [eva_temp,possible[i][0],possible[i][1]]
                alpha = max(alpha,maxEva[0])
            else:
                if maxEva<eva_temp:
                    maxEva= eva_temp 
                alpha= max(alpha, maxEva)
            if beta<=alpha:
                break
            i+=1
        return maxEva
    else:
        minEva= 100000000000
        possible = engine_find_possible(state,turn,minlocation,piece)
        if depth ==0 or possible[0]==[0,0,False]:
            if possible[0]==[0,0,False]:
                return 10000000000 *(constants.depth-depth)
            return staticeval(state,maxlocation,minlocation)
        i=0
        while i < len(possible) and possible[i][0]!=0:
            state0=copy.deepcopy(state)
            maxlocation0 = copy.deepcopy(maxlocation)
            minlocation0 = copy.deepcopy(minlocation)
            turn0,maxlocation0,minlocation0,piece0 = engine_move_piece(possible[i][0],possible[i][1],state0,turn,possible[i][2],maxlocation0,minlocation0)
            eva_temp= minimax(state0,maxlocation0,minlocation0, depth-1, alpha, beta, turn0,piece0)
            #eva = [eva_temp,possible[i][0],possible[i][1]]
            if depth == constants.depth:
                if type(minEva)==int:
                    minEva=[minEva,0,0]
                if minEva[0]>eva_temp:
                    minEva= [eva_temp,possible[i][0],possible[i][1]]
                beta = min(beta, minEva[0])
            else:
                if minEva >eva_temp:
                     minEva = eva_temp
                beta = min(beta, minEva)

            
            if beta<=alpha:
                break
            i+=1
            
        return minEva
    


class ThreadWithReturnValue(Thread):
    
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return