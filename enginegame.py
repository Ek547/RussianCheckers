from board import merge_list2,test#merge_list
from game import check_take_possible

def engine_find_possible(state,turn,location,piece):#find each child node
    if turn%2 == 1:
       possible=white_move(state,location,piece)
    elif turn%2 == 0:
        possible = black_move(state,location,piece)
    return possible
######################################################################################
def engine_move_piece(square1,square2,state,turn,take,whitelocation,blacklocation):#go to next child node
        y1,x1=find_square_bynum(state,square1)
        y2,x2 = find_square_bynum(state,square2)
        temp1 = state[y1][x1]
        temp2 = state[y2][x2]
        if turn%2 == 1  :#comeback and reconsider neccisity
            colour = 1
        elif turn % 2 == 0 :
            colour = 2
        if take == True:
                if colour == 2:
                    loc=whitelocation
                    sub,whitelocation=take_piece(x1,y1,x2,y2,colour,state,loc)
                    if sub==1:
                        piece = chainpiece(x1,y1,blacklocation)
                    else:
                        piece = -1
                elif colour == 1:
                    loc=blacklocation
                    sub,blacklocation=take_piece(x1,y1,x2,y2,colour,state,loc)
                    if sub==1:
                        piece = chainpiece(x1,y1,whitelocation)
                    else:
                        piece = -1
                turn-=sub
                #take piece plus take again
        turn+=1
        if take==False:
            piece=-1
        if temp1.occupied == 1 and y2 == 7 :
                temp2.occupied = 3
                whitelocation= promote_location(x1,y1,whitelocation)
                temp1.occupied=0
        elif temp1.occupied == 2 and y2 == 0:
                temp2.occupied = 4
                blacklocation= promote_location(x1,y1,blacklocation)
                temp1.occupied=0
        if temp1.occupied == 4:
                temp2.occupied = 4
        elif temp1.occupied == 3:
                temp2.occupied = 3
        elif temp1.occupied == colour:
                temp2.occupied = colour
        temp1.occupied = 0
        if colour == 1:
                whitelocation = update_location(x1,y1,x2,y2,whitelocation)
        else:
                blacklocation = update_location(x1,y1,x2,y2,blacklocation)

            #draw_pieces(state,WIN)
            ##if move[1] == True:
              #  turn=turn-take_piece(x1,y1,x2,y2,colour,WIN,state)#take piece plus take again
            #turn+=1
        return turn,whitelocation,blacklocation,piece



def merge_list(normal,queen,n):
    j=0
    q=0
    while q<len(queen) and queen[q][0]!=0:
         q+=1
    while n<len(normal) and j <= q:
         normal[n]=queen[j]
         j+=1
         n+=1
    return normal,n-1

def queen_movement(x0,y0,state):
    y=y0
    x=x0
    queen_list=[[0,0,False]]*20
    e=0
    end=[[0,0]]*4
    q=0
    while x != 7 and y != 7 and state[y+1][x+1].occupied == 0:
        queen_list[q] = [(state[y0][x0].num), (state[y+1][x+1].num),False]
        q+=1
        x+=1 
        y+=1
    if x<6 and y<6:
        end[e] = [2,y,x]
        e+=1
    x=x0
    y=y0
    while x != 0 and y != 7 and state[y+1][x-1].occupied == 0:
        queen_list[q] = [(state[y0][x0].num), (state[y+1][x-1].num),False]
        q+=1
        x-=1
        y+=1
    if x>1 and y<6:
        end[e] = [3,y,x]
        e+=1
    x=x0
    y=y0
    while x != 0 and y != 0 and state[y-1][x-1].occupied == 0:
        queen_list[q] = [(state[y0][x0].num), (state[y-1][x-1].num),False]
        q+=1
        x-=1
        y-=1
    if x>1 and y>1:
        end[e] = [4,y,x]
        e+=1
    x=x0
    y=y0
    while x != 7 and y != 0 and state[y-1][x+1].occupied == 0:
        queen_list[q] = [(state[y0][x0].num), (state[y-1][x+1].num),False]
        q+=1
        x+=1
        y-=1
    if x<6 and y>1:
        end[e] = [1,y,x]
        e+=1
    return queen_list,end

def queen_take_list(colour,state,num,end):
    i=0
    forced = [[0,0,False]]*15
    f=0
    while i<4 and end[i][0] != 0:
        y=end[i][1]
        x=end[i][2]
        direction=end[i][0]
        if direction == 1:
            if (state[y-1][x+1].occupied != colour and state[y-1][x+1].occupied != colour+2) and state[y-1][x+1].occupied !=0 and state[y-2][x+2].occupied == 0:
                        forced[f] = [num,state[y-2][x+2].num,True]
                        f+=1
                        xtemp=x+3
                        ytemp=y-3
                        while xtemp <=7 and ytemp >= 0 and state[ytemp][xtemp].occupied == 0:
                            forced[f] = [num, (state[ytemp][xtemp].num),True]
                            f+=1
                            xtemp+=1
                            ytemp-=1
        elif direction == 4 :
            if (state[y-1][x-1].occupied != colour and state[y-1][x-1].occupied != colour+2) and state[y-1][x-1].occupied !=0 and state[y-2][x-2].occupied == 0:
                        forced[f] = [num,state[y-2][x-2].num,True]
                        f+=1
                        xtemp=x-3
                        ytemp=y-3
                        while xtemp >=0 and ytemp >= 0 and state[ytemp][xtemp].occupied == 0:
                            forced[f] = [num, (state[ytemp][xtemp].num),True]
                            f+=1
                            xtemp-=1
                            ytemp-=1
        elif direction == 3:
             if (state[y+1][x-1].occupied != colour and state[y+1][x-1].occupied != colour+2) and state[y+1][x-1].occupied !=0 and state[y+2][x-2].occupied == 0:
                        forced[f] = [num,state[y+2][x-2].num,True]
                        f+=1
                        xtemp=x-3
                        ytemp=y+3
                        while xtemp >=0 and ytemp <=7 and state[ytemp][xtemp].occupied == 0:
                            forced[f] = [num, (state[ytemp][xtemp].num),True]
                            f+=1
                            xtemp-=1
                            ytemp+=1
        elif direction==2 :
            if (state[y+1][x+1].occupied != colour and state[y+1][x+1].occupied != colour+2) and state[y+1][x+1].occupied !=0 and state[y+2][x+2].occupied == 0:
                        forced[f] = [num,state[y+2][x+2].num,True]
                        f+=1
                        xtemp=x+3
                        ytemp=y+3
                        while xtemp <=7 and ytemp <=7 and state[ytemp][xtemp].occupied == 0:
                            forced[f] = [num, (state[ytemp][xtemp].num),True]
                            f+=1
                            xtemp+=1
                            ytemp+=1
        i += 1
    return forced

def list_take_possible(colour,state,location):
    forced=[[0,0,False]]*20
    f=0
    for i in range(12):
        if location[i]:
            x=location[i][1]
            y=location[i][0]
            piece = location[i][2]
            if piece == 1:
                if x<6 and y>1:
                    if (state[y-1][x+1].occupied != colour and state[y-1][x+1].occupied != colour+2) and state[y-1][x+1].occupied !=0 and state[y-2][x+2].occupied == 0:
                        forced[f] = [state[y][x].num,state[y-2][x+2].num,True]
                        f+=1
                if y>1 and x>1 :
                    if (state[y-1][x-1].occupied != colour and state[y-1][x-1].occupied != colour+2) and state[y-1][x-1].occupied !=0 and state[y-2][x-2].occupied == 0:
                        forced[f] = [state[y][x].num,state[y-2][x-2].num,True]
                        f+=1
                if y<6 and x>1 :
                    if (state[y+1][x-1].occupied != colour and state[y+1][x-1].occupied != colour+2) and state[y+1][x-1].occupied !=0 and state[y+2][x-2].occupied == 0:
                        forced[f] = [state[y][x].num,state[y+2][x-2].num,True]
                        f+=1
                if y<6 and x<6 :
                    if (state[y+1][x+1].occupied != colour and state[y+1][x+1].occupied != colour+2) and state[y+1][x+1].occupied !=0 and state[y+2][x+2].occupied == 0:
                        forced[f] = [state[y][x].num,state[y+2][x+2].num,True]
                        f+=1
    return forced   

def black_move(state,location,piece):
    if piece<=0:
        normal=[[0,0,False]]*30
        forced=list_take_possible(2,state,location)
        n=0
        for i in range(12):
          if location[i]:  
            if location[i][2] == 1:
                    if location[i][1] != 7 and location[i][0] != 0 and state[(location[i][0])-1][(location[i][1])+1].occupied == 0:
                        normal[n] = [(state[location[i][0]][location[i][1]].num), (state[(location[i][0])-1][(location[i][1])+1].num),False]
                        n+=1
                    #elif location[i][1] < 6:
                    #   if (state[(location[i][0])-1][(location[i][1])+1].occupied == 1 or state[(location[i][0])-1][(location[i][1])+1].occupied == 3) and state[(location[i][0])-2][(location[i][1])+2].occupied == 0:
                    #      forced[f] = [(state[location[i][0]][location[i][1]].num), (state[(location[i][0])-2][(location[i][1])+2].num),True]
                    #     f+=1
                    if location[i][1] != 0 and location[i][0] != 0 and state[(location[i][0])-1][(location[i][1])-1].occupied == 0:
                        normal[n] = [state[location[i][0]][location[i][1]].num, state[(location[i][0])-1][(location[i][1])-1].num,False]
                        n+=1
                    #elif location[i][1] > 1:
                    #   if (state[(location[i][0])-1][(location[i][1])-1].occupied == 1 or state[(location[i][0])-1][(location[i][1])-1].occupied == 3) and state[(location[i][0])-2][(location[i][1])-2].occupied == 0:
                    #      forced[f] = [(state[location[i][0]][location[i][1]].num), (state[(location[i][0])-2][(location[i][1])-2].num),True]
                    #     f+=1
            if location[i][2] == 2:
                temp=state[location[i][0]][location[i][1]]
                queen_list,end=queen_movement(location[i][1],location[i][0],state) #queen movement
                normal,n=merge_list(normal,queen_list,n) #queen movement
                forced = merge_list2(forced,queen_take_list(2,state,temp.num,end))
        if forced[0][2] == True:
            #print(location)
            return forced
        else:
            return normal
    else:
         forced=single_take(2,state,location,piece)
         return forced

def white_move(state,location,piece):
    if piece<=0:
        normal=[[0,0,False]]*30
        #forced=[[0,0,False]]*20
        forced = list_take_possible(1,state,location)
        n=0
        for i in range(12):
          if location[i]:  
            if location[i][2] == 1:
                    if location[i][1] != 7 and location[i][0] != 7 and state[(location[i][0])+1][(location[i][1])+1].occupied == 0:
                        normal[n] = [(state[location[i][0]][location[i][1]].num), (state[(location[i][0])+1][(location[i][1])+1].num),False]
                        n+=1
                    if location[i][1] != 0 and location[i][0] != 7 and state[(location[i][0])+1][(location[i][1])-1].occupied == 0:
                        normal[n] = [state[location[i][0]][location[i][1]].num, state[(location[i][0])+1][(location[i][1])-1].num,False]
                        n+=1

            if location[i][2] == 2:
                temp=state[location[i][0]][location[i][1]]
                queen_list,end=queen_movement(location[i][1],location[i][0],state) #queen movement
                normal,n=merge_list(normal,queen_list,n)
                forced = merge_list2(forced,queen_take_list(1,state,temp.num,end))
        if forced[0][2] == True:
            return forced
        else:
            return normal
    else:
        forced = single_take(1,state,location,piece)
        return forced
def chainpiece(x,y,location):
    for i in range(12):
       if location[i]:
        if location[i][0]== y and location[i][1] == x:
            return i

def find_square_bynum(state,num):
    for i in range(8):
        for j in range(8):
            if state[i][j]:
                if state[i][j].num == num:
                    return i,j
def update_location(x1,y1,x2,y2,location):
    for i in range(12):
      if location[i]:
        if location[i][0]== y1 and location[i][1] == x1:
            location[i] = [y2,x2,location[i][2]]
            return location
        
def delete_location(x,y,location):
    for i in range(12):
       if location[i]:
        if location[i][0]== y and location[i][1] == x:
            location[i] = None
            return location
def promote_location(x,y,location):
    for i in range(12):
       if location[i]:
        if location[i][0]== y and location[i][1] == x:
            location[i][2]=2
            return location
        
def single_take(colour,state,location,position):
    piece = state[location[position][0]][location[position][1]].occupied
    x = location[position][1]
    y = location[position][0]
    num = state[location[position][0]][location[position][1]].num
    forced = [[0,0,False]]*15
    f=0
    if piece == colour:
        if x<6 and y>1:
            if (state[y-1][x+1].occupied != colour and state[y-1][x+1].occupied != colour+2) and state[y-1][x+1].occupied !=0 and state[y-2][x+2].occupied == 0:
                forced[f] = [num,state[y-2][x+2].num,True]
                f+=1
        if y>1 and x>1 :
            if (state[y-1][x-1].occupied != colour and state[y-1][x-1].occupied != colour+2) and state[y-1][x-1].occupied !=0 and state[y-2][x-2].occupied == 0:
                forced[f] = [num,state[y-2][x-2].num,True]#
                f+=1
        if y<6 and x>1 :
            if (state[y+1][x-1].occupied != colour and state[y+1][x-1].occupied != colour+2) and state[y+1][x-1].occupied !=0 and state[y+2][x-2].occupied == 0:
                forced[f] = [num,state[y+2][x-2].num,True]#
                f+=1
        if y<6 and x<6 :
            if (state[y+1][x+1].occupied != colour and state[y+1][x+1].occupied != colour+2) and state[y+1][x+1].occupied !=0 and state[y+2][x+2].occupied == 0:
                forced[f] = [num,state[y+2][x+2].num,True]#
                f+=1
    elif piece == colour+2:
        y1=y
        x1=x
        while x1 != 7 and y1 != 7 and state[y1+1][x1+1].occupied == 0:
            x1+=1 
            y1+=1
        if x1<6 and y1<6:
            if (state[y1+1][x1+1].occupied != colour and state[y1+1][x1+1].occupied != colour+2) and state[y1+1][x1+1].occupied !=0 and state[y1+2][x1+2].occupied == 0:
                forced[f] = [num,state[y1+2][x1+2].num,True]
                f+=1
                xtemp=x1+3
                ytemp=y1+3
                while xtemp <=7 and ytemp <=7 and state[ytemp][xtemp].occupied == 0:
                    forced[f] = [num, (state[ytemp][xtemp].num),True]
                    f+=1
                    xtemp+=1
                    ytemp+=1
        y1=y
        x1=x
        while x1 != 0 and y1 != 7 and state[y1+1][x1-1].occupied == 0:
            x1-=1
            y1+=1
        if y1<6 and x1>1 :
            if (state[y1+1][x1-1].occupied != colour and state[y1+1][x1-1].occupied != colour+2) and state[y1+1][x1-1].occupied !=0 and state[y1+2][x1-2].occupied == 0:
                forced[f] = [num,state[y1+2][x1-2].num,True]
                f+=1
                xtemp=x1-3
                ytemp=y1+3
                while xtemp >=0 and ytemp <=7 and state[ytemp][xtemp].occupied == 0:
                    forced[f] = [num, (state[ytemp][xtemp].num),True]
                    f+=1
                    xtemp-=1
                    ytemp+=1
        y1=y
        x1=x
        while x1 != 0 and y1 != 0 and state[y1-1][x1-1].occupied == 0:
            x1-=1
            y1-=1
        if y1>1 and x1>1 :
            if (state[y1-1][x1-1].occupied != colour and state[y1-1][x1-1].occupied != colour+2) and state[y1-1][x1-1].occupied !=0 and state[y1-2][x1-2].occupied == 0:
                forced[f] = [num,state[y1-2][x1-2].num,True]
                f+=1
                xtemp=x1-3
                ytemp=y1-3
                while xtemp >=0 and ytemp >= 0 and state[ytemp][xtemp].occupied == 0:
                    forced[f] = [num, (state[ytemp][xtemp].num),True]
                    f+=1
                    xtemp-=1
                    ytemp-=1
        x1=x
        y1=y
        while x1 != 7 and y1 != 0 and state[y1-1][x1+1].occupied == 0:
            x1+=1
            y1-=1
        if x1<6 and y1>1:
            if (state[y1-1][x1+1].occupied != colour and state[y1-1][x1+1].occupied != colour+2) and state[y1-1][x1+1].occupied !=0 and state[y1-2][x1+2].occupied == 0:
                forced[f] = [num,state[y1-2][x1+2].num,True]
                f+=1
                xtemp=x1+3
                ytemp=y1-3
                while xtemp <=7 and ytemp >= 0 and state[ytemp][xtemp].occupied == 0:
                    forced[f] = [num, (state[ytemp][xtemp].num),True]
                    f+=1
                    xtemp+=1
                    ytemp-=1
    return forced

def take_piece(x1,y1,x2,y2,colour,state,location):
    if x1 > x2:
        if y1 > y2 :
            Ym = y2+1
            Xm = x2+1
            ydir=-1
        else:
            Ym=y2-1
            Xm = x2+1
            ydir=1
        xdir=-1
    elif y1 > y2:
            Ym=y2+1
            Xm = x2-1
            ydir=-1
            xdir=1
    else:
            Ym=y2-1
            Xm = x2-1
            ydir=1
            xdir=1
# ^^^^ find the direction that the take is in
    if state[y1][x1].occupied==colour:#if it is a normal piece, find the middle square
            middle=state[Ym][Xm]
    else:
        x=x1
        y=y1
        while x!=x2 and y!=y2:#If the piece is a queen search every square on the line until the first piece is found. This is the taken piece
            if state[y][x].occupied!=0 and state[y][x].occupied!=colour and state[y][x].occupied!=colour+2:
                middle=state[y][x]
                Ym=y
                Xm=x
            x+=xdir
            y+=ydir     
    middle.occupied=0#remove the piece from the board and the location array
    location=delete_location(Xm,Ym,location)

    if check_take_possible(x2,y2,colour,state,state[y1][x1].occupied):#check if another take is possible
        return 1,location
    else:
        return 0,location










