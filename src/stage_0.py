"""

ako je vanjska sila prema dolje, po konvenciji se označava kao negativna
pozitivan moment je u desno, koji zatvara šaku

"""



# loads_1 = {
#         "L1": {"type": "F", "value": -10, "angle": 0, "position": 0},
#         "L2": {"type": "q", "value": -5, "angle": 0, "position": [2, 10]},
#         "L3": {"type": "F", "value": -20, "angle": 0, "position": 10},
#         "L4": {"type": "M", "value": 10, "angle": 0, "position": 0},
# }
#
# beam_geometry = {
#         "length": [0,10],
#         "S1": {"x": True, "y": True, "M": False,  "location": 2},
#         "S2": {"x": True, "y": True, "M": False, "location": 10},
#         "S3": {"M": True, "location": 8}       # odmah ima x,y oslonce po difoltu jer je uklještenje
# }


loads_1 = {
        "L1": {"type": "F", "value": -10, "angle": 0, "position": 5},
        "L2": {"type": "M", "value": 10, "angle": 0, "position": 0},
}

beam_geometry_1 = {
        "length": [0,10],
        "S1": {"z": True, "M": False, "location": 0},
        "S2": {"z": True, "M": True, "location": 10}       # odmah ima x,y oslonce po difoltu jer je uklještenje
}







"""

treba dodati za q komponente ekvivalent Q, kako bi suma sila u solveru bila ok 


"""

