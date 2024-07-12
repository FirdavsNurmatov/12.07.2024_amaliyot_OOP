class Point :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
    def get_quarter(self) :
        # print(1)
        if self.x > 0 < self.y :
            print("x and y in 1-quarter")
        elif self.x < 0 > self.y :
            print("x and y in 3-quarter")
        elif self.x < 0 < self.y :
            print("x and y in 2-quarter")
        elif self.x > 0 > self.y :
            print("x and y in 4-quarter")
        else :
            print("x or y not in any quarter")

x = int(input('x = '))
y = int(input('y = '))
coordinate = Point(x,y)
coordinate.get_quarter()