from engineer import engineer

case = 1

# two engineers, one task apiece, one task dependent on the other
if case == 1:
    numtrials = 10000
    # run 10,000 trials with dependence between the engineers and 10,000 without
    # track the average goal for each, compare
    
    # apparently the average error is about the same, lets also check the time to close the design
    
    dependenceHistory = 0.0
    independenceHistory = 0.0
    DPworkHistory = 0.0
    IDPworkHistory = 0.0
    
    
    for trial in range(0,numtrials-1):
    
        # let's create two engineers
        e0 = engineer(0,1,5) # ID,numTasks,skillLevel
        e1 = engineer(1,1,5)
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
        
        # lets make task 1 for engineer 0 dependent on task 1 of engineer 1
        
        IDlist = ['1-1']
        errorList = [-.25]
        influenceList = [1.0]
        scaleFactor = .25
        
        e0.taskList[0].updateErrorList(IDlist,errorList,influenceList,scaleFactor)
        
        for d in range(0,180):
            e0.taskList[0].updateErrorList(IDlist,[e1.taskList[0].error],influenceList,scaleFactor)
            e0.work()
            e1.work()
            
    #     print '----------------------------------'
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
    
        dependenceHistory = dependenceHistory + e0.taskList[0].error
        DPworkHistory = DPworkHistory + float(e0.taskList[0].daysWorked)
        
    for trial in range(0,numtrials-1):
    
        # let's create two engineers
        e0 = engineer(0,1,5) # ID,numTasks,skillLevel
        e1 = engineer(1,1,5)
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
        
        # lets make task 1 for engineer 0 dependent on task 1 of engineer 1
        
        IDlist = ['1-1']
        errorList = [-.25]
        influenceList = [0.0]
        scaleFactor = .25
        
        e0.taskList[0].updateErrorList(IDlist,errorList,influenceList,scaleFactor)
        
        for d in range(0,180):
            e0.taskList[0].updateErrorList(IDlist,[e1.taskList[0].error],influenceList,scaleFactor)
            e0.work()
            e1.work()
            
    #     print '----------------------------------'
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
    
        independenceHistory = independenceHistory + e0.taskList[0].error
        IDPworkHistory = IDPworkHistory + float(e0.taskList[0].daysWorked)
        
    independenceAvg = independenceHistory/float(numtrials)
    dependenceAvg = dependenceHistory/float(numtrials)
    
    IDPavg = IDPworkHistory / float(numtrials)
    DPavg = DPworkHistory / float(numtrials)
    
    print 'average error with independent tasks was ' + str(independenceAvg) 
    print 'average error with dependent tasks was ' + str(dependenceAvg)
    
    print 'average days worked with independent tasks was ' + str(IDPavg) 
    print 'average days worked with dependent tasks was ' + str(DPavg)
    
elif case == 2:

    numtrials = 100000
    # run 10,000 trials with dependence between the engineers and 10,000 without
    # track the average goal for each, compare
    
    # apparently the average error is about the same, lets also check the time to close the design
    
    dependenceHistory0 = 0.0
    independenceHistory0 = 0.0
    DPworkHistory0 = 0.0
    IDPworkHistory0 = 0.0
    
    dependenceHistory1 = 0.0
    independenceHistory1 = 0.0
    DPworkHistory1 = 0.0
    IDPworkHistory1 = 0.0
    
    for trial in range(0,numtrials-1):
    
        # let's create two engineers
        e0 = engineer(0,1,5) # ID,numTasks,skillLevel
        e1 = engineer(1,1,5)
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
        
        # lets make task 1 for engineer 0 dependent on task 1 of engineer 1
        
        IDlist = ['1-1']
        errorList = [-.25]
        influenceList = [1.0]
        scaleFactor = .25
        
        e0.taskList[0].updateErrorList(IDlist,errorList,influenceList,scaleFactor)
        e1.taskList[0].updateErrorList(IDlist,errorList,influenceList,scaleFactor)
        
        for d in range(0,180):
            e0.taskList[0].updateErrorList(IDlist,[e1.taskList[0].error],influenceList,scaleFactor)
            e1.taskList[0].updateErrorList(IDlist,[e0.taskList[0].error],influenceList,scaleFactor)
            e0.work()
            e1.work()
            
    #     print '----------------------------------'
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
    
        dependenceHistory0 = dependenceHistory0 + e0.taskList[0].error
        DPworkHistory0 = DPworkHistory0 + float(e0.taskList[0].daysWorked)
        dependenceHistory1 = dependenceHistory1 + e1.taskList[0].error
        DPworkHistory1 = DPworkHistory1 + float(e1.taskList[0].daysWorked)
        
    for trial in range(0,numtrials-1):
    
        # let's create two engineers
        e0 = engineer(0,1,5) # ID,numTasks,skillLevel
        e1 = engineer(1,1,5)
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
        
        # lets make task 1 for engineer 0 dependent on task 1 of engineer 1
        
        IDlist = ['1-1']
        errorList = [-.25]
        influenceList = [0.0]
        scaleFactor = .25
        
        e0.taskList[0].updateErrorList(IDlist,errorList,influenceList,scaleFactor)
        e1.taskList[0].updateErrorList(IDlist,errorList,influenceList,scaleFactor)
        
        for d in range(0,180):
            e0.taskList[0].updateErrorList(IDlist,[e1.taskList[0].error],influenceList,scaleFactor)
            e1.taskList[0].updateErrorList(IDlist,[e0.taskList[0].error],influenceList,scaleFactor)
            e0.work()
            e1.work()
            
    #     print '----------------------------------'
        
    #     e0.printTaskInfo()
    #     e1.printTaskInfo()
    
        independenceHistory0 = independenceHistory0 + e0.taskList[0].error
        IDPworkHistory0 = IDPworkHistory0 + float(e0.taskList[0].daysWorked)
        independenceHistory1 = independenceHistory1 + e1.taskList[0].error
        IDPworkHistory1 = IDPworkHistory1 + float(e1.taskList[0].daysWorked)
        
    independenceAvg0 = independenceHistory0/float(numtrials)
    dependenceAvg0 = dependenceHistory0/float(numtrials)
    
    IDPavg0 = IDPworkHistory0 / float(numtrials)
    DPavg0 = DPworkHistory0 / float(numtrials)
    
    independenceAvg1 = independenceHistory1/float(numtrials)
    dependenceAvg1 = dependenceHistory1/float(numtrials)
    
    IDPavg1 = IDPworkHistory1 / float(numtrials)
    DPavg1 = DPworkHistory1 / float(numtrials)
    
    print '0 average error with independent tasks was ' + str(100*independenceAvg0) 
    print '0 average error with dependent tasks was ' + str(100*dependenceAvg0)
    
    print '0 average days worked with independent tasks was ' + str(IDPavg0) 
    print '0 average days worked with dependent tasks was ' + str(DPavg0)
    
    print '1 average error with independent tasks was ' + str(100*independenceAvg1) 
    print '1 average error with dependent tasks was ' + str(100*dependenceAvg1)
    
    print '1 average days worked with independent tasks was ' + str(IDPavg1) 
    print '1 average days worked with dependent tasks was ' + str(DPavg1)