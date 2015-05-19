from engineer import engineer

# let's create two engineers
e0 = engineer(0,1,5) # ID,numTasks,skillLevel
e1 = engineer(1,1,5)

e0.printTaskInfo()
e1.printTaskInfo()

# lets make task 1 for engineer 0 dependent on task 1 of engineer 1

IDlist = ['1-1']
errorList = [-.25]
influenceList = [1.0]
scaleFactor = .2

e0.taskList[0].updateErrorList(IDlist,errorList,influenceList,scaleFactor)

for d in range(0,365):
    e0.taskList[0].updateErrorList(IDlist,[e1.taskList[0].error],influenceList,scaleFactor) # this grabs the most recent error
    e0.work()
    e1.work()
    e0.communicate()
    e1.communicate()
    
print '----------------------------------'

e0.printTaskInfo()
e1.printTaskInfo()