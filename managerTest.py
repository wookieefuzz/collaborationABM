# create an engineer with a task
# create a manager and assign the engineer to it
# have the manager intervene weekly (every 5 days)
# check performance with and without manager feedback

from manager import manager
from engineer3 import engineer3
from task3 import task3

#def __init__(self,skill,cat,timeliness,insight):

mSkill = 5.0
mCat = 1.0
mTimeliness = 1.00
mInsight = 1.0
m = manager(mSkill,mCat,mTimeliness,mInsight)

engSkill = 5.0
engCat = 1.0
timeliness = 0.00

# spawn the engineers
e0 = engineer3('e0',engSkill,engCat)
e1 = engineer3('e1',engSkill,engCat)

# set up the first task
diff = 5.0
cat = 1.0
prio = 1.0
days = 100

# make our test task
t0 = task3(diff,cat,prio,days,'t0')
e0.addTask(t0)

t1 = task3(diff,cat,prio,days,'t1')
e1.addTask(t1)

e0.setTimeliness(timeliness)
e1.setTimeliness(timeliness)

e1.setListening(0.0)

m.addEngineer(e0)
m.addEngineer(e1)

# impact factor
impactFactor = 0.5
# add the dependsTask
t0.addDependsTask(t1,impactFactor)

#while (t0.complete == False) or (t1.complete == False): 
while (t0.complete == False) & (t0.daysWorked < 1000): 
    e0.work()
    e1.work()
    print str(t0.trueState) + ',' + str(t0.perceivedState) + ',' +str(t0.perceivedGoal)+','+ str(t0.daysWorked) + ',' + str(t1.trueState) + ',' + str(t1.perceivedState) + ',' +str(t1.perceivedGoal)+','+ str(t1.daysWorked)
    m.provideFeedack()
    
print '----------------------------------------------------'
t0.printInfo()
print '----------------------------------------------------'
t1.printInfo()
