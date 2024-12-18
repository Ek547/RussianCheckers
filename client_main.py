if __name__ == "__main__":
  import pygame, sys
  import time
  from pygame.locals import QUIT,MOUSEBUTTONDOWN,MOUSEBUTTONUP,KEYDOWN,K_e,K_r,K_s,K_l
  from board import state,draw,initial_setup ,display_turn,bot_highlight,bot_unhighlight,edit_mode,change_piece
  from game import find_possible,highlight_possible,unhighlight_possible,move_piece,bot_move
  import constants
  from engine import minimax,ThreadWithReturnValue
  from menu import main_menu
  from server_connection import Network

#import functions from other files
# This is the entry point for the menu. It's called from main. py and the menu should be placed in a file
  main_menu() # call main menu for settings
  pygame.init()
  pygame.mixer.init()
  try:
    constants.movesound = pygame.mixer.Sound("move.wav")
  except:
    constants.file = False
  end=0  #game is not over
  clock=pygame.time.Clock()
  state = initial_setup(state)#setup board
  WIN = draw (state)# display board for first time
  turn=1 #set initial whites's turn
  possible_found=False #initialise 
  bot=[0.0,0,0]
  piece=-1
  n = Network()
  p = n.getid()
  constants.botplayer = (p+1)%2
  print(p)
  while True: # Forever loop
      if possible_found==False and end == 0: #check if list of possible  moves has beeen generated and if the game is over
        possible=find_possible(state,turn) #generate list of possible moves
        if possible[0]==[0,0,False]: #check there any possible moves
            end=1 #end of game
        
        display_turn(turn,WIN,end)# redraw the banner  
        possible_found = True
        #print(staticeval(state,constants.whitelocation,constants.blacklocation))
        if end == 0:# check if bot is playing
          if turn%2==constants.botplayer: #check if it is the computer's turn
            #if possible[1][0]!=0: #check if there is only one possible move
              #start=time.time()
              #simult = n.send(pickle.dumps((state,constants.whitelocation,constants.blacklocation,constants.depth,-10000000,10000000,turn,piece)))
              # create a thread for the minimax algoritm)
            if constants.comp == True:
                simult = ThreadWithReturnValue(target= minimax, args=(state,constants.whitelocation,constants.blacklocation,constants.depth,-10000000,10000000,turn,piece))
                # create a thread for the minimax algoritm
                simult.start()#start minimax thread
                while simult.is_alive()==True:
                    pygame.event.pump()
                    #keep the pygame window alive while the minimax is running
                    pygame.time.wait(0.5)
                pygame.event.clear()
                bot=simult.join() #get best move from the minimax thread
            else:
                received = False
                print("waiting")
                while received == False:
                    bot = n.receive()
                    if bot != [0,0,0]: 
                        received = True
                        print(bot)
                    else:
                        pygame.event.pump()
                pygame.event.clear()

            #else:
              #bot[1]=possible[0][0]
              #bot[2]=possible[0][1]
            turn,change,piece=bot_move(bot[1],bot[2],state,turn,possible,WIN,piece)# move bot piece
            bot_highlight(bot[1],bot[2],state,WIN,constants.botplayer)
            if change == True:
              possible_found=False
              if constants.file == True:
                pygame.mixer.Sound.play(constants.movesound)# play sound
              time.sleep(0.1)
          #pygame.display.update()#update screen
      else:
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
          elif event.type == MOUSEBUTTONDOWN: 
            if event.button==1:
              down=event.pos
              if down[0]<=constants.width and down[1]<=constants.height:
                x1 = down[0] * 8 // constants.width
                y1 = down[1] * 8 // constants.height
                highlight_possible(down,state,possible,WIN)
          elif event.type == MOUSEBUTTONUP:
            if event.button == 1: # 1 == left button
              dark=unhighlight_possible(state,WIN)
              up = event.pos
              if up[0]<=constants.width and up[1]<=constants.height:
                temp_turn = turn
                turn,change,piece=move_piece(up,x1,y1,state,turn,possible,WIN,piece)
                if change == True:
                    bot_unhighlight(state,WIN)
                    square1 = state[y1][x1]
                    square2 = state[up[1] * 8 // constants.height][up[0] * 8 // constants.width]
                    send = [temp_turn,square1.num,square2.num]
                    n.send(send)
                    possible_found=False
                    if constants.file==True:
                      pygame.mixer.Sound.play(constants.movesound)
                    time.sleep(0.1)

          
              
              
      pygame.display.update()
        
      clock.tick(60)
