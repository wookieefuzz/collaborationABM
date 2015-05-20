from task3 import task3

# # test 1, make sure true state makes sense
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
# t1 = task3(diff,cat,prio,days,'blah')
# 
# # impact factor
# impactFactor = 1.0
# 
# # add the dependsTask
# t0.addDependsTask(t1,impactFactor)
# 
# print 'with both tasks at 0 percent...'
# t0.printTrueState()
# 
# print 'with T0 at 100% ...'
# t0.daysWorked = days
# t0.workAmount = 1.0
# t0.printTrueState()
# 
# print 'with T0 at 100% and lowered priority on T1'
# t1.priority = 0.25
# t0.printTrueState()
# t1.priority = 1.0
# 
# print 'with T0 at 100% and T1 at 100%'
# t1.daysWorked = days
# t1.workAmount = 1.0
# t1.calcTrueState()
# t0.printTrueState()
# 
# print '--------------------------------------------------------'
# 
# avgWork = .8
# stdDev = .1
# effort = 1.0
# 
# t0.daysWorked = 0.0
# t0.workAmount = 0.0
# 
# t1.daysWorked = 0.0
# t1.workAmount = 0.0
# 
# t1.communicatedState = 0.0
# t1.trueState = 0.0
# 
# for i in range(0,100):
#     t0.calcPerceivedState(avgWork,stdDev,effort)
#     t0.printTrueState()
#     #t0.printInfo()
#     print '--------------------------------------------------------'
#     
# 
# t1.communicatedState = 0.0
# for i in range(0,300):
#     t0.calcPerceivedState(avgWork,stdDev,effort)
#     t0.printTrueState()
#     #t0.printInfo()
#     print '--------------------------------------------------------'
# 
# t1.printInfo()
# 
# 
# ## RESET EVERYTHING
# t0.reset()
# t1.reset()
# 
# t0.printInfo()
# t1.printInfo()
# 
# while (t0.complete == False) or (t1.complete == False):
#     t0.calcPerceivedState(avgWork,stdDev,effort)
#     t1.calcPerceivedState(avgWork,stdDev,effort)
#     
# t0.printInfo()
# t1.printInfo()


# test 1, make sure true state makes sense
 
# set up the first task
diff = 5.0
cat = 1.0
prio = 1.0
days = 100
name = 'testTask'
 
# make our test task
t0 = task3(diff,cat,prio,days,name)

avgWork = .8
stdDev = .1
effort = 1.0

t1 = task3(diff,cat,prio,days,'blah')
 
# impact factor
impactFactor = 1.0
 
# add the dependsTask
t0.addDependsTask(t1,impactFactor)
#t1.setToTrueComplete()
#t1.setToN00bComplete()
while(t0.complete == False):
    t0.calcPerceivedState(avgWork,stdDev,effort)
    t1.calcPerceivedState(avgWork,stdDev,effort)
print '----------------------------------------------------'
t0.printInfo()
print '----------------------------------------------------'
t1.printInfo()
