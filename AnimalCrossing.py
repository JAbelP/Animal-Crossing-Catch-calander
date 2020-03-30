import json
import datetime




'''Things to add
    Price of item (Nooks shop, after hours, and special buyer)
    List them based on price. 
    List them based on Name.
    Add Fishes

    Time issues:

'''
Bugs=[]
Fishes = []
BugsA=[]
FishesA=[]
timeHour = None
timeMonth= None


class Bug:

     def __init__(self,Ctype,name,time,Months,location,price=0):
        self.name      = name
        self.type      = Ctype
        self.time      = time
        self.Months    = Months
        self.location  = location
        self.price     = price
        self.flickPrice= int(price*1.50)
        self.afterHourPrice = int(price*.80)

     def printNoDetail(self):
        return "Name: {}\nPrice: {}\nflick's price: {}\nAfter hour price: {}".format(self.name,self.price,self.flickPrice,self.afterHourPrice)

     def __str__(self):
        return "Type: {} \nName: {} \nSeasons avaliable: {}\nWhere to find: {}".format(self.type,self.name,self.Months,self.location)

class Fish:
    def __init__(self,Ctype,name,startTime,endTime,month,Location):
        self.name      = name
        self.type      = Ctype
        self.startTime = startTime
        self.endTime   = endTime
        self.month     = month
        self.Location  = Location

    def __str__(self):
        return "Type: {} \nName: {} \nYou can start catching at: {}\nYou will no longer catch at: {}\nLocations: {}\nSeasons avaliable: {}".format(self.type,self.name,self.startTime,self.endTime,self.Location,self.month)


def createList():
    with open('List.json') as file:
        data = json.load(file)
        #-debug
        #counter = 0
        #adding bugs to the list
        for b in data['type']['bug']:
            Bugs.append(Bug("Bug",b['name'],b['time'],b['Season'],b['Location'],b['price']))
            #Debug
            '''
            print("----------")
            print(Bugs[counter])
            print(counter)
            #-debug1
            #counter = counter + 1
            '''


            '''
            #adding fishes
            for f in data['type']['fish']:
            Fishes.append(Fish("Fish",f['name'],f['Start-time'],f['End-Time'],f['Season'],f['Location']))
            '''

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
        timeMonth = datetime.datetime.now().month
        

    if (TimeValue == 2):
        timeHour = int(input("Enter in the hour in the 24 hour format.(ie.10 pm is now 22: "))
        timeMonth = int(input("What month is it (give me the numerical value of month (October = 10)): "))


    #make a list
    for insect in Bugs:
        if(timeMonth in insect.Months):
            for wake in insect.time:
                wakeStart = wake['Start-Time']
                WakeEnd   = wake['End-Time']       
                if(wakeStart<timeHour and WakeEnd>timeHour):
                    BugsA.append(insect)
 


    for creature in Fishes:
        if (creature.startTime<timeHour and creature.endTime>timeHour):
            if(timeMonth in creature.month):
                FishesA.append(creature)
    






createList()
whatIsAvaliableBTime()
for insect in BugsA:
    print(insect)
    print("---------------")
'''
creatingList()
whatIsAvaliableBTime()
for insect in BugsA:
    print(insect.printNoDetail())
    print("---------------")

'''



