import random

class task3:
    
    def __init__(self,diff,cat,prio,days,name):
        self.name = name
        
        self.nullZone = .02
        self.impThreshold = .001
        self.noMoreImprovement = False
        self.improvementHistory = [0]*30
        
        self.managementModifier = 0.0
        self.managementDeemsComplete = False
        self.managementState = 'Stale'
        
        self.difficulty = diff
        self.category = cat
        
        self.priority = prio
        self.nominalDays = days
        self.daysWorked = 0.0
        self.workAmount = 0.0
        self.dependsOnTasks = []
        self.impactAmnt = []
        
        self.trueState = 0.0
        self.trueGoal = 1.0
        self.perceivedState = 0.0
        self.perceivedGoal = .75
        self.communicatedGoal = 1.0
        self.communicatedState = 0.0
        self.presentedState = 0.0
        
        self.complete = False
        self.gainedKnowledge = 0.0
        
        
    
    def updateSharedInfo(self):
        self.presentedState = self.perceivedState
    
    def reset(self):
        self.complete = False
        self.daysWorked = 0.0
        self.workAmount = 0.0
        self.trueState = 0.0
        self.perceivedState = 0.0
        self.perceivedGoal = .75
        self.trueGoal = 1.0
        self.communicatedGoal = self.perceivedGoal
        self.communicatedState = 0.0
        self.presentedState = 0.0
        self.gainedKnowledge = 0.0
    
    def setToTrueComplete(self):
        self.complete = True
        self.daysWorked = self.nominalDays
        self.workAmount = 1.0
        self.trueState = 1.0
        self.perceivedState = 1.0
        self.perceivedGoal = 1.0
        self.trueGoal = 1.0
        self.communicatedGoal = self.perceivedGoal
        self.communicatedState = 1.0
        self.presentedState = 1.0
        self.gainedKnowledge = .25
        
    def setToN00bComplete(self):
        self.complete = True
        self.daysWorked = self.nominalDays
        self.workAmount = 1.0
        self.trueState = .75
        self.perceivedState = 1.0
        self.perceivedGoal = .75
        self.trueGoal = 1.0
        self.communicatedGoal = 1.0
        self.communicatedState = .75
        self.presentedState = 1.0
        self.gainedKnowledge = 0.0
    
        
        
    def cap(self,input,capVal):
        output = 0.0
        if (input>capVal):    
            output = capVal
        else:
            output = input
        
        return output
    
    
    def updateHistory(self,newVal):
        for i in range(0,29):
            self.improvementHistory[i] = self.improvementHistory[i+1]
        self.improvementHistory[29] = newVal
        
    def avgImprovement(self):
        avg = sum(self.improvementHistory) / 30.0
        return avg
            
    
    def updateManagementModifier(self,err,goal):
        #print 'received error update of ' + str(err) + ' and goal is ' + str(goal)
        self.managementState = 'Fresh'
        self.managementModifier = err
        self.perceivedGoal = 1.05 * self.perceivedGoal
        if self.perceivedGoal > 1.0:
            self.perceivedGoal = 1.0
        
        
    def calcTrueState(self):
        ts1 = (self.workAmount * float(self.daysWorked))/float(self.nominalDays)
        ts1 = self.cap(ts1,1.0)
        
        prioritySum = self.priority
        
        n = -1
        for t in self.dependsOnTasks:
            n += 1
            prioritySum += t.priority * self.impactAmnt[n]
        
        numSum = ts1
        n = -1
        for t in self.dependsOnTasks:
            n += 1
            numSum += t.trueState * t.priority * self.impactAmnt[n]
            #print ' just added ' + str(t.trueState) + ' from task ' + str(t.name)
        
        ts = numSum / prioritySum
        
        if ts>1.0:
            ts = 1.0
        
        self.trueState = ts * self.perceivedGoal
        self.communicatedState = self.trueState
        return ts
    
    
    def work(self,avgWork,stdDev,effort):
        work = effort * random.gauss(avgWork,stdDev)/self.nominalDays
        return work
        
    
    def calcPerceivedState(self,avgWork,stdDev,effort,timeliness):
        
        oldPerceivedState = self.perceivedState
        
        if (self.perceivedState >= 1.0-self.nullZone) or (self.managementDeemsComplete == True) or (self.noMoreImprovement == True):
            #print 'Task Already Complete, was finished in ' + str(self.daysWorked) + ' days'
            self.complete = True
            
        #elif (self.managementModifier > (1.0 - self.perceivedState)) & (self.managementState == 'Fresh'):
        elif  (self.managementState == 'Fresh'):
            #print 'im an engineer!'
            #print 'ignoring my perception, just listening to boss'
            #print 'management modifier was ' + str(self.managementModifier)
            self.perceivedState = 1.0 - self.managementModifier
            
            # EXPERIMENTAL ! This would AVERAGE their states
            
            avg = (self.perceivedState + (1.0-self.managementModifier)) / 2.0
            self.perceivedState = avg
            
            #print 'so my perceived state is ' + str(self.perceivedState)
            work = self.work(avgWork,stdDev,effort)
            
            self.workAmount += work
            self.daysWorked += 1.0
            self.perceivedState += work
            self.managementState = 'Stale'
            
        #elif (self.managementModifier > (1.0 - self.perceivedState)) & (self.managementState == 'Stale'):
#         elif  (self.managementState == 'Stale'):
#             
#             work = self.work(avgWork,stdDev,effort)
#             
#             self.workAmount += work
#             self.daysWorked += 1.0
#             self.perceivedState += work
            
        else: 
            print 'using my own error perception'
            self.complete = False
            # come up with a work amount
            work = self.work(avgWork,stdDev,effort)
            self.workAmount += work
            self.daysWorked += 1.0
            # calc the denominator
            prioritySum = self.priority
            n = -1
            for t in self.dependsOnTasks:
                n += 1
                prioritySum += t.priority * self.impactAmnt[n]
            
            # calculate the numerator
            numSum = work * self.priority
            #print 'amount of work * priority = ' + str(numSum)
            n = -1
            for t in self.dependsOnTasks:
                n += 1
                print 'communicated error = ' + str(t.communicatedGoal - t.communicatedState)
                print 'so we are adding: ' + str((t.communicatedGoal - t.communicatedState) * t.priority * self.impactAmnt[n])
                numSum += -((t.communicatedGoal - t.communicatedState) * t.priority * self.impactAmnt[n] / self.nominalDays) / prioritySum
                numSum += -((t.communicatedGoal - t.presentedState) * t.priority * effort*self.impactAmnt[n] / self.nominalDays) / prioritySum
            
            ps = numSum 
            self.perceivedState += ps
            
          
            
            
            
        if self.perceivedState<0.0:
            self.perceivedState = 0.0
            
        #print self.improvementHistory
        improvement = self.perceivedState - oldPerceivedState
        self.updateHistory(improvement)
        avgImp = self.avgImprovement()
        #print avgImp
        #print self.improvementHistory
        
        if (self.daysWorked > self.nominalDays*2.0) & (avgImp<self.impThreshold):
            print 'no meaningful improvement'
            self.noMoreImprovement = True
            
            
            
        rv = random.random()
            
        if (rv<timeliness):
            self.updateSharedInfo()
        
    
    def printTrueState(self):
        ts = self.calcTrueState()
        print 'Task: ' + self.name + ' is at trueState = ' + str(ts)
        print 'Task: ' + self.name + ' is at perceivedState = ' + str(self.perceivedState)
    
    
    def printInfoIndented(self):
        self.printTrueState()
        print '    Complete? = ' + str(self.complete)
        print '    Difficulty = ' + str(self.difficulty)
        print '    Category = ' + str(self.category)
        print '    Priority = ' + str(self.priority)
        print '    Nominal Days = ' + str(self.nominalDays)
        print '    Days Worked On = ' +str(self.daysWorked)
        print '    Amount Worked On = ' + str(self.workAmount)
        print '    Depends On Tasks : '+ str(self.dependsOnTasks)
        #for t in self.dependsOnTasks:
            #t.printInfoIndented()
        print '    Impact Amounts = ' + str(self.impactAmnt)
    
    
    def printInfo(self):
#         self.printTrueState()
#         self.printTrueState()
#         self.printTrueState()
#         self.printTrueState()
        print 'Name = ' + str(self.name)
        print 'Complete? = ' + str(self.complete)
        print 'Difficulty = ' + str(self.difficulty)
        print 'Category = ' + str(self.category)
        print 'Priority = ' + str(self.priority)
        print 'Nominal Days = ' + str(self.nominalDays)
        print 'Days Worked On = ' +str(self.daysWorked)
        print 'Amount Worked On = ' + str(self.workAmount)
        print 'Depends On Tasks : '+ str(self.dependsOnTasks)
        #for t in self.dependsOnTasks:
            #t.printInfoIndented()
        print 'Impact Amounts = ' + str(self.impactAmnt)
        print 'True State = ' +str(self.trueState)
        print 'Perceived State = ' + str(self.perceivedState)
        print 'Perceived Goal = ' + str(self.perceivedGoal)
        print 'Communicated Goal = ' + str(self.communicatedGoal)
        print 'Communicated State = ' +str(self.communicatedState)
        print 'Presented State = ' +str(self.presentedState)
        print 'Gained Knowledge = ' +str(self.gainedKnowledge)
        
        
        
        
        
        
    def addDependsTask(self,task,impact):
        self.dependsOnTasks.append(task)
        self.impactAmnt.append(impact)