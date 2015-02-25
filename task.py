class task:
    
    def __init__(self,difficulty,targetValue,initialValue,dependenceList,nullZone,skill):
        self.skill = skill
        self.state = 'incomplete'
        self.difficulty = difficulty
        self.targetValue = targetValue
        self.initialValue = initialValue
        self.currentValue = initialValue
        self.dependenceList = dependenceList
        self.nullZone
        self.contributedInformation = [0] * len(dependenceList) # initialize values from colleagues as zeros for now
        
        # dependence list supplies the number of inputs needed for the task/model
        # model won't converge until all dependence variables are converged
        # harder problems should maybe have more dependence variables?
        # dependenceList is a list of the ID's needed for updating the model
        
        
    def doWork(self,workRate):
        return void

    def runModel(self,inputValue,contributedInformation):
        # run the model
        return void
        
    def updateModel(self,contributor,newValue):
        index = dependenceList.index(contributor);
        self.contributedInformation[index] = newValue        
        return void