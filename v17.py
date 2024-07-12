class Car :
    def __init__(self,speed,time) :
        self.speed = speed
        self.time = time
    def get_info(self) :
        return self.speed * self.time

speed = int(input("speed(kilometers) = "))
time = int(input('time(hours) = '))
find_distance = Car(speed,time)
print(f"Answer: {find_distance.get_info()} km/h")