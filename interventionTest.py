from manager import manager
from engineer3 import engineer3
from task3 import task3

f = open('MonteCarloStrongManagement.txt','w')

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

runNum = 0

for day in range(0,400):
                            
    runNum += 1
    
    e0.setListening(0.0)
    e1.setListening(0.0)
    e2.setListening(0.0)
    m.timeliness = float(.5)
    e0.setTimeliness(0.0)
    e1.setTimeliness(0.0)
    e2.setTimeliness(0.0)
    

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
    
        e0.setListening(0.0)
        e1.setListening(0.0)
        e2.setListening(0.0)
    
        m.sentFeedback = 0.0
    
        for t in taskList:
            t.reset()
         
        numDaysPassed = -1   
        while(t0.complete == False) or (t1.complete == False) or(t2.complete == False) or (t3.complete == False)or(t4.complete == False) or (t5.complete == False):
            numDaysPassed += 1
            
            if numDaysPassed == day:
                e0.setListening(.66)
                e1.setListening(.66)
                e2.setListening(.66)
                
            for e in engineerList:
               e.work()
            m.provideFeedack()

            
        daysToFinish = [t0.daysWorked,t1.daysWorked,t2.daysWorked,t3.daysWorked,t4.daysWorked,t5.daysWorked]
        #print(max(daysToFinish))
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
    #print str(e0.listening) +','+str(e1.listening) +','+str(e2.listening) +','+str(e0.timeliness) +','+str(e1.timeliness) +','+str(e2.timeliness) +','+str(m.timeliness)
    #print 'number = ' + str(runNum)
    print str(day) +','+str(avgDays)


f.close()
