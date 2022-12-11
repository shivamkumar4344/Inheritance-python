class Info(object):
    def __init__(self,name,city,gpa,major):
        self.name = name
        self.city = city
        self.gpa = gpa
        self.major = major
    def Display(self):
        print(self.name,self.city,self.gpa,self.major)
        
stud1 = Info("Ravi","Patna",8.5,"Business") 
stud2 = Info("Animesh","Raipur",7.95,"B.Tech")
stud3 = Info("Satyam","Chennai",9.03,"Arts")  
stud1.Display()  
stud2.Display()  
stud3.Display()  

