
# CLASS 
class Human:
# class ATTRIBUTE
    species = "homo sapiens"
 
 # initialization method (CONSTRUCTOR)
    def __init__(self, name):
        print(f"A new man named {name} is being created!")
 # object attribute
        self.name = name

 # METHOD - a function inside the CLASS
    def introduce_yourself(self):
        return(f"Hello, my name is {self.name}.")

    def introduce(self, person):
        print(f"Here is {person.name}!")

# default syntax suggested, to be compared with the original underneath
#class Child(Human):
 #   def introduce_yourself(self):
  #      return super().introduce_yourself() 

class Child(Human):
    def introduce_yourself(self):
        print(f"Hi, I'm {self.name}")

    def go_play(self):
        print("What a great fun, fuckin' mindblowing!")

# creating the OBJECT
# recreating from the CLASS
# making by the attached prescription
# actualizing the CLASS

human_01 = Human("Adam")
human_02 = Human("Eve")
man_child_01 = Child("Bimbo")

print(human_01.species)
print(human_02.species)
print(human_01.name)
print(human_02.name)
print(human_01.introduce_yourself())
# checking OBJECT TYPE: print(type(human01))
# checking OBJECT's CONTENT: print(dir(human01))

human_01.introduce_yourself()
human_01.introduce(human_02)
man_child_01.introduce_yourself()
man_child_01.go_play()





