"""

ako je vanjska sila prema dolje, po konvenciji se označava kao negativna
pozitivan moment je u desno, koji zatvara šaku

"""



loads_1 = {
        "L1": {"type": "q", "value": -20, "position": [0,5]},
        "L2": {"type": "F", "value": -10, "position": 4},
}



beam_geometry_1 = {
        "length": [0, 10],
        "z": [1],
        "M": [10]
}







"""

treba dodati za q komponente ekvivalent Q, kako bi suma sila u solveru bila ok 


"""

