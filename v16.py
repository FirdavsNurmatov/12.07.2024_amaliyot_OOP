class Time :
    def __init__(self,min,sec) :
        self.min = min
        self.sec = sec
    def get_minutes(self) :
        return self.min
    def get_seconds(self) :
        return self.sec

min = int(input('min='))
sec = int(input('sec='))
time = Time(min,sec)
print(f"{time.get_minutes():02d} : {time.get_seconds():02d}")