




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
        print(f"Hello, my name is {self.name}.")

    def introduce(self, Human):
        print(f"Here is {Human.name}!")

# creating the OBJECT
# recreating from the CLASS
# making by the attached prescription
# actualizing the CLASS

human_01 = Human("Adam")
human_02 = Human("Eve")

print(human_01.species)
print(human_02.species)
print(human_01.name)
print(human_02.name)

# checking OBJECT TYPE: print(type(human01))
# checking OBJECT's CONTENT: print(dir(human01))

human_01.introduce_yourself()
human_01.introduce(human_02)




