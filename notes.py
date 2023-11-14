#Class inheritance
"""
class Fish(Animal):
    def __init__(self):
        super().__init__()

"""
#Fish is inheriting from the Animal class
# to get a hold of everything that an Animal has / is, add super().__init__() - initialize everything in the super-class (Animal)

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):

    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this under water.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
# nemo.swim()
nemo.breathe()
# print(nemo.num_eyes)

"""
slicing lists and tuples
piano_keys = ["a" ,"b" ,"c" ,"d" ,"e" ,"f", "g"]
piano_keys = [2:5] = [c,d,e]
slices start at the beginning, i.e. '5' is between e and f





"""