from engineer import engineer

# let's create two engineers
e0 = engineer(0,1,5) # ID,numTasks,skillLevel
e1 = engineer(1,1,5)

e0.printTaskInfo()
e1.printTaskInfo()

for d in range(0,365):
    e0.work()
    e1.work()
    
print '----------------------------------'

e0.printTaskInfo()
e1.printTaskInfo()