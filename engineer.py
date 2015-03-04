import random

class engineer:
    
    # engineers are spawned with a number of tasks
    # they run models which will tell them what direction to head
    # their models are dependent on other users progress
    # if another user is generating bad information but is unaware of it, design will take longer to close
    # tasks have varying levels of priority
    # impact of bad decision on low priority task is small
    # each task has an associated model
    
    
    
    def __init__(self,ID,numTasks,skill):
        self.ID = ID
        self.numTasks = numTasks
        self.skill = skill
        taskList = []
        initTasks()
        
    def initTasks(self):
        
        
        #  def __init__(self,difficulty,initialValue,dependenceList,nullZone,nominalDays):
        
        for i in range(0,numTasks):
            difficulty = random.randrange(1,10)
            intialValue = 0
            nullZone = .01
            nominalDays = int(random.uniform*90)
            dependenceList = []
            self.taskList.append(task(difficulty,intialValue,dependenceList,nullZone,nominalDays))
        
    def work(self,timeStep):
        a = 1

    