''''
class Emp:
    company_name="Khyaathi"
    company_address="maithrivanam"
    def __init__(self,name,e_id):
        self.name=name
        self.id=e_id
    def get(self):
        return self.id,self.name,self.company_name,self.company_address
sai=Emp("sailaxmi",2)
jay=Emp("jayaram",3)
'''
'''
print(sai.get())
print(jay.get())
print(Emp.company_name)
print(Emp.company_address)
print(sai.company_address)
print(sai.company_name)
print(sai.name)
print(sai.id)
print(Emp.name)
'''



class Emp:
    company_name="Khyaathi"
    company_address="maithrivanam"
    def __init__(self,name,e_id):
        self.name=name
        self.id=e_id
        
    @staticmethod
    def parsing(x,y): #static method
        return x+y
    @classmethod
    def get_company(cls,x): # class method
        return cls.company_name,cls.company_address
    def get(self): # instance method
        return self.id,self.name,self.company_name,self.company_address
sai=Emp("sailaxmi",2)
jay=Emp("jayaram",3)
#print(sai.get_company())
#print(Emp.get_company())
#print(sai.get_company())
print(Emp.parsing(100,200))
print(sai.parsing(10,20))
print(Emp.get_company(10))
print(sai.get_company(20))
print(sai.get())
print(Emp.get(sai))
