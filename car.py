class car:

    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"


fordmustang=car("red",10000)
swift=car("blue",20000)


print(fordmustang)
print(swift)