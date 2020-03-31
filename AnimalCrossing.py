import json
import datetime




'''Things to add
    List them based on price. 
    List them based on Name.
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
    def __init__(self,Ctype,name,time,month,Location,price,shadow):
        self.name      = name
        self.type      = Ctype
        self.time      = time
        self.month     = month
        self.Location  = Location
        self.price     = price
        self.shadow    = shadow
        self.cjPrice   = int(price*1.50)
        self.afterHourPrice = int(price*.80)
    def __str__(self):
        return "Type: {} \nName: {} \nLocations: {}\nlook for {} shadows\nSeasons avaliable: {}".format(self.type,self.name,self.Location,self.shadow,self.month)


def createList():
    with open('List.json') as file:
        data = json.load(file)
        #-debug
        #counter = 0
        #adding bugs to the list
        for b in data['type']['bug']:
            Bugs.append(Bug("Bug",b['name'],b['time'],b['Season'],b['Location'],b['price']))
        for f in data['type']['fish']:
            Fishes.append(Fish("Fish",f['name'],f['time'],f['Season'],f['Location'],f['price'],f['shadow']))
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

                if(wakeStart<=timeHour and WakeEnd>=timeHour):
                    BugsA.append(insect)
 


    for creature in Fishes:
        if(timeMonth in creature.month):
            for wake in creature.time:
                wakeStart = wake['Start-Time']
                WakeEnd   = wake['End-Time'] 
                    
                if(wakeStart<=timeHour and WakeEnd>=timeHour):
                    FishesA.append(creature)


createList()
whatIsAvaliableBTime()
counter = 0
for insect in BugsA:
        print("---------------")
        print(insect)
print("\n\n\n\n\n")
for creature in FishesA:
    print("^^^^^^^^^^^^^")
    print(creature)


