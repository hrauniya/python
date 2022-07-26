class Dog:

    """
    This is the class attribute, which is the same value for all instances of Dog class.
    """
    species="Canis Familiaris"

    """
    In the constructor, the instance variables are defined where these variables are different for every instance. 
    """
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #instance methods
    """
    __str__ is a dunder method which starts and ends with double underscores.
    """
    def __str__(self):
        # print(self.name,"is",self.age,"years old!")
        return f"{self.name} is {self.age} years old"
    
    def makesound(self,sound):
        # print(self.name,"makes sound",sound)
        return f"{self.name} says {sound}"


"""
These are child classes with Dog class as parent
"""
class Labrador(Dog):
    def makesound(self, sound="BhooBhoo"):
        return f"{self.name} says {sound}"

class GermanShepard(Dog):
    def makesound(self, sound="BhowBhow"):
        return f"{self.name} says {sound}"


class Pitbull(Dog):
    def makesound(self,sound="YapYap"):
        return f"{self.name} says {sound}"



# oreo=Dog("Oreo", 10)
# sinclair=Dog("Sinclair",5)


# print(oreo.name)
# print(oreo.age)

# print("Species:",sinclair.species)
# print(sinclair.name)
# print(sinclair.age)
oreo=Labrador("Oreo", 10)
sinclair=Pitbull("Sinclair",5)
bellamy=GermanShepard("Bellamy",2)

# print(oreo.description())
# print(oreo.makesound("Bhow Bhow!"))


"""
printing using the dunder method __str__. It allows info about the object to be printed without using dot notation.
We can just print the object details by printing the object's name. Without using a dunder method this would not be possible as
printing the object would just print the memory location for the object.
"""


#can make sound with default values defined in the child class 
print(oreo.makesound())
print(bellamy.makesound())
print(sinclair.makesound())

#can also make new sounds that differs from the child class
print(oreo.makesound("Grrrrrr!"))