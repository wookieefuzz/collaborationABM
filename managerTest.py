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
mTimeliness = 1.0
mInsight = 1.0
m = manager(mSkill,mCat,mTimeliness,mInsight)

engSkill = 5.0
engCat = 1.0
timeliness = 1.0

# spawn the engineers
e0 = engineer3('e0',engSkill,engCat)

# set up the first task
diff = 5.0
cat = 1.0
prio = 1.0
days = 100

# make our test task
t0 = task3(diff,cat,prio,days,'t0')
e0.addTask(t0)

e0.setTimeliness(timeliness)

m.addEngineer(e0)


while(t0.complete == False): 
    e0.work()
    print str(t0.trueState) + ',' + str(t0.perceivedState)
    m.provideFeedack()
    
print '----------------------------------------------------'
t0.printInfo()
