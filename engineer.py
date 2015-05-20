import random
from task import task

class engineer:
    
    # engineers are spawned with a number of tasks
    # they run models which will tell them what direction to head
    # their models are dependent on other user's progress
    # if another user is generating bad information but is unaware of it, design will take longer to close
    # tasks have varying levels of priority
    # impact of bad decision on low priority task is small
    # each task has an associated model
    
    # when working, these are tasks:
    # do work
    
    # check to see if you should update your data you are presenting to other people
    
    # if time to share information with other people
    # perturb function is dependent on skill modifier, current error, and time spent on project
    
    
    
    def __init__(self,ID,numTasks,skill):
        self.taskCounter = 0
        self.ID = ID
        self.numTasks = numTasks
        self.skill = skill
        self.taskList = []
        self.initTasks()
        #self.initTestTasks()
        self.avgWork = .8
        self.stdDev = 0.1
        self.listening = 0.0
        self.commAccuracy = 0.0
        self.freq = 0.0
        self.freqStdDev = 0.0
        
        
    def setListening(self,listening):
        self.listening = listening
        
    def setCommAccuracy(self,commAccuray):
        self.commAccuracy = commAccuray
        
    def setFrequency(self,freq,stdDev):
        self.freq = freq
        self.freqStdDev = stdDev
        
    def initTasks(self):
        
        #  def __init__(self,difficulty,initialValue,dependenceList,nullZone,nominalDays):
        
        for i in range(0,self.numTasks):
            self.taskCounter = self.taskCounter + 1
            difficulty = float(random.randrange(1,10))
            intialValue = 0
            nullZone = .01
            nominalDays = random.randrange(5,90)
            taskIDstring = str(self.ID) + '-' + str(self.taskCounter)
            self.taskList.append(task(difficulty,intialValue,nullZone,nominalDays,taskIDstring))
            
    def initTestTasks(self):
        
        #  def __init__(self,difficulty,initialValue,dependenceList,nullZone,nominalDays):
        
        for i in range(0,self.numTasks):
            self.taskCounter = self.taskCounter + 1
            difficulty = 5.0
            intialValue = 0
            nullZone = .01
            nominalDays = 90
            taskIDstring = str(self.ID) + '-' + str(self.taskCounter)
            self.taskList.append(task(difficulty,intialValue,nullZone,nominalDays,taskIDstring))

    def work(self):
        for task in self.taskList:
            task.work(self.skill,self.avgWork,self.stdDev) 
        
    def printTaskInfo(self):
        for task in self.taskList:
            task.printInfo()
        
    def communicate(self):
        print 'fill this in'
        
    
    def getFeedback(self,taskIndex,error,force):
        rv = random.random()
        listeningThreshold = .5 - (.4 * self.listening)
        
        # if user is good at listening, take the advice
        if rv>listeningThreshold:
            self.taskList[taskIndex].getManagementInput(error,force)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        