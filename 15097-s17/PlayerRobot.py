from robot import Robot
from constants import Actions, TileType
import random
import time

##########################################################################
# One of your team members, Chris Hung, has made a starter bot for you.  #
# Unfortunately, he is busy on vacation so he is unable to aid you with  #
# the development of this bot.                                           #
#                                                                        #
# Make sure to read the README for the documentation he left you         #
#                                                                        #
# @authors: christoh, [TEAM_MEMBER_1], [TEAM_MEMBER_2], [TEAM_MEMBER_3]  #
# @version: 2/4/17                                                       #
#                                                                        #
# README - Introduction                                                  #
#                                                                        #
# Search the README with these titles to see the descriptions.           #
##########################################################################

# !!!!! Make your changes within here !!!!!
class player_robot(Robot):
    def __init__(self, args):
        super(self.__class__, self).__init__(args)
        ##############################################
        # A couple of variables - read what they do! # 
        #                                            #
        # README - My_Robot                          #
        ##############################################
        self.toHome = []             
        self.numturns = 0            
        self.goinghome = False;      
        self.targetPath = None
        self.targetDest = (0,0)
        self.state = 0 #0=searching, 1=have level, 2=going home
        self.levelNumber = 0
        self.pos = (0,0)
        self.incomplete = false

    # A couple of helper functions (Implemented at the bottom)
    def OppositeDir(self, direction):
        return # See below

    def ViewScan(self, view):
        return # See below

    def FindRandomPath(self, view):
        return # See below

    def UpdateTargetPath(self):
        return # See below

    ###########################################################################################
    # This function is called every iteration. This method receives the current robot's view  #
    # and returns a tuple of (move_action, marker_action).                                    #
    #                                                                                         #
    # README - Get_Move                                                                       #
    ###########################################################################################
   
    def containsRed(L):
        for marker in L:	
	    if Marker.GetColor() == RED:
                return True
        return False
   
    def containsGreen(L):
        for marker in L:
            if Marker.GetColor() == GREEN: 
                return True
        return False
   
    def containsYellow(L):
    	for marker in L:
	    if Marker.GetColor() == YELLOW: return False
	return False
 
    def boundary(self):
        n = self.levelNumber
        x,y = self.pos
        if (x > 0 and y > 0): return Actions.MOVE_W
        if (x < 0 and y < 0): return Actions.MOVE_E
        if (x > 0 and y < 0): return Actions.MOVE_N
        if (x < 0 and y > 0): return Actions.MOVE_S
    
    def goingHome(self,view):
    	dirToReverse = self.toHome[len(self.toHome)-1]
	finalDirection = oppositeDir(self,dirToReverse)
	x,y = self.pos
	markers = view[2][2][2]
	self.toHome[:-1]
	actions = Actions.DROP_NONE
	if y = self.levelNumber and containsRed(markers) :
		if !containsYellow(markers) and self.incomplete == True:
			actions = Actions.DROP_YELLOW
		elif containsYellow(markers) and self.incomplete == False:
			actions = Actions.DROP_GREEN
	return(finalDirection, actions)

    def containsBlue(L):
        for marker in L:
            if Marker.GetColor() == BLUE: 
                return True
        return False
    def containsYellow(L):
        for marker in L:
            if Marker.GetColor() == YELLOW: 
                return True
        return False
    def containsOrange(L):
        for marker in L:
            if Marker.GetColor() == ORANGE: 
                return True
        return False 


    def boundary(self):
        n = self.levelNumber
        x,y = self.pos
        if (x > -n and x <= n and y == n): return Actions.MOVE_W
        if (x >= -n and x < n and y == -n): return Actions.MOVE_E
        if (y >= -n and y < n and x == n): return Actions.MOVE_N
        if (y > -n and y <= n and x == -n): return Actions.MOVE_S

    def getKey(D, v):
    #the value should be in the D
    for key in D:
        if key[D] == v: return key

    def isM(x,y,view):
        return view[x][y][0] == Mountain
    def mountainDeal(direction, view):
        x,y = 2,2
        directions = {Actions.MOVE_E:(1,0), 
      		      Actions.MOVE_W:(-1,0),
		      Actions.MOVE_N:(0,-1),
		      Actions.MOVE_S:(0,1),
			Actions.MOVE_NW:(-1,-1),
			Actions.MOVE_NE:(1,-1),
			Actions.MOVE_SE:(1,1),
			Actions.MOVE_SW:(-1,1) }
  
        dx,dy = directions[direction]
        trynaX, trynaY = x+dx, y+dy
        if not isM(trynaX, trynaY, view): return (direction, None)
        
        
        
         


    def get_move(self, view):
        terrain = view[2][2][0]
        markers = view[2][2][2]

        if (self.state == 0):
            # want to go up, need to check for mountain, resource, w/e
            if not containsRed(markers):
                self.levelNumber = self.pos[x]
                (action, drops) = (mountainDeal(boundary(self), view), Actions.DROP_RED)
                self.toHome.append(action)
                updatePos(self, (action, drops))

                return (action, drops)
        elif (self.state == 1):
            if view[2][2][0] == resource:
                return(Actions.MINE, Actions.DROP_NONE)

            self.toHome.append(action)
            updatePos(self, (action, drops))

            return (action, drops)
        elif (self.state == 2):
            action = goHome(self, view)
            updatePos(self, action)
            return action
            
            

    def updatePos(self, (action, _)):
        if (action == Actions.MOVE_N):
            self.pos = (self.pos[0], self.pos[1]+1)
            return
        if (action == Actions.MOVE_NE):
            self.pos = (self.pos[0]+1, self.pos[1]+1)
            return
        if (action == Actions.MOVE_E):
            self.pos = (self.pos[0]+1, self.pos[1])
            return
        if (action == Actions.MOVE_SE):
            self.pos = (self.pos[0]+1, self.pos[1]-1)
            return
        if (action == Actions.MOVE_S):
            self.pos = (self.pos[0], self.pos[1]-1)
            return
        if (action == Actions.MOVE_SW):
            self.pos = (self.pos[0]-1, self.pos[1]-1)
            return
        if (action == Actions.MOVE_W):
            self.pos = (self.pos[0]-1, self.pos[1])
            return
        if (action == Actions.MOVE_NW):
            self.pos = (self.pos[0]-1, self.pos[1]+1)
            return
        else return




	


            
        
        '''

        # Returns home if you have one resource
        if (self.held_value() > 0):
            self.goinghome = True
        if(self.storage_remaining() == 0):
            self.goinghome = True

        # How to navigate back home
        if(self.goinghome):
            # You are t home
            if(self.toHome == []):
                self.goinghome = False
                return (Actions.DROPOFF, Actions.DROP_NONE)
            # Trace your steps back home
            prevAction = self.toHome.pop()
            revAction = self.OppositeDir(prevAction)
            assert(isinstance(revAction, int))
            return (revAction, Actions.DROP_NONE)

        viewLen = len(view)
        score = 0
        # Run BFS to find closest resource

        # Search for resources
        # Updates self.targetPath, sefl.targetDest
        self.ViewScan(view)
        
        # If you can't find any resources...go in a random direction!
        actionToTake = None
        if(self.targetPath == None):
            actionToTake = self.FindRandomPath(view)

        # Congrats! You have found a resource
        elif(self.targetPath == []):
            self.targetPath = None
            return (Actions.MINE, Actions.DROP_NONE)
        else:
            # Use the first coordinate on the path as the destination , and action to move
            actionToTake = self.UpdateTargetPath()
        self.toHome.append(actionToTake)
        #markerDrop = random.choice([Actions.DROP_RED,Actions.DROP_YELLOW,Actions.DROP_GREEN,Actions.DROP_BLUE,Actions.DROP_ORANGE])
        markerDrop = Actions.DROP_NONE
        assert(isinstance(actionToTake, int))
        return (actionToTake, markerDrop)
        '''

    # Returns opposite direction
    def OppositeDir(self, prevAction):
        if(prevAction == Actions.MOVE_N):
            return Actions.MOVE_S
        elif(prevAction == Actions.MOVE_NE):
            return Actions.MOVE_SW
        elif(prevAction == Actions.MOVE_E):
            return Actions.MOVE_W
        elif(prevAction == Actions.MOVE_SE):
            return Actions.MOVE_NW
        elif(prevAction == Actions.MOVE_S):
            return Actions.MOVE_N
        elif(prevAction == Actions.MOVE_SW):
            return Actions.MOVE_NE
        elif(prevAction == Actions.MOVE_W):
            return Actions.MOVE_E
        elif(prevAction == Actions.MOVE_NW):
            return Actions.MOVE_SE
        else:
            return Actions.MOVE_S

    # Scans the entire view for resource searching
    # REQUIRES: view (see call location)
    def ViewScan(self, view):
        viewLen = len(view)
        queue = [[(0,0)]]
        deltas = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        visited = set()
        visited.add((0,0))

        targetDepleted = (view[self.targetDest[0]][self.targetDest[1]][0].GetType() == TileType.Resource and
                         view[self.targetDest[0]][self.targetDest[1]][0].AmountRemaining() <= 0)

        # BFS TO find the next resource within your view
        if(self.targetPath == None or targetDepleted):
            while(len(queue)>0):
                path = queue[0]
                loc = path[0]
                queue = queue[1:]
                viewIndex = (loc[0] + viewLen//2,loc[1]+viewLen//2)
                if (view[viewIndex[0]][viewIndex[1]][0].GetType() == TileType.Resource and
                    view[viewIndex[0]][viewIndex[1]][0].AmountRemaining() > 0):
                    # print(path)
                    self.targetPath = path[1:]
                    self.targetDest = path[0]
                    return
                elif(view[viewIndex[0]][viewIndex[1]][0].CanMove()):
                    for i in range(8):
                        x = loc[0] + deltas[i][0]
                        y = loc[1] + deltas[i][1]
                        if(abs(x) <= viewLen//2 and abs(y) <= viewLen//2):
                            if((x,y) not in visited):
                                queue.append([(x,y)] + path[1:] + [deltas[i]])
                                visited.add((x,y))

        return

    # Picks a random move based on the view - don't crash into mountains!
    # REQUIRES: view (see call location)
    def FindRandomPath(self, view):
        viewLen = len(view)

        while(True):
            actionToTake = random.choice([Actions.MOVE_E,Actions.MOVE_N,
                                          Actions.MOVE_S,Actions.MOVE_W,
                                          Actions.MOVE_NW,Actions.MOVE_NE,
                                          Actions.MOVE_SW,Actions.MOVE_SE])
            if ((actionToTake == Actions.MOVE_N and view[viewLen//2-1][viewLen//2][0].CanMove()) or
               (actionToTake == Actions.MOVE_S and view[viewLen//2+1][viewLen//2][0].CanMove()) or
               (actionToTake == Actions.MOVE_E and view[viewLen//2][viewLen//2+1][0].CanMove()) or
               (actionToTake == Actions.MOVE_W and view[viewLen//2][viewLen//2-1][0].CanMove()) or
               (actionToTake == Actions.MOVE_NW and view[viewLen//2-1][viewLen//2-1][0].CanMove()) or
               (actionToTake == Actions.MOVE_NE and view[viewLen//2-1][viewLen//2+1][0].CanMove()) or
               (actionToTake == Actions.MOVE_SW and view[viewLen//2+1][viewLen//2-1][0].CanMove()) or
               (actionToTake == Actions.MOVE_SE and view[viewLen//2+1][viewLen//2+1][0].CanMove()) ):
               return actionToTake

        return None

    # Returns actionToTake
    # REQUIRES: self.targetPath != []
    def UpdateTargetPath(self):
        actionToTake = None
        (x, y) = self.targetPath[0]

        if(self.targetPath[0] == (1,0)):
            actionToTake = Actions.MOVE_S
        elif(self.targetPath[0] == (1,1)):
            actionToTake = Actions.MOVE_SE
        elif(self.targetPath[0] == (0,1)):
            actionToTake = Actions.MOVE_E
        elif(self.targetPath[0] == (-1,1)):
            actionToTake = Actions.MOVE_NE
        elif(self.targetPath[0] == (-1,0)):
            actionToTake = Actions.MOVE_N
        elif(self.targetPath[0] == (-1,-1)):
            actionToTake = Actions.MOVE_NW
        elif(self.targetPath[0] == (0,-1)):
            actionToTake = Actions.MOVE_W
        elif(self.targetPath[0] == (1,-1)):
            actionToTake = Actions.MOVE_SW

        # Update destination using path
        self.targetDest = (self.targetDest[0]-x, self.targetDest[1]-y)
        # We will continue along our path    
        self.targetPath = self.targetPath[1:]

        return actionToTake

