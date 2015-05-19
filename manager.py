from engineer import engineer
from task import task

class manager:
    
    def __init__(self,skill):
        self.skill = skill
        self.engineerList = []
        
        
    def addEngineer(self,engineer):
        self.engineerList.append(engineer)
        
    
    def checkForErrors(self):
        
        # manager skill relative to task difficulty informs probability of spotting error
        # manager only recognizes error, not value, feeds back as jump in task goal via modifier
        
        force = 1.0
        
        for engineer in self.engineerList:
            tIndex = -1
            for task in engineer.taskList:
                tIndex = tIndex + 1
                if task.state == 'incomplete':
                    taskError= task.error
                    engineer.getFeedback(tIndex,taskError,force)
                    
    
    

        