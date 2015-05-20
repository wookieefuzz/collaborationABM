from taskState import taskState
from task2 import task2
import random

class engineer2:
    
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
        
        # list of ID's of other tasks, as well as their states
        self.dependenceList = []
        self.dependenceScale = []
        self.dependentTaskList = []
        
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
        
    def addDependentTask(self,tID,scale,task):
        self.dependenceList.append(tID)
        self.dependenceScale.append(scale)
        self.dependentTaskList.append(task)
    
    
    
    def printTaskInfo(self):
        for t in self.taskList:
            t.printInfo()
    
    
    
    def work(self):
        
        # get the amount to be worked on each task (a fancy RV with some logic)
        workAmount = self.workAmnt() 
        
        i = -1
        for t in self.taskList:
            
            trueDependMod = 0.0
            perceivedDependMod = 0.0
            
            i += 1
            
            n = -1
            for tt in self.dependentTaskList:
                s = tt.state
                n += 1
               
                if (self.dependenceList[n] == i):
                    depMod = (s.trueState - 1.0) # true dependence modification is the true error times the scale factor
                    #print 'depMod = ' + str(depMod)
                    trueDependMod += self.dependenceScale[n] * depMod # increment
                    #print 'true dependence modifier = ' + str(trueDependMod)
                    depMod2 = (s.perceivedGoal - s.communicatedState ) # perceived dependence modification is the perceived error times the scale factor
                    #print 'depMod2 = ' + str(depMod2)
                    perceivedDependMod += self.dependenceScale[n] * depMod2 # increment
                    #print 'perceived dependence modifier = ' + str(perceivedDependMod)
            
            # now that all modifiers are out there... check your perceived goal
         
                
                
            
            perceivedGoalTmp = t.state.perceivedGoal + perceivedDependMod
            #print 'temp perceived goal is ' + str(perceivedGoalTmp)        
            t.state.perceivedGoalTmp = perceivedGoalTmp
            if (t.state.perceivedState > perceivedGoalTmp) & (t.state.complete == False):
                t.state.complete = True
            else:
                t.state.dependMod = trueDependMod
                t.state.pDependMod = perceivedDependMod
                t.state.pureState += workAmount[i]
                t.state.perceivedState += workAmount[i] 
                t.state.trueState = t.state.pureState + trueDependMod
                #if trueDependMod<0:
                    #print 'true state = ' + str(t.state.trueState)
                t.daysWorked += 1
                
            rv = random.random()
            
            if (rv<self.timeliness):
               
                t.state.communicatedState = t.state.perceivedState - perceivedDependMod
    
    
    
    
    
    
    def improveModel(self,task,skillMod,effort):
        # max improvement is a function of this, max improvement should be (.25 / nominal days) so someone improving at the max rate each day gets a perfect design
            maxImprovement = effort * (.25 / (10.0*task.nominalDays))
            improvement = maxImprovement * skillMod
            # probability of improving model approaches 100% as time progresses
            rv = random.random()
            improvementThreshold = .5 - 0.4*(float(task.daysWorked) / float(task.nominalDays))
            if rv>improvementThreshold:
                task.state.perceivedGoal += improvement
            
            if  task.state.perceivedGoal  > 1.0:
                 task.state.perceivedGoal = 1.0
                
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def workAmnt(self):
        
        workList = []
        
        numTasks = len(self.taskList)
        
        # add up all the priorities, this will let us know how much to work on each task
        prioritySum = 0.0
        for t in self.taskList:
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
            
            dailyWork = effort * random.gauss(self.avgWork,self.stdDev)/t.nominalDays # amount of work user will accomplish this day (random variable)
           
            workList.append(dailyWork)
           
        return workList
           
           
        
        def getDependenceModifier(self,taskNum):
            for s in self.dependentTaskState:
                i = self.dependenceList.index(s)
                impactedTask = self.taskList[self.dependenceList[i]]
                realError = 1.0 - s.trueState
                communicatedError = 1.0 - s.perceivedState
                
        
        
        