# from engineer3 import engineer3
# from task3 import task3
# 
# engSkill = 5.0
# engCat = 1.0
# timeliness = 0.0
# 
# # spawn the engineers
# e0 = engineer3('e0',engSkill,engCat)
# e1 = engineer3('e1',engSkill,engCat)
# 
# # set up the first task
# diff = 5.0
# cat = 1.0
# prio = 1.0
# days = 100
# name = 'testTask'
#  
# # make our test task
# t0 = task3(diff,cat,prio,days,name)
# 
# t1 = task3(diff,cat,prio,days,'taskOtherTaskDependsOn')
#  
# # impact factor
# impactFactor = .1
#  
# # add the dependsTask
# t0.addDependsTask(t1,impactFactor)
# t1.addDependsTask(t0,impactFactor)
# 
# # add tasks to the engineers
# e0.addTask(t0)
# e1.addTask(t1)
# 
# # set their communication skill
# e0.setTimeliness(timeliness)
# e1.setTimeliness(timeliness)
# 
# engineerList = [e0,e1]
# 
# while(t0.complete == False) or (t1.complete == False):
#    for e in engineerList:
#        e.work()
# print '----------------------------------------------------'
# t0.printInfo()
# print '----------------------------------------------------'
# t1.printInfo()

from engineer3 import engineer3
from task3 import task3

engSkill = 5.0
engCat = 1.0
timeliness = 0.0

# spawn the engineers
e0 = engineer3('e0',engSkill,engCat)
e1 = engineer3('e1',engSkill,engCat)
e2 = engineer3('e2',engSkill,engCat)

# set up the first task
diff = 5.0
cat = 1.0
prio = 1.0
days = 100

 
# make our test task
t0 = task3(diff,cat,prio,days,'t0')
t1 = task3(diff,cat,prio,days,'t1')
t2 = task3(diff,cat,prio,days,'t2')
t3 = task3(diff,cat,prio,days,'t3')
t4 = task3(diff,cat,prio,days,'t4')
t5 = task3(diff,cat,prio,days,'t5')
 
# impact factor
impactFactor = 1.0
 
# add the dependsTask
t0.addDependsTask(t5,impactFactor)
t1.addDependsTask(t2,impactFactor)
t2.addDependsTask(t1,impactFactor)

# add tasks to the engineers
e0.addTask(t0)
e0.addTask(t1)

e1.addTask(t2)
e1.addTask(t3)

e2.addTask(t4)
e2.addTask(t5)

# set their communication skill
e0.setTimeliness(timeliness)
e1.setTimeliness(timeliness)
e2.setTimeliness(timeliness)

engineerList = [e0,e1,e2]

while(t0.complete == False) or (t1.complete == False) or(t2.complete == False) or (t3.complete == False)or(t4.complete == False) or (t5.complete == False):
    for e in engineerList:
       e.work()
#     t0.printInfo()
#     t1.printInfo()
#     t2.printInfo()
#     t3.printInfo()
#     t4.printInfo()
#     t5.printInfo()
    
print '----------------------------------------------------'
t0.printInfo()
print '----------------------------------------------------'
t1.printInfo()
print '----------------------------------------------------'
t2.printInfo()
print '----------------------------------------------------'
t3.printInfo()
print '----------------------------------------------------'
t4.printInfo()
print '----------------------------------------------------'
t5.printInfo()


