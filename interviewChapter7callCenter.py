import interviewChapter3queues

class CallHandler:
    Levels = 3
    numResponders = 10
    numManagers = 4
    numDirectors = 2

    employeeLevels[0] = "Respondents"
    employeeLevels[1] = "Managers"
    employeeLEvels[2] = "Directors"

    callQueues = Queue()

    def getHandlerForCall(call):

    def dispatchCaller(caller):
        call = new Call(caller)
        dispatchCall(call)

    def dispatchCall(call):
        emp = getHandlerForCall(call)
        if emp is not None:
            emp.receiveCall(call)
            call.setHandler(emp)
        else:
            call.reply("Please wait for employee to reply")
            callQueues.get(call.getRank().getValue()).add(call)

    def assignCall(emp):

class Call:
    def __init__(self, rank, caller):
        self.rank = rank
        self.caller = caller
        self.handler = None

    def setHandler(self, emp):
        self.handler = emp

    def reply(self):
    def getRank(self):
        return self.rank
    def setRank(self, rank):
        self.rank = rank
    def incrementRank(self):
        self.rank = self.rank + 1
    def disconnect(self):


class Employee(CallHandler):
    def __init__(self, rank):
        self.currentCall = None
        self.rank = rank

    def receiveCall(call):

    def callCompleted():
        
        


class Respondant:
    def __init__(self):
        self.canHandle = True

    def dispatchCall(self):
        

class Manager(Respondant):

class Director(Manager):
