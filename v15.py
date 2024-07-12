class Countries :
    def __init__(self,c_name,c_city,c_community,c_chegaros,c_prezident) :
        self.c_name = c_name
        self.c_city = c_city
        self.c_community = c_community
        self.c_chegaros = c_chegaros
        self.c_prezident = c_prezident
    def info(self) :
        print(f"""    {self.c_name}, {self.c_city}, {self.c_community}, {self.c_chegaros}, {self.c_prezident}""")
   
lst = [
    Countries('Amerika','New-York',500262000,456,'Bayden'),
    Countries('Kanada','New-York',100023500,356,'Trump'),
    Countries('Braziliya','Rio-de-Janero',523000300,256,'Trump'),
    Countries('Tojikiston','Bapesh',5000023000,156,'Trump'),
    Countries("O'zbekiston",'Toshkent',5004300000,456,'Shavkat'),
    Countries('Rossiya','Moskva',500000020,1096,'Putin'),
    Countries('Moldova','Borusiya',340000000,256,'Trump'),
    Countries('Ukraina','New-York',500060000,254,'Jorj'),
    Countries('Polsha','Varshava',3000630000,446,'Trump'),
    Countries('Chexiya','Praga',40060020,126,'Trump')
]
lst2 = sorted(lst,key = lambda x: x.c_name)
for i in lst2 :
    i.info()