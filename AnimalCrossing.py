import json
import datetime




'''Things to add
    Price of item (Nooks shop, after hours, and special buyer)
    List them based on price. 
    List them based on Name.
    Time function - Current Time and what ever time the user wants.
    Check if the month is correct (Maybe change from Name date to Numerical Date?)
    Time issues:
    Emperor ButterFly
    Moth
    Man-Faced Stinkbug
    Tarantula
    HermitCrab
    Spider
    PillBug
'''
Bugs=[]
Fishes = []
BugsA=[]
FishesA=[]
timeHour = None


class Bug:
    def __init__(self,Ctype,name,startTime,endTime,Months,price=0):
        self.name      = name
        self.type      = Ctype
        self.startTime = startTime
        self.endTime   = endTime
        self.Months    = Months
        self.price     = price
    
    def printNoDetail(self):
        return "Name: {}\nPrice: {}\nCan catch until: {}".format(self.name,self.price,self.endTime)

    def __str__(self):
       
     return "Type: {} \nName: {} \nYou can start catching at: {}\nYou will no longer catch at: {}\nSeasons avaliable: {}".format(self.type,self.name,self.startTime,self.endTime,self.Months)

class Fish:
    def __init__(self,Ctype,name,startTime,endTime,month,Location):
        self.name      = name
        self.type      = Ctype
        self.startTime = startTime
        self.endTime   = endTime
        self.month    = month
        self.Location  = Location

    def __str__(self):
        return "Type: {} \nName: {} \nYou can start catching at: {}\nYou will no longer catch at: {}\nLocations: {}\nSeasons avaliable: {}".format(self.type,self.name,self.startTime,self.endTime,self.Location,self.month)

def whatIsAvaliableBTime():
    '''
        Set the Time 
    '''
    print("Use the current time or have you time skipped?")
    TimeValue = 0
    while TimeValue>2 or TimeValue<1:
        TimeValue = int(input("1 for Computer time/ 2 for own time: "))
    if (TimeValue == 1):
        timeHour= datetime.datetime.now().hour
        print("Abel")

    if (TimeValue == 2):
        timeHour = int(input("Enter in the hour in the 24 hour format.(ie.10 pm is now 22: "))

    #make a list
    for insect in Bugs:
        if (insect.startTime<timeHour and insect.endTime>timeHour):
            if(datetime.datetime.now().month in insect.Months):
                BugsA.append(insect)

    for creature in Fishes:
        if (creature.startTime<timeHour and creature.endTime>timeHour):
            if(datetime.datetime.now().month in creature.Months):
                FishesA.append(creature)
    
def creatingList():
    '''
    This creates the Bugs and Fish list that will be used in other methods.

    '''
    with open('List.json') as file:
        data = json.load(file)

        #adding bugs to the list
        for b in data['type']['bug']:
            
            Bugs.append(Bug("Bug",b['name'],b['Start-time'],b['End-Time'],b['Season']))

        #adding fishes
        for f in data['type']['fish']:
            Fishes.append(Fish("Fish",f['name'],f['Start-time'],f['End-Time'],f['Season'],f['Location']))


creatingList()
whatIsAvaliableBTime()
for insect in BugsA:
    print(insect.printNoDetail())
    print("---------------")





