from manager import manager
from engineer3 import engineer3
from task3 import task3

f = open('MonteCarlo5.txt','w')

numRuns = 100

mSkill = 5.0
mCat = 1.0
mTimeliness = 1.0
mInsight = 1.0
m = manager(mSkill,mCat,mTimeliness,mInsight)


engSkill = 5.0
engCat = 1.0
timeliness = 1.0
listening = 1.0

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
impactFactor = .5
 
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

for e in engineerList:
    e.setListening(listening)

m.addEngineer(e0)
m.addEngineer(e1)
m.addEngineer(e2)

taskList = [t0, t1, t2, t3, t4, t5]

for mt in range(0,3):
    for e0l in range(0,3):
        for e1l in range(0,3):
            for e2l in range(0,3):
                for e0t in range(0,3):
                    for e1t in range(0,3):
                        for e2t in range(0,3):
    
                            e0.setListening(.5*float(e0l))
                            e1.setListening(.5*float(e1l))
                            e2.setListening(.5*float(e2l))
                            m.timeliness = .5*float(mt)
                            e0.setTimeliness(.5*float(e0t))
                            e1.setTimeliness(.5*float(e1t))
                            e2.setTimeliness(.5*float(e2t))
                            
                
                            days = []
                            
                            timesManaged = 0.0
                            sharedInfo = 0.0
                            timesListened = 0.0
                            maxCompletion = 0.0
                            maxCompletionBest = 0.0
                            minCompletion = 0.0
                            minCompletionBest = 1.0
                            avgCompletion = 0.0
                            
                            for test in range(0,numRuns):
                            
                                m.sentFeedback = 0.0
                            
                                for t in taskList:
                                    t.reset()
                                    
                                while(t0.complete == False) or (t1.complete == False) or(t2.complete == False) or (t3.complete == False)or(t4.complete == False) or (t5.complete == False):
                                    for e in engineerList:
                                       e.work()
                                    m.provideFeedack()
                                    #print str(t0.trueState) + ',' + str(t0.perceivedState) + ',' +str(t0.perceivedGoal)+','+ str(t0.daysWorked) + ',' + str(t1.trueState) + ',' + str(t1.perceivedState) + ',' +str(t1.perceivedGoal)+','+ str(t1.daysWorked)
                                #     t0.printInfo()
                                #     t1.printInfo()
                                #     t2.printInfo()
                                #     t3.printInfo()
                                #     t4.printInfo()
                                #     t5.printInfo()
                                    
                                daysToFinish = [t0.daysWorked,t1.daysWorked,t2.daysWorked,t3.daysWorked,t4.daysWorked,t5.daysWorked]
                                days.append(max(daysToFinish))
                                timesManaged += m.sentFeedback
                                for t in taskList:
                                    sharedInfo += t.updatedTimes
                            
                                for e in engineerList:
                                   timesListened += e.listenedTimes
                                   e.listenedTimes = 0.0
                            
                                maxCompletion = max([t0.trueState,t1.trueState,t2.trueState,t3.trueState,t4.trueState,t5.trueState])
                                maxCompletionBest = max([maxCompletion,maxCompletionBest])
                                
                                minCompletion = min([t0.trueState,t1.trueState,t2.trueState,t3.trueState,t4.trueState,t5.trueState])
                                minCompletionBest = min([minCompletion,minCompletionBest])
                            
                                avgCompletion += sum([t0.trueState,t1.trueState,t2.trueState,t3.trueState,t4.trueState,t5.trueState]) / 6.0
                                
                            
                            avgUpdatedTime = sharedInfo / numRuns
                            avgListenedTimes = timesListened / numRuns
                            avgDays = sum(days)/len(days)
                            avgTimesManaged = timesManaged / numRuns
                            avgCompletion = avgCompletion / numRuns
                            #print 'average number of days to complete all tasks = ' + str(avgDays)
                            #print 'average number of times managed = ' + str(avgTimesManaged)
                            #print 'average number of times listened = ' + str(avgListenedTimes)
                            #print 'average number of times updated = ' + str(avgUpdatedTime)
                            #print 'worst completion = ' + str(minCompletionBest)
                            #print 'best completion = ' + str(maxCompletionBest)
                            #print 'avg completion = ' + str(avgCompletion)
                            
                            text = str(e0.listening) +','+str(e1.listening) +','+str(e2.listening) +','+str(e0.timeliness) +','+str(e1.timeliness) +','+str(e2.timeliness) +','+str(m.timeliness)+','+str(impactFactor)+','+str(avgDays)+','+str(avgTimesManaged)+','+str(avgListenedTimes)+','+str(avgUpdatedTime)+','+str(minCompletionBest)+','+str(maxCompletionBest)+','+str(avgCompletion)
                            f.write(text +' \n')
                            print str(e0.listening) +','+str(e1.listening) +','+str(e2.listening) +','+str(e0.timeliness) +','+str(e1.timeliness) +','+str(e2.timeliness) +','+str(m.timeliness)
                            

f.close()
