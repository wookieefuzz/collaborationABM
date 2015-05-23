from engineer3 import engineer3
from task3 import task3
import random

class manager:
    
    def __init__(self,skill,cat,timeliness,insight):
        self.skill = skill
        self.category = cat
        self.timeliness = timeliness
        self.insight = insight
        self.engineerList = []
        self.specialtyModifier = .75
        
        
    def addEngineer(self,engineer):
        self.engineerList.append(engineer)
        
    
    
    def provideFeedack(self):
        
        # for each engineer in their purview
        # for each task that engineer has
        # if its in the managers specialty area, give em the whole truth
        # ADD DIFFICULTY MOD
        # take a hit if not the same category
        # create error list, feed to engineer in one go 
        
        for e in self.engineerList:
            errList = []
            goalList = []
            for t in e.taskList:
                rv = random.random()
                if rv < self.timeliness:
                    actualTaskError = t.trueGoal - t.trueState
                    if actualTaskError <= 0.0 :
                        actualTaskError = 0.0
                        t.managementDeemsComplete = True
                    #print 'manager sees task goal as ' +str(t.trueGoal) + ' and state as ' +str(t.trueState) +' and error is ' + str(actualTaskError)
                    if (self.category == t.category):
                        perceivedError = self.insight * actualTaskError
                    else:
                        perceivedError = self.insight * actualTaskError * self.specialtyModifier
                    #print 'perceived error communicated to engineer = ' + str(perceivedError)
                    errList.append(perceivedError)
                    goalList.append(1.0)
            e.receiveFeedback(errList,goalList)
                
    
#     def checkForErrors(self):
#         
#         # manager skill relative to task difficulty informs probability of spotting error
#         # manager only recognizes error, not value, feeds back as jump in task goal via modifier
#         
#         force = 1.0
#         
#         for engineer in self.engineerList:
#             tIndex = -1
#             for task in engineer.taskList:
#                 tIndex = tIndex + 1
#                 if task.state == 'incomplete':
#                     taskError= task.error
#                     engineer.getFeedback(tIndex,taskError,force)
                    
    
    

        