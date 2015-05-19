import random

class task:
    
    def __init__(self,difficulty,initialValue,nullZone,nominalDays,ID):
        self.ID = ID
        # nominal days to accomplish task
        self.nominalDays = nominalDays
        self.goal = .75
        # cap on maximum allowable work per day
        self.maxWork = 1.0 / (0.9 * float(nominalDays))
        self.state = 'incomplete'
        self.difficulty = difficulty
        self.initialValue = initialValue
        self.currentValue = initialValue
        self.nullZone = nullZone
        self.daysWorked = 0
        self.error = self.goal - 1.0 # this is the actual error
        self.publicError = 1.0 # this is the error shared with others
       
        self.IDlist = []
        self.errorList = []
        self.influenceList = []
        self.scaleFactor = 0
       
        # dependence list supplies the number of inputs needed for the task/model
        # model won't converge until all dependence variables are converged
        # harder problems should maybe have more dependence variables?
        # dependenceList is a list of the ID's needed for updating the model
        
    def work(self,userSkill,avgWork,stdDev):
        
        colleagueModifier = self.getColleagueModifier()
        managementModifier = self.getManagementModifer()
        
        self.error = (self.goal + colleagueModifier)- 1.0 # error is due to self goal and colleagues
        
        self.improveModel(userSkill)
        
        # you've finished if you reach your goal, modified by colleagues and management
        if(self.currentValue < (self.goal +colleagueModifier + managementModifier)): 
            self.state = 'incomplete'
            
        # if you aren't with tol of your goal, do work 
        if (self.state == 'incomplete'):
             self.daysWorked = self.daysWorked + 1
             skillModifier = userSkill / self.difficulty
             dailyWork = random.gauss(avgWork,stdDev)/self.nominalDays # amount of work user will accomplish this day (random variable)
             self.currentValue = self.currentValue + dailyWork
        
        if(self.currentValue > self.goal + managementModifier + colleagueModifier):
            self.state = 'complete'
        
        
        
        
    def runModel(self,contributedInformation):
        # run the model
        return void
        
        
    def improveModel(self,userSkill):
        skillModifier = userSkill / self.difficulty # this can range from .1 to 10
        # max improvement is a function of this, max improvement should be (.25 / nominal days) so someone improving at the max rate each day gets a perfect design
        maxImprovement = .25 / (10.0*self.nominalDays)
        improvement = maxImprovement * skillModifier
        # probability of improving model approaches 100% as time progresses
        rv = random.random()
        improvementThreshold = .5 - 0.4*(float(self.daysWorked) / float(self.nominalDays))
        if rv>improvementThreshold:
            self.goal = self.goal + improvement
        
        if self.goal > 1.0:
            self.goal = 1.0
            
        return 0.0
    
    def getColleagueModifier(self):
        
        colleagueModifier = 0.0
        
        # loop through collaborators
        numDepends = len(self.errorList)
        
        if numDepends==1:
            err = self.errorList[0]
#             print err
            influence = self.influenceList[0]
#             print influence
#             print self.scaleFactor
            colleagueModifier = (err * influence * self.scaleFactor)
        elif numDepends > 1:
            i = -1
            for e in self.errorList:
                i = i + 1
                print i 
                colleagueModifier = colleagueModifier + (e * self.influenceList[i] * self.scaleFactor)
            
        return colleagueModifier
        
    def getManagementModifer(self):
        return 0.0
    
    def getManagementInput(self,error,force):
        return 0.0
    
    def updateErrorList(self,IDlist,errorList,influenceList,scaleFactor):
        self.IDlist = IDlist
        self.errorList = errorList
        self.influenceList = influenceList
        self.scaleFactor = scaleFactor
    
    def updateModel(self,contributor,newValue):
        index = dependenceList.index(contributor);
        self.contributedInformation[index] = newValue        
        return void
    
    
    
    def printInfo(self):
        print 'Task ID is ' + str(self.ID)
        print 'Difficulty level is ' + str(self.difficulty)
        print 'Task should nominally take ' + str(self.nominalDays) + ' days'
        percentGoalError = int((1 - self.goal)*100.0)
        print 'Current Design goal error is ' +str(percentGoalError) + '%'
        print 'Current design goal is ' + str(self.goal)
        percentComplete = int((self.currentValue / self.goal)*100.0)
        print 'Current progress towards goal is ' +str(percentComplete)+ '%'
        print 'Current days worked are: ' + str(self.daysWorked)