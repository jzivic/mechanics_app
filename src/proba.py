from src_2.stage_0 import beam_geometry


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







beam_geometry_1 = {
        "length": [0,10],
        "S1": {"z": True, "M": False, "location": 0},
        "S2": {"z": False, "M": True, "location": 10}       # odmah ima x,y oslonce po difoltu jer je uklještenje
}








a = [("z",0), ("z",10), ("M",10), ]




a = {}

for key, value in beam_geometry_1.items():
    if key != "length":


        for k,v in value.items():
            a[key] = v if v is True else None










print(a)
































