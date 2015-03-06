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
       
        self.IDlist = []
        self.errorList = []
        self.influenceList = []
        self.scaleFactor = 0
       
        # dependence list supplies the number of inputs needed for the task/model
        # model won't converge until all dependence variables are converged
        # harder problems should maybe have more dependence variables?
        # dependenceList is a list of the ID's needed for updating the model
        
    def work(self,userSkill,avgWork,stdDev):
        
        if(self.currentValue < self.goal):
            self.state = 'incomplete'
        
        # get the colleague modifier
        colleagueModifier = self.getColleagueModifier()
        
        tempGoal = self.goal + colleagueModifier
        
        # if you aren't with tol of your goal, do work 
        if (self.state == 'incomplete'):
             skillModifier = userSkill / self.difficulty
             dailyWork = random.gauss(avgWork,stdDev)/self.nominalDays # amount of work user will accomplish this day (random variable)
             self.currentValue = self.currentValue + dailyWork
        
        if(self.currentValue > self.goal):
            self.state = 'complete'
        
        
        
            
    def doWork(self,userSkill,avgWork,stdDev):
        
        # if the current value is within a tolerance of the goal, don't do any work, otherwise: work
        if (abs(self.currentValue - self.goal)>self.nullZone):
            skillModifier = userSkill / self.difficulty # ratio increases as user skill outstrips difficulty
            rv = random.gauss(skillModifier * avgWork * self.maxWork,stdDev*self.maxWork); 
            colleagueModifier = self.getColleagueModifier()
            #managementModifier = self.getManagementModifer()
            self.currentValue = self.currentValue + rv #+ colleagueModifier + managementModifier
        return self.currentValue
   
    def runModel(self,contributedInformation):
        # run the model
        return void
        
        
    def improveModel(self):
        # model can only be improved if task is approaching DONE state
        # or if help is received
        
        return void
    
    def getColleagueModifier(self):
        # loop through collaborators
        i = -1
        colleagueModifier = 0.0
        for e in self.errorList:
            i = i + 1
            print i 
            colleagueModifier = colleagueModifier + (e * self.influenceList[i] * self.scaleFactor)
        return colleagueModifier
    
    def getManagementModifer(self):
        return 0.0
    
    def updateErrorList(self,IDlist,errorList,influenceList,scaleFactor):
        self.IDlist = IDlist
        self.errorList = errorList
        self.influenceList = influenceList
        self.scaleFactor = scaleFactor
    
    def printInfo(self):
        print 'Task ID is ' + str(self.ID)
        print 'Difficulty level is ' + str(self.difficulty)
        print 'Task should nominally take ' + str(self.nominalDays) + ' days'
        percentGoalError = int((1 - self.goal)*100.0)
        print 'Current Design goal error is ' +str(percentGoalError) + '%'
        percentComplete = int((self.currentValue / self.goal)*100.0)
        print 'Current progress towards goal is ' +str(percentComplete)+ '%'
    
    def updateModel(self,contributor,newValue):
        index = dependenceList.index(contributor);
        self.contributedInformation[index] = newValue        
        return void