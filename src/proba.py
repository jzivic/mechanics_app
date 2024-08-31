





class c1:
    def __init__(self, a):
        print("ovo ide iz c1")
        self.auto = "cvaja"
        self.ime = "josip"



class c2(c1):
    def __init__(self, a, b):
        super().__init__(b)  # Correctly calls the parent class constructor
        print(self.auto)  # Access `auto` through `self`
        print(self.ime)






a = c2(2, 3)