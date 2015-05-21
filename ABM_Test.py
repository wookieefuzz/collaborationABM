from engineer3 import engineer3
from task3 import task3

engSkill = 5.0
engCat = 1.0
timeliness = 0.0

# spawn the engineers
e0 = engineer3('e0',engSkill,engCat)
e1 = engineer3('e1',engSkill,engCat)

# set up the first task
diff = 5.0
cat = 1.0
prio = 1.0
days = 100
name = 'testTask'
 
# make our test task
t0 = task3(diff,cat,prio,days,name)

t1 = task3(diff,cat,prio,days,'taskOtherTaskDependsOn')
 
# impact factor
impactFactor = .1
 
# add the dependsTask
t0.addDependsTask(t1,impactFactor)
t1.addDependsTask(t0,impactFactor)

# add tasks to the engineers
e0.addTask(t0)
e1.addTask(t1)

# set their communication skill
e0.setTimeliness(timeliness)
e1.setTimeliness(timeliness)

engineerList = [e0,e1]

while(t0.complete == False) or (t1.complete == False):
   for e in engineerList:
       e.work()
print '----------------------------------------------------'
t0.printInfo()
print '----------------------------------------------------'
t1.printInfo()


