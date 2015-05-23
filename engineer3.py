from task3 import task3
import random

class engineer3:
    
    def __init__(self,ID,skill,cat):
        
        # Skills, ID, etc
        self.ID = ID
        self.skill = skill
        self.category = cat
        self.listening = 1.0
        self.communication = 1.0
        self.timeliness = 1.0
        self.avgWork = 0.8
        self.stdDev = 0.2
        
        
        # own task list
        self.taskList = []
        
        
        
    def setAvgWork(self,aw):
        self.avgWork = aw
        
    def setStdDev(self,sd):
        self.stdDev = sd
    
    def addTask(self,t):
        self.taskList.append(t)
        
    def setListening(self,l):
        self.listening = l
        
    def setCommunication(self,c):
        self.communication = c
        
    def setTimeliness(self,t):
        
        self.timeliness = t
        
    def setSkill(self,s):
        self.skill = s
        
    def setCategory(self,c):
        self.category = c
        
    def setID(self,ID):
        self.ID = ID
         
    def printTaskInfo(self):
        for t in self.taskList:
            t.printInfo()
    
    
    
    def work(self):
        
        # get the amount to be worked on each task (a fancy RV with some logic)
        effortAmount = self.effortAmnt() 
       
        i = -1
        for t in self.taskList:
            i += 1
            
            t.calcPerceivedState(self.avgWork,self.stdDev,effortAmount[i],self.timeliness)
            t.calcTrueState()
            
           
    def receiveFeedback(self,errList,goalList):
        
        i = -1
        for t in self.taskList:
            i += 1
            rv = random.random()
            if rv<self.listening:
                t.updateManagementModifier(errList[i],goalList[i])
    
    
    
    
    
    def improveModel(self,task,skillMod,effort):
        # max improvement is a function of this, max improvement should be (.25 / nominal days) so someone improving at the max rate each day gets a perfect design
            maxImprovement = effort * (.25 / (10.0*task.nominalDays))
            improvement = maxImprovement * skillMod
            # probability of improving model approaches 100% as time progresses
            rv = random.random()
            improvementThreshold = .5 - 0.4*(float(task.daysWorked) / float(task.nominalDays))
            if rv>improvementThreshold:
                if task.gainedKnowledge<.25:
                    task.gainedKnowledge += improvement
                    task.perceivedGoal += improvement
            
           
                
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def effortAmnt(self):
        
        effortList = []
        
        numTasks = len(self.taskList)
        
        stillWorking = False
        for t in self.taskList:
            if t.complete == False:
                stillWorking = True
        
        if stillWorking == True:    
            # add up all the priorities, this will let us know how much to work on each task
            prioritySum = 0.0
            for t in self.taskList:
                if t.complete == False:
                    prioritySum = prioritySum + t.priority
                
            # now do the work    
            # start off by finding the skill modifier
            # this is hampered by 50% if work is not in user's wheelhouse
            # if user skill far outstrips difficulty, this 50% becomes less of an issue
            
            n = -1
            
            for t in self.taskList:
                
                n += 1
                
                if self.category == t.category:
                    skillModifier = self.skill/t.difficulty
                else:
                    skillModifier = 0.5 * self.skill/t.difficulty
                
                # calculate the effort for each task (2 equal priority tasks will get 50% effort each)
                effort = t.priority / prioritySum
                
                # improve task's PERCEIVED GOAL by some amount
                self.improveModel(t,skillModifier,effort)
            
                # do work on the task
                # perceived state will increase
                # ACTUAL state will still be affected by dependence
                
                
                effortList.append(effort)
        else:
            for t in self.taskList:
                effortList.append(0.0)
                    
        return effortList
           
           
        
        def getDependenceModifier(self,taskNum):
            for s in self.dependentTaskState:
                i = self.dependenceList.index(s)
                impactedTask = self.taskList[self.dependenceList[i]]
                realError = 1.0 - s.trueState
                communicatedError = 1.0 - s.perceivedState
                
        
        
        