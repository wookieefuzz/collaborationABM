from taskState import taskState
from task2 import task2
from engineer2 import engineer2

timeResultsList = []
stateResultsList = []

timeliness = 0.0
taskDiff = 10.0
engSkill = 1.0

for x in range(0,1000):

    # create an engineer (0)
    e0 = engineer2(0,engSkill,1) # ID = 0, Skill = 5, Category = 1
    e0.setTimeliness(timeliness)
    t0 = task2(taskDiff,1,1.0,100,'task0') # def __init__(self,diff,cat,prio,days,name):
    t1 = task2(taskDiff,1,1.0,100,'task1') # def __init__(self,diff,cat,prio,days,name):
    e0.addTask(t0)
    e0.addTask(t1)
     
    # create a new engineer (1)
    e1 = engineer2(1,engSkill,1)
    e1.setTimeliness(timeliness)
    t2 = task2(taskDiff,1,1.0,100,'task2') # def __init__(self,diff,cat,prio,days,name):
    t3 = task2(taskDiff,1,1.0,100,'task3') # def __init__(self,diff,cat,prio,days,name):
    e1.addTask(t2)
    e1.addTask(t3)
    
    # create a new engineer (2)
    e2 = engineer2(1,engSkill,1)
    e2.setTimeliness(timeliness)
    t4 = task2(taskDiff,1,1.0,100,'task4') # def __init__(self,diff,cat,prio,days,name):
    t5 = task2(taskDiff,1,1.0,100,'task5') # def __init__(self,diff,cat,prio,days,name):
    e2.addTask(t4)
    e2.addTask(t5)
    
    # set the dependencies
    #e0.addDependentTask(0,.5,t5)
    #e0.addDependentTask(1,.5,t2)
    
    
    #e1.addDependentTask(0,.5,t1)
    #e1.addDependentTask(1,.5,t4)
    
    #e1.addDependentTask(0,.5,t3)
    #e1.addDependentTask(1,.5,t0)
    
    e0.addDependentTask(1,.5,t4)
    e0.addDependentTask(1,.5,t2)
    
    e1.addDependentTask(0,.5,t1)
    
    e2.addDependentTask(0,.5,t1)
    

    while(t0.state.complete == False or t1.state.complete == False or t2.state.complete == False or t3.state.complete == False or t4.state.complete == False or t5.state.complete == False):
        e0.work()
        e1.work()
        e2.work()
        #print '------------------------------------------------------------------'
        #e0.printTaskInfo()
        #e1.printTaskInfo()
    
    
    days = [t0.daysWorked,t1.daysWorked,t2.daysWorked,t3.daysWorked,t4.daysWorked,t5.daysWorked]
    states = [[t0.state.trueState,t1.state.trueState,t2.state.trueState,t3.state.trueState,t4.state.trueState,t5.state.trueState]]
    
    stateResultsList.append(t1.state.trueState)
    timeResultsList.append(max(days))
    
avgDays = sum(timeResultsList)/float(len(timeResultsList))
avgState = sum(stateResultsList)/float(len(stateResultsList))
print 'average days = ' + str(avgDays)
print 'average state = ' + str(avgState)

e0.printTaskInfo()
print states

