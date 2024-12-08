if __name__ == "__main__":
  import pygame, sys
  import time
  from pygame.locals import QUIT,MOUSEBUTTONDOWN,MOUSEBUTTONUP,KEYDOWN,K_e,K_r,K_s,K_l
  from board import state,draw,initial_setup ,display_turn,bot_highlight,bot_unhighlight,edit_mode,change_piece
  from game import find_possible,highlight_possible,unhighlight_possible,move_piece,bot_move
  import constants
  from engine import minimax,ThreadWithReturnValue
  from menu import main_menu
  import pickle

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

  while True: # Forever loop
    if constants. edit == False:  #check if edit mode is on
      if possible_found==False and end == 0: #check if list of possible  moves has beeen generated and if the game is over
        possible=find_possible(state,turn) #generate list of possible moves
        if possible[0]==[0,0,False]: #check there any possible moves
            end=1 #end of game
            constants.movetime.pop(0)#
            #if constants.comp == True:
            print("depth = ", constants.depth)
            print("mean: ",sum(constants.movetime)/len(constants.movetime))
            print("max: ", max(constants.movetime))
            #adding time taken to array for data analysis
        
        display_turn(turn,WIN,end)# redraw the banner  
        possible_found = True
        #print(staticeval(state,constants.whitelocation,constants.blacklocation))
        if constants.comp == True and end == 0:# check if bot is playing
          if turn%2==constants.botplayer: #check if it is the computer's turn
            if possible[1][0]!=0: #check if there is only one possible move
              start=time.time()
              simult = ThreadWithReturnValue(target= minimax, args=(state,constants.whitelocation,constants.blacklocation,constants.depth,-10000000,10000000,turn,piece))
              # create a thread for the minimax algoritm
              simult.start()#start minimax thread
              while simult.is_alive()==True:
                pygame.event.pump()
                #keep the pygame window alive while the minimax is running
                time.sleep(0.5)
              pygame.event.clear()
              bot=simult.join() #get best move from the minimax thread   
              constants.movetime.append(time.time()-start)
            else:
              bot[1]=possible[0][0]
              bot[2]=possible[0][1]
            turn,change,piece=bot_move(bot[1],bot[2],state,turn,possible,WIN,piece)# move bot piece
            bot_highlight(bot[1],bot[2],state,WIN,constants.botplayer)
            if change == True:
              possible_found=False
              if constants.file == True:
                pygame.mixer.Sound.play(constants.movesound)# play sound
              time.sleep(0.1)
          pygame.display.update()#update screen
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
          if event.key == K_e:#toggle editmode
            constants.edit = not constants.edit
            if constants.edit == False: 
                possible_found=False
          elif event.key == K_r:#next player turn
            if constants.edit == True:
              turn+=1
              possible_found = False
          elif event.key == K_s:#next player turn
            if constants.edit == True:
              file = open("storedposition","wb")
              pickle.dump((state,constants.whitelocation,constants.blacklocation,turn), file)
              file.close()

          elif event.key == K_l:#next player turn
            if constants.edit == True:
              file = open('storedposition', 'rb')
              state,constants.whitelocation,constants.blacklocation,turn = pickle.load(file)
              file.close()
              draw(state)
          
          display_turn(turn,WIN,end)
          time.sleep(0.1)

          #edit mode controls
        
      elif event.type == MOUSEBUTTONDOWN: 
        if event.button==1:
          down=event.pos
          if down[0]<=constants.width and down[1]<=constants.height:
            x1 = down[0] * 8 // constants.width
            y1 = down[1] * 8 // constants.height
            if constants.edit == False:
              highlight_possible(down,state,possible,WIN)
          #print(possible)
            #  n=0
          #if n<20:
          # dark=game.highlight_possible(down,counter,possible,WIN)
        elif event.button == 3:
          if constants.edit == True:
            state = change_piece(event.pos,state,WIN)
      elif event.type == MOUSEBUTTONUP:
        if event.button == 1: # 1 == left button
        # if dark == True:
          dark=unhighlight_possible(state,WIN)
          up = event.pos
          #if up == down:
          # same=True
            #print("s1")
            #
          # n=0
          if up[0]<=constants.width and up[1]<=constants.height:
            if constants.edit == False: 
                turn,change,piece=move_piece(up,x1,y1,state,turn,possible,WIN,piece)
            else:
                change,piece = edit_mode(up,x1,y1,state,WIN)
            if change == True:
                bot_unhighlight(state,WIN)
                possible_found=False
                if constants.file==True:
                  pygame.mixer.Sound.play(constants.movesound)
                time.sleep(0.1)
            #WIN=draw(counter)
            #same=False
      
          
          
      pygame.display.update()
      
    clock.tick(60)
