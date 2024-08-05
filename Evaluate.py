from constants import centrerow,centrecolumn,Backrow,piece,queen
from multiprocessing import Process,Pool

#class processWithReturnValue():
    
    #def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
      #  process.__init__(self, group, target, name, args, kwargs)

     #   self._return = None

    #def run(self):
        #if self._target is not None:
       #     self._return = self._target(*self._args,
        #                                        **self._kwargs)
    #def join(self, *args):
     #   process.join(self, *args)
      #  return self._return
def count_pieces(location,colour):
    total=0.0
    for i in range(12):
        if location[i]:
            if location[i][2]==1:
                total+=piece
            elif location[i][2]==2:
                total+=queen
            if location[i][0]==3 or location[i][0]==4:
                total+=centrerow
                if location[i][1]>=2 and location[i][1]<=5:
                    total+=centrecolumn
            if (colour == 1 and location[i][0]==0) or (colour==2 and location[i][0]==7):
                total+= Backrow
    
    return total


def check_safe(location,colour,state):
    opposite=(colour%2)+1
    total=0.0
    for i in range(12):
        if location[i]:
            take=False
            x0=location[i][1]
            y0=location[i][0]
            if x0>0 and y0>0 and state[y0-1][x0-1].occupied==0:
                x=x0+1
                y=y0+1
                d=0
                while y<=7 and x<=7 and state[y][x].occupied==0:
                    y+=1
                    x+=1
                    d+=1
                if x<=7 and y<=7:
                    if d==0 and state[y][x].occupied==opposite:
                        take=True
                    elif d>0 and state[y][x].occupied==opposite+2:
                        take=True
            if x0>0 and y0<7 and state[y0+1][x0-1].occupied==0:
                x=x0+1
                y=y0-1
                d=0
                while y>=0 and x<=7 and state[y][x].occupied==0 :
                    y-=1
                    x+=1
                    d+=1
                if x<=7 and y>=0:
                    if d==0 and state[y][x].occupied==opposite:
                        take=True
                    elif d>0 and state[y][x].occupied==opposite+2:
                        take=True
            if x0<7 and y0<7 and state[y0+1][x0+1].occupied==0:
                x=x0-1
                y=y0-1
                d=0
                while y>=0 and x>=0 and state[y][x].occupied==0 :
                    y-=1
                    x-=1
                    d+=1
                if x>=0 and y>=0:
                    if d==0 and state[y][x].occupied==opposite:
                        take=True
                    elif d>0 and state[y][x].occupied==opposite+2:
                        take=True
                    
            if x0<7 and y0>0 and state[y0-1][x0+1].occupied==0:
                x=x0-1
                y=y0+1
                d=0
                while y<=7 and x>=0 and state[y][x].occupied==0 :
                    y+=1
                    x-=1
                    d+=1
                if x>=0 and y<=7:
                    if d==0 and state[y][x].occupied==opposite:
                        take=True
                    elif d>0 and state[y][x].occupied==opposite+2:
                        take=True
            if take == True: total-=3.0
            else: total += 3.0                  
    return total



def staticeval(state,location1,location2):
    eval1=check_safe(location1,1,state)+count_pieces(location1,1)
    eval2 = check_safe(location2,2,state)+count_pieces(location2,2)
    return eval1-eval2



def staticeval2(state,location1,location2):
    input_data1 = [(location1,1,state)]
    #input_data2 = [(location1,1)]
    input_data3 = [(location2,2,state)]
    #input_data4 = [(location2,2)]

    with Pool(processes=4) as pool:
        eval1_check=pool.map(check_safe,input_data1)
        #eval1_count = pool.map(count_pieces, input_data2)
        eval2_check=pool.map(check_safe, input_data3)
        #eval2_count = pool.map(count_pieces, input_data4)
    
    #total = eval1_check[0] + eval1_count[0] - eval2_check[0] - eval2_count[0]
    total = eval1_check[0] + count_pieces(location1,1) - eval2_check[0] - count_pieces(location2,2)
    return total
