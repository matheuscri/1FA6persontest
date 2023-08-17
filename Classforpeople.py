class People:
    def __init__(self,personname,age,bornlocation,home):

        self.personname = personname
        self.age = age
        self.bornlocation = bornlocation
        self.home = home

        #change age (get older) and change home
    

    def Changemetods(self):
        
        print("What's the new age?")
        self=input(self.age)
        print("What's the new home?")
        self=input(self.home)


 # for exemple I will create a a name

p1=People("Laura","28","Belfort","Toulouse")
print(p1)