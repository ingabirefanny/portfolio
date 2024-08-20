class Vehicle:
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color

    def move(self):
        print("starts moving") 

    def hoot(self):
        print("honk honk")       

class Bus (Vehicle):
    def __init__(self,make,model,color,capacity):
        super().__init__(make,model,color)
        self.capacity=capacity
    def start_boarding(self):
        print("the bus is now boarding")    

class Lorry(Vehicle):
    def __init__(self,make,model,color,max_board):
        super().__init__(make,model,color)
        self.max_board=max_board

    def load(self):
        print("start loading")