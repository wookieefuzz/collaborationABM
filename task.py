import random

class task:
    
    def __init__(self,difficulty,initialValue,nullZone,nominalDays):
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
       
        # dependence list supplies the number of inputs needed for the task/model
        # model won't converge until all dependence variables are converged
        # harder problems should maybe have more dependence variables?
        # dependenceList is a list of the ID's needed for updating the model
        
        
    
    
    def work(self,userSkill,avgWork,stdDev):
        
        # if you aren't with tol of your goal, do work 
        if (abs(self.currentValue - self.goal)>self.nullZone):
             skillModifier = userSkill / self.difficulty
             dailyWork = random.gauss(avgWork,stDev) # amount of work user will accomplish this day (random variable)
             colleagueModifier = self.getColleagueModifier()
        
        
        
        return 0.0
        
        
        
        
        
        
        
        
        
        
        
        
    def doWork(self,userSkill,avgWork,stdDev):
        
        # if the current value is within a tolerance of the goal, don't do any work, otherwise: work
        if (abs(self.currentValue - self.goal)>self.nullZone):
            skillModifier = userSkill / self.difficulty # ratio increases as user skill outstrips difficulty
            rv = random.gauss(skillModifier * avgWork * self.maxWork,stdDev*self.maxWork); 
            #colleagueModifier = self.getColleagueModifier()
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
    
    def getColleagueModifier(self,IDlist,errorList,influenceList,scaleFactor):
        # loop through collaborators
        i = -1
        colleagueModifier = 0.0
        for e in errorList:
            i = i + 1
            print i 
            colleagueModifier = colleagueModifier + (e * influenceList[i] * scaleFactor)
        return colleagueModifier
    
    def getManagementModifer(self):
        return 0.0
    
    def updateModel(self,contributor,newValue):
        index = dependenceList.index(contributor);
        self.contributedInformation[index] = newValue        
        return void