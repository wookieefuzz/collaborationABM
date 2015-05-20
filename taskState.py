class taskState:
    
    def __init__(self):
        self.complete = False
        self.trueState = 0.0
        self.pureState = 0.0
        self.goal = 1.0
        self.perceivedGoal = .75
        self.perceivedGoalTmp = .75
        self.perceivedState = 0.0
        self.communicatedState = 0.0
        self.dependMod = 0.0
        self.pDependMod = 0.0
        
    def setPerceivedGoal(self,g):
        self.perceivedGoal = g
    
    def setComplete(self):
        self.complete = True
        
    def setTrueState(self,val):
        self.trueState = val
        
    def setPerceivedState(self,val):
        self.perceivedState = val
        
    def setCommunicatedState(self,val):
        self.communicatedState = val
        
   
    def updateState(self,work,depMod):
        self.pureState += work # pure state is always incremented and is untouched by anything else 
        self.trueState = self.pureState - depMod # true state is affected by dependence modifier
    
    
    def printInfo(self):
        print 'Complete = ' + str(self.complete) +'\n'
        print 'True State = ' + str(self.trueState) +'\n' 
        print 'Pure State = ' + str(self.pureState) +'\n'
        print 'Perceived Goal = ' + str(self.perceivedGoal) +'\n'
        print 'Perceived Goal (tmp)= ' + str(self.perceivedGoalTmp) +'\n'
        print 'Perceived State = ' + str(self.perceivedState) +'\n'
        print 'Communicated State = ' + str(self.communicatedState) +'\n'  
        print 'True Dependence Modifier = ' + str(self.dependMod) +'\n'  
        print 'Perceived Dependence Modifier = ' + str(self.pDependMod) +'\n'
        