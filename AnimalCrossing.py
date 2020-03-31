import json
import datetime
import time




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

     def __init__(self,Ctype,name,time,Months,location,price=0,org=0):
        self.name      = name
        self.type      = Ctype
        self.time      = time
        self.Months    = Months
        self.location  = location
        self.price     = price
        self.flickPrice= int(price*1.50)
        self.afterHourPrice = int(price*.80)
        self.org=org

     def printNoDetail(self):
        return "Name: {}\nPrice: {}\nflick's price: {}\nAfter hour price: {}".format(self.name,self.price,self.flickPrice,self.afterHourPrice)

     def __str__(self):
        return "Type: {} \nName: {} \nSeasons avaliable: {}\nWhere to find: {}\nPrice:{}".format(self.type,self.name,self.Months,self.location,self.price)
     def __lt__(self,other):
         '''
            if org is 0 , it will sort based on name.
            if org is 1 sort based on (nook) value 
         <
         '''
         if (self.org == 0):
             return self.name <other.name
         if(self.org == 1):
            return self.price > other.price
        


class Fish:
    def __init__(self,Ctype,name,time,month,Location,price,shadow,fin=False,org = 0):
        self.name      = name
        self.type      = Ctype
        self.time      = time
        self.month     = month
        self.Location  = Location
        self.price     = price
        self.shadow    = shadow
        self.fin       = fin
        self.cjPrice   = int(price*1.50)
        self.afterHourPrice = int(price*.80)
        self.org = org
    def __str__(self):
        if(self.fin == False):
            return "Type: {} \nName: {} \nLocations: {}\nlook for a size {} shadow\nSeasons avaliable: {}\nPrice: {}".format(self.type,self.name,self.Location,self.shadow,self.month,self.price)
        else:
            return "Type: {} \nName: {} \nLocations: {}\nlook for a size {} shadow with a fin! \nSeasons avaliable: {}\nPrice:".format(self.type,self.name,self.Location,self.shadow,self.month,self.price)

    def __lt__(self,other):
         '''
            if org is 0 , it will sort based on name.
            if org is 1 sort based on (nook) value 
         <
         '''
         if (self.org == 0):
             return self.name <other.name
         if(self.org == 1):
            return self.price > other.price



def createList():
    with open('List.json') as file:
        data = json.load(file)
        #-debug
        #counter = 0
        #adding bugs to the list
        for b in data['type']['bug']:
            Bugs.append(Bug("Bug",b['name'],b['time'],b['Season'],b['Location'],b['price']))
        for f in data['type']['fish']:
            finfin = 'fin' in f
            if finfin == True:
                  Fishes.append(Fish("Fish",f['name'],f['time'],f['Season'],f['Location'],f['price'],f['shadow'],f['fin']))
            else:
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

for insect in BugsA:
        print("---------------")
        print(insect)
print("\n\n\n\n\n")

print("\n\n\n\n\n\nCheck it nerd\n\n\n\n")

for insect in BugsA:
    insect.org = 1
    

BugsA.sort()
for insect in BugsA:
        print("---------------")
        print(insect)
print("\n\n\n\n\n")
FishesA.sort()
for creature in FishesA:
    creature.org = 1
FishesA.sort()

for creature in FishesA:
    print("^^^^^^^^^^^^^")
    print(creature)

'''
for creature in FishesA:
    print("^^^^^^^^^^^^^")
    print(creature)
'''

