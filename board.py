import pygame
#from checkers import Pieces #place_pieces,draw_pieces,draw_single
import constants # width,height,brown,white,square



class squares: 
  def __init__(self,num,x,y):
    self.num= num #num is square number
    self.pix_centreX = x #the X cordinate where a the piece should be drawn
    self.pix_centreY = y #the Y cordinate where a the piece should be drawn
    self.occupied=0 #The piece on the square, 0=empty

#board = [([None, squares(), None, squares(), None, squares(), None, squares()],[squares(), None, squares(), None, squares(), None, squares() ,None])*4] 
#          0                                    1                               2                   3                                                4                         5                                          6                                    7
row_0 = [None, squares(32,(1.5 * constants.square),(0.5 * constants.square)), None, squares(31,(3.5 * constants.square),(0.5 * constants.square)), None, squares(30,(5.5 * constants.square),(0.5 * constants.square)), None, squares(29,(7.5 * constants.square),(0.5 * constants.square))]
row_1 = [squares(28,(0.5 * constants.square),(1.5 * constants.square)), None, squares(27,(2.5 * constants.square),(1.5 * constants.square)), None, squares(26,(4.5 * constants.square),(1.5 * constants.square)), None, squares(25,(6.5 * constants.square),(1.5 * constants.square)) ,None]
row_2 = [None, squares(24,(1.5 * constants.square),(2.5 * constants.square)), None, squares(23,(3.5 * constants.square),(2.5 * constants.square)), None, squares(22,(5.5 * constants.square),(2.5 * constants.square)), None, squares(21,(7.5 * constants.square),(2.5 * constants.square))]
row_3 = [squares(20,(0.5 * constants.square),(3.5 * constants.square)), None, squares(19,(2.5 * constants.square),(3.5 * constants.square)), None, squares(18,(4.5 * constants.square),(3.5 * constants.square)), None, squares(17,(6.5 * constants.square),(3.5 * constants.square)) ,None]
row_4 = [None, squares(16,(1.5 * constants.square),(4.5 * constants.square)), None, squares(15,(3.5 * constants.square),(4.5 * constants.square)), None, squares(14,(5.5 * constants.square),(4.5 * constants.square)), None, squares(13,(7.5 * constants.square),(4.5 * constants.square))]
row_5 = [squares(12,(0.5 * constants.square),(5.5 * constants.square)), None, squares(11,(2.5 * constants.square),(5.5 * constants.square)), None, squares(10,(4.5 * constants.square),(5.5 * constants.square)), None, squares( 9,(6.5 * constants.square),(5.5 * constants.square)) ,None]
row_6 = [None, squares( 8,(1.5 * constants.square),(6.5 * constants.square)), None, squares( 7,(3.5 * constants.square),(6.5 * constants.square)), None, squares( 6,(5.5 * constants.square),(6.5 * constants.square)), None, squares( 5,(7.5 * constants.square),(6.5 * constants.square))]
row_7 = [squares( 4,(0.5 * constants.square),(7.5 * constants.square)), None, squares( 3,(2.5 * constants.square),(7.5 * constants.square)), None, squares( 2,(4.5 * constants.square),(7.5 * constants.square)), None, squares( 1,(6.5 * constants.square),(7.5 * constants.square)) ,None]


state = [row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7]
print(state[3][2].occupied)

def draw(state): ##Initial setup + draw_pieces
    WIN = pygame.display.set_mode((constants.width, constants.height*1.125))
    for y in range(constants.height):
        for x in range(constants.width):
            pygame.draw.rect(WIN, (x + y) % 2 and constants.brown or constants.white, pygame.Rect(constants.square*x, constants.square*y, constants.square, constants.square))
    WIN = draw_pieces(state,WIN)
    return WIN
def initial_setup(state):#place the pieces and set up the location arrays
    n=0
    for i in range(3):
        for j in range (8):
            if state[i][j] != None:
                state[i][j].occupied = 1
                constants.whitelocation[n]=[i,j,1]#setup white location
                n+=1
    n=0
        
    for i in range(5,8):
        for j in range (8):
            if state[i][j] != None:
                state[i][j].occupied = 2
                constants.blacklocation[n]=[i,j,1]
                n+=1  
    return state

def draw_pieces(state,WIN):
    for i in range(8):
       for j in range(8):
          if state[i][j] != None:
            temp = state[i][j]
            if temp.occupied==1:
                pygame.draw.circle(WIN,[225,225,225],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
            elif temp.occupied==2:
                pygame.draw.circle(WIN,[25,25,25],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
            elif temp.occupied==5:
                pygame.draw.circle(WIN,[153,255,255],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)
            elif temp.occupied==3:
                pygame.draw.circle(WIN,[225,225,225],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
                pygame.draw.circle(WIN,[255,193,37],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)
            elif temp.occupied==4:
                pygame.draw.circle(WIN,[25,25,25],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
                pygame.draw.circle(WIN,[255,193,37],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)
            elif temp.occupied==0:
                pygame.draw.rect(WIN,constants.brown,[(temp.pix_centreX)-(constants.square/2), (temp.pix_centreY)-(constants.square/2), constants.square,constants.square], 0)
    return WIN



#WIN = draw (board)

def find_square_bynum(state,num):
    for i in range(8):
        for j in range(8):
            if state[i][j]:
                if state[i][j].num == num:
                    return state[i][j]
                

def redraw_specific(temp,WIN):
  if temp.occupied==0:
    pygame.draw.rect(WIN,constants.brown,[(temp.pix_centreX)-(constants.square/2), (temp.pix_centreY)-(constants.square/2), constants.square,constants.square], 0)
  else:
    draw_single(temp,WIN)

def draw_single(temp,WIN):
  pygame.draw.rect(WIN,constants.brown,[(temp.pix_centreX)-(constants.square/2), (temp.pix_centreY)-(constants.square/2), constants.square,constants.square], 0)
  if temp.occupied==1:
      pygame.draw.circle(WIN,[225,225,225],(temp.pix_centreX,temp.pix_centreY),0.43*constants.square)
  elif temp.occupied==2:
      pygame.draw.circle(WIN,[25,25,25],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
  elif temp.occupied==5:
      pygame.draw.circle(WIN,[153,255,255],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)
  elif temp.occupied==3:
    pygame.draw.circle(WIN,[225,225,225],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
    pygame.draw.circle(WIN,[255,193,37],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)
  elif temp.occupied==4:
    pygame.draw.circle(WIN,[25,25,25],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
    pygame.draw.circle(WIN,[255,193,37],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)


def display_turn(turn,WIN,end):
    pygame.draw.rect(WIN,constants.grey,pygame.Rect(0,constants.height,constants.width,constants.square))
    myfont = pygame.font.SysFont("monospace", constants.square//2)
    
    
    if (turn+end)%2 == 1:
        colour = "White"
        label = myfont.render(colour, 1, constants.white)
    else:
        colour= "Black"
        label = myfont.render(colour, 1, constants.black)
    if end == 0:
        WIN.blit(label, (constants.square, constants.height+0.25*constants.square))
        if constants.edit==False:
            pygame.draw.rect(WIN,(0,255,0),pygame.Rect(7*constants.square,constants.height,constants.square,constants.square))
        else:
            pygame.draw.rect(WIN,(255,0,0),pygame.Rect(7*constants.square,constants.height,constants.square,constants.square))     

    else:
        myfont = pygame.font.SysFont("corbel", constants.square)
        label = myfont.render(colour+" Wins!!!", 1, constants.black)
        WIN.blit(label, (constants.square, constants.height))
    pygame.display.update()


def draw_all(WIN,state):
    for i in range(len(constants.whitelocation)):
      temp = state[constants.whitelocation[i][0]][constants.whitelocation[i][1]]
      redraw_specific(temp,WIN)
    for i in range(len(constants.blacklocation)):
        temp = state[constants.blacklocation[i][0]][constants.blacklocation[i][1]]
        redraw_specific(temp,WIN)
    


def merge_list(normal,queen,n):
    j=0
    while n<len(normal) and j <= constants.q:
         normal[n]=queen[j]
         j+=1
         n+=1
    print(j)
    return normal,n-1

def merge_list2(forced,queen):
    i=0
    while forced[i][2] == True:
        i+=1
    for q in range(len(queen)):
        if queen[q][2] == True:
            forced[i]=queen[q]
            i+=1
    return forced





def bot_highlight(square1,square2,state,WIN,colour):
    temp=find_square_bynum(state,square2)
    temp2=find_square_bynum(state,square1)
    pygame.draw.rect(WIN,constants.red,[(temp.pix_centreX)-(constants.square/2), (temp.pix_centreY)-(constants.square/2), constants.square,constants.square], 0)
    pygame.draw.rect(WIN,constants.red,[(temp2.pix_centreX)-(constants.square/2), (temp2.pix_centreY)-(constants.square/2), constants.square,constants.square], 0)
    if temp.occupied==1:
      pygame.draw.circle(WIN,[225,225,225],(temp.pix_centreX,temp.pix_centreY),0.43*constants.square)
    elif temp.occupied==2:
        pygame.draw.circle(WIN,[25,25,25],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
    elif temp.occupied==3:
        pygame.draw.circle(WIN,[225,225,225],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
        pygame.draw.circle(WIN,[255,193,37],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)
    elif temp.occupied==4:
        pygame.draw.circle(WIN,[25,25,25],(temp.pix_centreX,temp.pix_centreY),0.45*constants.square)
        pygame.draw.circle(WIN,[255,193,37],(temp.pix_centreX,temp.pix_centreY),0.25*constants.square)
def bot_unhighlight(state,WIN):
    if constants.botplayer == 1:
        colour = 1
    else:
        colour = 2
    for i in range(8):
        for j in range(8):
            if state[i][j]:
                if state[i][j].occupied==0 or state[i][j].occupied==colour or state[i][j].occupied==colour+2:
                    redraw_specific(state[i][j],WIN)  

def test(state):
    for i in range(8):
        for j in range(8):
            if state[i][j]==None:
                print("  ",end="")
            else:
                print(state[i][j].occupied,end=" ")
        print()
def update_location(x1,y1,x2,y2,location):
    for i in range(12):
      if location[i]:
        if location[i][0]== y1 and location[i][1] == x1:
            location[i] = [y2,x2,location[i][2]]
            return location


def edit_mode(up,x1,y1,state,WIN):
    x2 =  up[0] * 8 // constants.width
    y2 =  up[1] * 8 // constants.height
    if (x1 != x2 or y1 != y2) and (x2+y2)%2 != 0 and (x1+y1)%2 != 0:
        temp1 = state[y1][x1]
        temp2 = state[y2][x2]
        if temp2.occupied == 0:
            colour = temp1.occupied
            temp2.occupied = colour
            temp1.occupied = 0
            redraw_specific(temp1,WIN)
            redraw_specific(temp2,WIN)
            if colour == 1 or colour == 3:
                constants.whitelocation = update_location(x1,y1,x2,y2,constants.whitelocation)
            else:
                constants.blacklocation = update_location(x1,y1,x2,y2,constants.blacklocation)
            return True,-1
    return False,-1

def change_piece(down,state,WIN):
    xc=down[0]
    yc=down[1]
    if yc <= constants.height and xc <= constants.width:
       x= xc * 8 // constants.width
       y =  yc * 8 // constants.height
       if state[y][x]:
        temp = state[y][x]
        if temp.occupied == 1:
            temp.occupied+=2
            constants.whitelocation = promote_location(x,y,constants.whitelocation)
        elif temp.occupied == 2:
            temp.occupied+=2
            constants.blacklocation = promote_location(x,y,constants.blacklocation)
        elif temp.occupied == 4:
            temp.occupied -= 2
            constants.blacklocation = unpromote_location(x,y,constants.blacklocation)
        elif temp.occupied == 3:
            temp.occupied -= 2
            constants.whitelocation = unpromote_location(x,y,constants.whitelocation)
        redraw_specific(temp,WIN)
    return state
    
            


def promote_location(x,y,location):
    for i in range(12):
       if location[i]:
        if location[i][0]== y and location[i][1] == x:
            location[i][2]=2
            return location
        
def unpromote_location(x,y,location):
    for i in range(12):
       if location[i]:
        if location[i][0]== y and location[i][1] == x:
            location[i][2]=1
            return location