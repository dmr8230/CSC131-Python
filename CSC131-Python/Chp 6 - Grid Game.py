#==========================================================================
# PROGRAM PURPOSE:... Ch6-1 Modified Ch6 M2/3
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... I looked up the random.choice(colors) through stack overflow
# WORK TIME(h:mm):... 12:30
#==========================================================================

import turtle as t 
import random
import time 

t.setup(800,600)


# need print statements explaining the rules of the game 
def create_box():
    boardwid = -200
    boardheight = -200
    nbr_of_lines = 0
    t.speed("normal")
    #for length in range(0, 35):
    while nbr_of_lines < 11:
        
        while boardwid < 200: 
            t.penup()
            t.setposition(boardwid, boardheight)
            boardwid += 200
            t.pendown()
            t.setposition(boardwid,boardheight)
            t.penup()
        
        boardheight += 40
        nbr_of_lines += 1
        boardwid = -200

    nbr_of_lines = 0
    boardheight = -200
    boardwid = -200
    while nbr_of_lines < 11:
        
        while boardheight < 200: 
            t.penup()
            t.setposition(boardwid, boardheight)
            boardheight += 200
            t.pendown()
            t.setposition(boardwid,boardheight)
            t.penup()
        
        boardwid += 40
        nbr_of_lines += 1
        boardheight = -200

    t.penup() 
    
        
           


create_box()

terminate = False
#while not terminate: 
def create_players(): 
# create players/wormholes
    # create variable with input to determine the amount of players
    numplayers = int(input("Enter 4-10 the number of players you want to have "))
    while(numplayers < 4 or numplayers >10):
        numplayers = int(input("Please, a number from 4-10 "))
    numholes = int(input("Enter a number from 0-5 of black holes (death spots) "))
    while(numholes < 0 or numholes >5):
        numholes = int(input("Please, a number from 1-5 of black holes (death spots) "))
    guesses = (int(input("Guess how many players will remain after 100 turns ")))
    #create the four players and their positions - need a loop to assign players
    playercreate = []
    holecreate = [] 
    playerdir = [0, 90, 180, 270]
    playerstart = [-160, -120, -80, -40, 0, 40, 80, 120, 160]
    colorchoices = ('black', 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'aqua', 'violet', 'darksalmon', 'teal','indigo','c') 
    for k in range(0,numplayers):
        newplayer = t.Turtle()
        newplayer.penup()
        newplayer.shape('turtle')
        cc = colorchoices[k]
        newplayer.fillcolor(cc)
        newplayer.speed(0)
        newplayer.setheading(playerdir[random.randint(0,3)])
        start1 = playerstart[random.randint(0,8)]
        start2 = playerstart[random.randint(0,8)]
        newplayer.setpos(start1, start2)
        newplayer.pendown()
        newplayer.pencolor(cc)
        #playerstart.remove(start1) -- something like this so colors are different
        #playerstart.remove(start2) 
        playercreate.append(newplayer)

    t.speed(0)

    #creation of black holes
    
##    
    for l in range (0, numholes):
        newhole = t.Turtle()
        newhole.penup()
        newhole.shape('circle')
        newhole.fillcolor('black')
        bhstart1 = playerstart[random.randint(0,8)]
        bhstart2 = playerstart[random.randint(0,8)]
        newhole.setpos(bhstart1,bhstart2)
        holecreate.append(newhole)
        

##        newhole = t.Turtle()
##        newhole.penup()
##        newhole.shape('circle')
##        newhole.fillcolor('black')
##        bhstart1 = playerstart[0]
##        bhstart2 = playerstart[0]
##        newhole.setpos(0,0)
    

    #for m in range(0, len(holecreate)):
        
        #print(holecreate[m].pos())
    # a variable to determines direction
        #then push forward 40
    cnt = 0 
    while len(playercreate) > 0 and cnt < 100: 
    

                    
        for k in range(0,len(playercreate)):
            t.tracer(0,0)
            playercreate[k].forward(40)
            if playercreate[k].xcor() <= -160:
                playercreate[k].setx(0)
##                    if playercreate[k].xcor() == 0 and playercreate[k].ycor() == 0:
##                        print(colorchoices[k], "color wins!!!") 
##                        terminate = True 
                for m in range(0, len(holecreate)): 
                    if playercreate[k].pos() >= holecreate[m].pos():
                        playercreate[k].hideturtle()
                        #del playercreate[k]
                        if len(playercreate) == 1:
                            print(colorchoices[k], "color wins!!!")
                            terminate = True
                            break
                        
            elif playercreate[k].xcor() >= 160:
                playercreate[k].setx(0)
##                    if playercreate[k].xcor() == 0 and playercreate[k].ycor() == 0:
##                        print(colorchoices[k], "color wins!!!")
##                        terminate = True 
                for m in range(0, len(holecreate)): 
                    if playercreate[k].pos() >= holecreate[m].pos():
                        playercreate[k].ht()
                        #del playercreate[k]
                        if len(playercreate) == 1:
                            print(colorchoices[k], "color wins!!!")
                            terminate = True
                            break
                        
            elif playercreate[k].ycor() <= -160:
                playercreate[k].sety(0)
##                    if playercreate[k].xcor() == 0 and playercreate[k].ycor() == 0:
##                        print(colorchoices[k], "color wins!!!") 
##                        terminate = True 
                for m in range(0, len(holecreate)): 
                    if playercreate[k].pos() >= holecreate[m].pos():
                        #del playercreate[k]
                        playercreate[k].ht()
                        if len(playercreate) == 1:
                            print(colorchoices[k], "color wins!!!")
                            terminate = True
                            break
                        
            elif playercreate[k].ycor() >= 160:
                playercreate[k].sety(0)
##                    if playercreate[k].xcor() == 0 and playercreate[k].ycor() == 0:
##                        print(colorchoices[k], "color wins!!!") 
##                        terminate = True 
                for m in range(0, len(holecreate)): 
                    if playercreate[k].pos() >= holecreate[m].pos():
                        playercreate[k].ht()
                        #del playercreate[k]
                        if len(playercreate) == 1:
                            print(colorchoices[k], "color wins!!!")
                            terminate = True
                            break

            #for m in range(0, len(holecreate)): 
                #if playercreate[k].pos() == holecreate[m].pos():
                  #  print("hi")
                    #playercreate.remove(k)
                    #del playercreate[k]

                    #playercreate[k].clear()
                    #t.exitonclick()

            #print(holecreate.pos())
            cnt += 1 
            t.update()
            playercreate[k].setheading(playerdir[random.randint(0,3)])

            

            #if 
            
        numseconds = 10
        start_time= time.time()
        if time.time() - start_time > numseconds:
            break 
     
        
#algorithm 

    # an if statement afterwards so if two are in the same spot
        #add another random wormhole 


#def createwormholes():
    #something 
    
    
            #newplayer.fillcolor('
                #if condition to ensure colors are not the same
                #have the user input their color - give a choice of 10
            #newplayer.speed(0)
            #create a way to input the position first position of the ball
                #this requires user input
                # if statement to ensure that positions of the balls are not the same
        #at the end of this function you should return ball and pass that through the other functions
    #create wormholes
        #for k2 in range(0,numplayers):
            #create wormhole
                # wormhole = t.Turtle()
                # wormhole = shape('circle')
                # wormhole = fillcolor('black')
                # location is user input - input right after they put in their location
                    # if statement to ensure that wormholes are not in the same location as users
            #if player position == wormhole position player is eliminated

# wormhole creater -- possibility 
    #create wormhole with random coordinates 
    #if player hits the wormhole reprompt the create wormhole

# random place generator for each of the players
    # for each of the players use random to determine if they move up,down,left, right
        #the number of spots moved should always be the distance between each grid spot
        #if they go off the gril then switch from negative to positive
    #pen down so that each one may have a trail
    # if a player hits a trail or another player then delete that player

# when one player is left alive then .exit() and show that player as the winner
    #display winner by saying player 'color' is the winner 
    
                
create_players()


#playerdirect() 


    
