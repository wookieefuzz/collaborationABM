from task import task

# difficult, initial value, dependence list, nullzone, nominal days to complete
testTask = task(5.0,0.0,[],0.0,30.0)

cv = 0
days = 0


# def getColleagueModifier(self,IDlist,errorList,influenceList,scaleFactor):

IDlist = [1,2,3]
errorList = [.5 , .1 , .1]
influenceList = [0,1,1]
scaleFactor = .25

while (cv<1):
    days = days + 1
    cv = testTask.doWork(5.0,.9,.25)
    cm = testTask.getColleagueModifier(IDlist,errorList,influenceList,scaleFactor)

print 'colleague modifier is %1.6f' % cm 
print 'task took user ' + str(days) + ' days'
