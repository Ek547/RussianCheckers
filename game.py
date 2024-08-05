import constants
from board import find_square_bynum,redraw_specific,merge_list,merge_list2
def find_possible(state,turn):
    if turn%2 == 1:
       possible=white_move(state)
    elif turn%2 == 0:
        possible = black_move(state)
    return possible

def take_piece(x1,y1,x2,y2,colour,WIN,state,location):
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
    if state[y1][x1].occupied==colour:
            middle=state[Ym][Xm]
    else:
        for x,y in zip(range(x1,x2,xdir),range(y1,y2,ydir)):
            if state[y][x].occupied!=0 and state[y][x].occupied!=colour and state[y][x].occupied!=colour+2:
                middle=state[y][x]
                Ym=y
                Xm=x

    middle.occupied=0
    location=delete_location(Xm,Ym,location)
    redraw_specific(middle,WIN)

    if check_take_possible(x2,y2,colour,state,state[y1][x1].occupied):
        return 1,location
    else:
        return 0,location
    
  
def check_take_possible(x,y,colour,state,piece):
    if piece == colour:
        if x<6 and y>1:
            if (state[y-1][x+1].occupied != colour and state[y-1][x+1].occupied != colour+2) and state[y-1][x+1].occupied !=0 and state[y-2][x+2].occupied == 0:
                return True
        if y>1 and x>1 :
            if (state[y-1][x-1].occupied != colour and state[y-1][x-1].occupied != colour+2) and state[y-1][x-1].occupied !=0 and state[y-2][x-2].occupied == 0:
                return True
        if y<6 and x>1 :
            if (state[y+1][x-1].occupied != colour and state[y+1][x-1].occupied != colour+2) and state[y+1][x-1].occupied !=0 and state[y+2][x-2].occupied == 0:
                return True
        if y<6 and x<6 :
            if (state[y+1][x+1].occupied != colour and state[y+1][x+1].occupied != colour+2) and state[y+1][x+1].occupied !=0 and state[y+2][x+2].occupied == 0:
                return True
    elif piece == colour+2:
        y1=y
        x1=x
        while x1 != 7 and y1 != 7 and state[y1+1][x1+1].occupied == 0:
            x1+=1 
            y1+=1
        if x1<6 and y1<6:
            if (state[y1+1][x1+1].occupied != colour and state[y1+1][x1+1].occupied != colour+2) and state[y1+1][x1+1].occupied !=0 and state[y1+2][x1+2].occupied == 0:
                return True
        y1=y
        x1=x
        while x1 != 0 and y1 != 7 and state[y1+1][x1-1].occupied == 0:
            x1-=1
            y1+=1
        if y1<6 and x1>1 :
            if (state[y1+1][x1-1].occupied != colour and state[y1+1][x1-1].occupied != colour+2) and state[y1+1][x1-1].occupied !=0 and state[y1+2][x1-2].occupied == 0:
                return True
        y1=y
        x1=x
        while x1 != 0 and y1 != 0 and state[y1-1][x1-1].occupied == 0:
            x1-=1
            y1-=1
        if y1>1 and x1>1 :
            if (state[y1-1][x1-1].occupied != colour and state[y1-1][x1-1].occupied != colour+2) and state[y1-1][x1-1].occupied !=0 and state[y1-2][x1-2].occupied == 0:
                return True
        x1=x
        y1=y
        while x1 != 7 and y1 != 0 and state[y1-1][x1+1].occupied == 0:
            x1+=1
            y1-=1
        if x1<6 and y1>1:
            if (state[y1-1][x1+1].occupied != colour and state[y1-1][x1+1].occupied != colour+2) and state[y1-1][x1+1].occupied !=0 and state[y1-2][x1+2].occupied == 0:
                return True
    return False

def queen_movement(x0,y0,state):
    y=y0
    x=x0
    queen_list=[[0,0,False]]*20
    e=0
    constants.end=[[0,0]]*4
    constants.q=0
    while x != 7 and y != 7 and state[y+1][x+1].occupied == 0:
        queen_list[constants.q] = [(state[y0][x0].num), (state[y+1][x+1].num),False]
        constants.q+=1
        x+=1 
        y+=1
    if x<6 and y<6:
        constants.end[e] = [2,y,x]
        e+=1
    x=x0
    y=y0
    while x != 0 and y != 7 and state[y+1][x-1].occupied == 0:
        queen_list[constants.q] = [(state[y0][x0].num), (state[y+1][x-1].num),False]
        constants.q+=1
        x-=1
        y+=1
    if x>1 and y<6:
        constants.end[e] = [3,y,x]
        e+=1
    x=x0
    y=y0
    while x != 0 and y != 0 and state[y-1][x-1].occupied == 0:
        queen_list[constants.q] = [(state[y0][x0].num), (state[y-1][x-1].num),False]
        constants.q+=1
        x-=1
        y-=1
    if x>1 and y>1:
        constants.end[e] = [4,y,x]
        e+=1
    x=x0
    y=y0
    while x != 7 and y != 0 and state[y-1][x+1].occupied == 0:
        queen_list[constants.q] = [(state[y0][x0].num), (state[y-1][x+1].num),False]
        constants.q+=1
        x+=1
        y-=1
    if x<6 and y>1:
        constants.end[e] = [1,y,x]
        e+=1
    return queen_list
    
def queen_take_list(colour,state,num):
    i=0
    forced = [[0,0,False]]*8
    f=0
    while i<4 and constants.end[i][0] != 0:#iterate through end
        y=constants.end[i][1]
        x=constants.end[i][2]
        direction=constants.end[i][0]
        if direction == 1:#check each direction
            if (state[y-1][x+1].occupied != colour and state[y-1][x+1].occupied != colour+2) and state[y-1][x+1].occupied !=0 and state[y-2][x+2].occupied == 0:#check empty squares
                        forced[f] = [num,state[y-2][x+2].num,True]#add to forced
                        f+=1
                        xtemp=x+3
                        ytemp=y-3
                        while xtemp <=7 and ytemp >= 0 and state[ytemp][xtemp].occupied == 0:
                            forced[f] = [num, (state[ytemp][xtemp].num),True]#add all squares after the take
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
        #temp1=state[constants.end[i][1]][constants.end[i][2]]




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

def white_move(state):
    normal=[[0,0,False]]*30
    forced = list_take_possible(1,state,constants.whitelocation)#updates values in the constants file
    n=0
    for i in range(12):#iterate through white location
      if constants.whitelocation[i]:  
        if constants.whitelocation[i][2] == 1:#check if piece is queen
                if constants.whitelocation[i][1] != 7 and constants.whitelocation[i][0] != 7 and state[(constants.whitelocation[i][0])+1][(constants.whitelocation[i][1])+1].occupied == 0:
                    normal[n] = [(state[constants.whitelocation[i][0]][constants.whitelocation[i][1]].num), (state[(constants.whitelocation[i][0])+1][(constants.whitelocation[i][1])+1].num),False]
                    n+=1
                if constants.whitelocation[i][1] != 0 and constants.whitelocation[i][0] != 7 and state[(constants.whitelocation[i][0])+1][(constants.whitelocation[i][1])-1].occupied == 0:
                    normal[n] = [state[constants.whitelocation[i][0]][constants.whitelocation[i][1]].num, state[(constants.whitelocation[i][0])+1][(constants.whitelocation[i][1])-1].num,False]
                    n+=1
        if constants.whitelocation[i][2] == 2:
            temp=state[constants.whitelocation[i][0]][constants.whitelocation[i][1]]
            queen_list=queen_movement(constants.whitelocation[i][1],constants.whitelocation[i][0],state) #uses the end from take
            normal,n=merge_list(normal,queen_list,n)
            forced = merge_list2(forced,queen_take_list(1,state,temp.num))
    if forced[0][2] == True:
        return forced
    else:
        return normal

def black_move(state):
    normal=[[0,0,False]]*30
    forced=list_take_possible(2,state,constants.blacklocation)
    n=0
    for i in range(12):
      if constants.blacklocation[i]:  
        if constants.blacklocation[i][2] == 1:
                if constants.blacklocation[i][1] != 7 and constants.blacklocation[i][0] != 0 and state[(constants.blacklocation[i][0])-1][(constants.blacklocation[i][1])+1].occupied == 0:
                    normal[n] = [(state[constants.blacklocation[i][0]][constants.blacklocation[i][1]].num), (state[(constants.blacklocation[i][0])-1][(constants.blacklocation[i][1])+1].num),False]
                    n+=1
                if constants.blacklocation[i][1] != 0 and constants.blacklocation[i][0] != 0 and state[(constants.blacklocation[i][0])-1][(constants.blacklocation[i][1])-1].occupied == 0:
                    normal[n] = [state[constants.blacklocation[i][0]][constants.blacklocation[i][1]].num, state[(constants.blacklocation[i][0])-1][(constants.blacklocation[i][1])-1].num,False]
                    n+=1
        if constants.blacklocation[i][2] == 2:
            temp=state[constants.blacklocation[i][0]][constants.blacklocation[i][1]]
            queen_list=queen_movement(constants.blacklocation[i][1],constants.blacklocation[i][0],state) #queen movement
            #print(queen_list)
            normal,n=merge_list(normal,queen_list,n) #queen movement
            forced = merge_list2(forced,queen_take_list(2,state,temp.num))
    if forced[0][2] == True:
        #print(constants.blacklocation)
        return forced
    else:
        return normal
    
def search_possible(possible,num1,num2):
  i=0
  while possible[i][1] !=0:
    if possible[i][0] == num1 and possible[i][1]== num2:
      if possible[i][2]==True:
        return True,True
      return True,False
    i+=1
  return False,True



def highlight_possible(down,state,possible,WIN):
    select=state[down[1] * 8 // constants.height][down[0] * 8//constants.width]
    i=0
    if select != None:
        while  i < len(possible) and possible[i][1] !=0:
            if possible[i][0] == select.num:
                #print(select.num)
                temp=find_square_bynum(state,possible[i][1])
                temp.occupied=5
                redraw_specific(temp,WIN)
            i+=1
def unhighlight_possible(state,WIN):
    for i in range(8):
        for j in range(8):
            if state[i][j]:
                if state[i][j].occupied==5:
                    state[i][j].occupied = 0
                    redraw_specific(state[i][j],WIN)
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
def chainpiece(x,y,location):
    for i in range(12):
       if location[i]:
        if location[i][0]== y and location[i][1] == x:
            return i

def move_piece(up,x1,y1,state,turn,possible,WIN,piece):
    x2 =  up[0] * 8 // constants.width
    y2 =  up[1] * 8 // constants.height
    if x1 != x2 and y1 != y2 and (x2+y2)%2 != 0:
        temp1 = state[y1][x1]
        temp2 = state[y2][x2]
        if turn%2 == 1 and temp1 and (temp1.occupied==1 or temp1.occupied==3):
            colour = 1#
            if piece>=0:
                checkpiece=chainpiece(x1,y1,constants.whitelocation)
        elif turn % 2 == 0 and temp1 and (temp1.occupied == 2 or temp1.occupied == 4):
            colour = 2
            if piece>=0:
                checkpiece=chainpiece(x1,y1,constants.blacklocation)

        else:
            #print(temp1.occupied)
            #print("out")
            return turn,False,piece
        if piece>=0 and checkpiece != piece:
            return turn,False,piece
        move = search_possible(possible,temp1.num,temp2.num)
        if move[0] == True:#check if move is possible
            if move[1] == True:#check if take
                if colour == 2:
                    loc=constants.whitelocation
                    sub,constants.whitelocation=take_piece(x1,y1,x2,y2,colour,WIN,state,loc)
                    if sub==1:
                        piece = chainpiece(x1,y1,constants.blacklocation)
                    else:
                        piece = -1
                elif colour == 1:
                    loc=constants.blacklocation
                    sub,constants.blacklocation=take_piece(x1,y1,x2,y2,colour,WIN,state,loc)
                    if sub==1:
                        piece = chainpiece(x1,y1,constants.whitelocation)
                    else:
                        piece = -1
                turn-=sub
                #take piece plus take again
            turn+=1
            if temp1.occupied == 1 and y2 == 7 :
                temp2.occupied = 3
                constants.whitelocation= promote_location(x1,y1,constants.whitelocation)
                temp1.occupied=0
            elif temp1.occupied == 2 and y2 == 0 :
                temp2.occupied = 4
                constants.blacklocation= promote_location(x1,y1,constants.blacklocation)
                temp1.occupied=0
            if temp1.occupied == 4:
                temp2.occupied = 4
            elif temp1.occupied == 3:
                temp2.occupied = 3
            elif temp1.occupied == colour:
                temp2.occupied = colour
            temp1.occupied = 0
            if colour == 1:
                constants.whitelocation = update_location(x1,y1,x2,y2,constants.whitelocation)
            else:
                constants.blacklocation = update_location(x1,y1,x2,y2,constants.blacklocation)
            redraw_specific(temp1,WIN)
            redraw_specific(temp2,WIN)

            #draw_pieces(state,WIN)
            ##if move[1] == True:
              #  turn=turn-take_piece(x1,y1,x2,y2,colour,WIN,state)#take piece plus take again
            #turn+=1
        else: return turn,False,piece
    else:return turn,False,piece
    return turn,True,piece

def find_square_bynum2(state,num):
    for i in range(8):
        for j in range(8):
            if state[i][j]:
                if state[i][j].num == num:
                    return i,j

def bot_move(square1,square2,state,turn,possible,WIN,piece):
    y1,x1=find_square_bynum2(state,square1)
    y2,x2 = find_square_bynum2(state,square2)
    if x1 != x2 and y1 != y2 and (x2+y2)%2 != 0:
        temp1 = state[y1][x1]
        temp2 = state[y2][x2]
        if turn%2 == 1 and temp1 and (temp1.occupied==1 or temp1.occupied==3):
            colour = 1#
            if piece>=0:
                checkpiece=chainpiece(x1,y1,constants.whitelocation)
        elif turn % 2 == 0 and temp1 and (temp1.occupied == 2 or temp1.occupied == 4):
            colour = 2
            if piece>=0:
                checkpiece=chainpiece(x1,y1,constants.blacklocation)

        else:
            #print(temp1.occupied)
            #print("out")
            return turn,False,piece
        if piece>=0 and checkpiece != piece:
            return turn,False,piece
        move = search_possible(possible,temp1.num,temp2.num)
        if move[0] == True:#check if move is possible
            if move[1] == True:#check if take
                if colour == 2:
                    loc=constants.whitelocation
                    sub,constants.whitelocation=take_piece(x1,y1,x2,y2,colour,WIN,state,loc)
                    if sub==1:
                        piece = chainpiece(x1,y1,constants.blacklocation)
                    else:
                        piece = -1
                elif colour == 1:
                    loc=constants.blacklocation
                    sub,constants.blacklocation=take_piece(x1,y1,x2,y2,colour,WIN,state,loc)
                    if sub==1:
                        piece = chainpiece(x1,y1,constants.whitelocation)
                    else:
                        piece = -1
                turn-=sub
                #take piece plus take again
            turn+=1
            if temp1.occupied == 1 and y2 == 7 :
                temp2.occupied = 3
                constants.whitelocation= promote_location(x1,y1,constants.whitelocation)
                temp1.occupied=0
            elif temp1.occupied == 2 and y2 == 0 :
                temp2.occupied = 4
                constants.blacklocation= promote_location(x1,y1,constants.blacklocation)
                temp1.occupied=0
            if temp1.occupied == 4:
                temp2.occupied = 4
            elif temp1.occupied == 3:
                temp2.occupied = 3
            elif temp1.occupied == colour:
                temp2.occupied = colour
            temp1.occupied = 0
            if colour == 1:
                constants.whitelocation = update_location(x1,y1,x2,y2,constants.whitelocation)
            else:
                constants.blacklocation = update_location(x1,y1,x2,y2,constants.blacklocation)
            redraw_specific(temp1,WIN)
            redraw_specific(temp2,WIN)

            #draw_pieces(state,WIN)
            ##if move[1] == True:
              #  turn=turn-take_piece(x1,y1,x2,y2,colour,WIN,state)#take piece plus take again
            #turn+=1
        else: return turn,False,piece
    else:return turn,False,piece
    return turn,True,piece




