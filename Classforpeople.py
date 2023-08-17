class People:
    def __init__(self,personname,age,bornlocation,home):

        self.personname = personname
        self.age = age
        self.bornlocation = bornlocation
        self.home = home

        #change age (get older) and change home
    

    def Changemetods(self):
        
        self.age= "50"
        self.home= "Paris"
    
    def Callresults(self):

        print("Person name is"+ self.personname +" the age is: " +self.age + " born in " + self.bornlocation + " the home now is: " + self.home)


 # for exemple I will create a a name

p1=People("Laura","28","Belfort","Toulouse")
p1.Callresults()
p1.Changemetods()
p1.Callresults()

