# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

class MyAI ( Agent ):

    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self.aList = [ ]        
   
        self.ourMap = [['@', '.', '.', ',' ],
                        ['.', '.', '.', '.' ],
                        ['.', '.', '.', '.' ],
                        ['.', ',', ',', ',' ]]


        self.maxWidth = 0
        self.maxHeight = 0

        self.curPos = [0, 0]
        self.curDir = RIGHT
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        if breeze and not self.aList:
            return Agent.Action.CLIMB

        


        #return Agent.Action.CLIMB
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

    def updateMap(self, stench, breeze, glitter, bump, scream) -> None:
        ''' Updates the contents of the current cell. '''
        
        if not bump and self.curDir == RIGHT:
            self.checkHorBounds()
        if not bump and self.curDir == UP:
            self.checkVerBounds()
       

        self.checkPercepts(stench, breeze, glitter, bump, scream)
        

    

    def checkHorBounds(self) -> None:
        ''' Appends a list if we move towards the RIGHT '''
        x, y = self.curPos
        pass

    def checkVerBounds(self) -> None:
        x, y = self.curPos
        pass
        

    def checkPercepts(self, stench, breeze, glitter, bump, scream) -> None: 
        x, y = self.curPos
        if stench:
            self.ourMap[x][y].append('S')
        elif breeze:
            self.ourMap[x][y].append('B')
        elif glitter:
            self.ourMap[x][y].append('G')
        elif bump:
            if self.curDir == RIGHT:
                self.maxWidth = len(self.ourMap)
            if self.curDir == UP:
                self.maxHeight = len(self.ourMap[x])
        
        return


    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
