from taskState import taskState

class task2:
    
    def __init__(self,diff,cat,prio,days,name):
        self.name = name
        self.state = taskState()
        self.difficulty = diff
        self.category = cat
        
        self.priority = prio
        self.nominalDays = days
        self.daysWorked = 0.0
            
    def setDifficulty(self,diff):
        self.difficulty = diff
    
    def setCategory(self,cat):
        self.category = cat
        
    def printInfo(self):
        print 'Name = ' + str(self.name)
        self.state.printInfo()
        print 'Difficulty = ' + str(self.difficulty) + '\n'
        print 'Category = ' + str(self.category) + '\n'
        
        print 'Priority = ' + str(self.priority) + '\n'
        print 'Nominal Days = ' + str(self.nominalDays) + '\n'
        print 'Days Worked = ' + str(self.daysWorked) + '\n'