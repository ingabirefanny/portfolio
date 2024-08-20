class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass
    def eat(self):
        pass
class Bird(Animal):
    def make_sound(self):
        print("chirp")
    def move(self):
        print("flying")
    def eat(self):
        print("insect")    
class Fish(Animal):
    def make_sound(self):
        print("click")   
    def move(self):
        print("swimming")
    def eat(self):
        print("plants")    
class Dog(Animal):
    def make_sound(self):
        print("Bark")
    def move(self):
        print("running")   
    def eat(self):
        print("meat")    
class Human(Animal):
    def make_sound(self):
        print("Talk")
    def move(self):
        print("Walking") 
    def eat(self):
        print("Food")                      


