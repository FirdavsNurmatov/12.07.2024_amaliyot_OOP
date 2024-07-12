class Person :
    def __init__ (self,name,surname,birthday) :
        self.name = name
        self.surname = surname
        self.birthday = birthday
    def get_age(self) :
        return 2024-self.birthday
    def get_name(self) :
        return self.name.capitalize(),self.surname.capitalize()

user = Person('firdavs','Nurmatov',2008)
name,surname = user.get_name()
print(name,surname,user.get_age())