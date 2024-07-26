import idlelib.replace


def komba(f1, f2):
    def f1_f2(x):
        return f1(f2(x))
    return f1_f2

fog = komba( lambda x:x+1, lambda x:x+2)
a = fog(3)







# Funkcijski dekoratori
# modify the behavior of a function or method.

# idelano rješenje za bilježenje poiva čitavog niza funkicija čiji kod ne želimo ili ne moremo mijenjati


def balet():
    return "Ples sa sabljama"

def podvuci(f):
    def podvucena():
        return f().replace(" ", "_")
    return podvucena()

p = podvuci(balet)



# f2 = lambda a: a.replace(" ", "_")
# print(f2("ovo je represija"))






# "zamjena_decorator" je funckija u koju dolazi neka funkcija kao parametar f - definirana kao dekorator
# ona vraća novu funkciju "wrapper" koja modificira ponašanje "f"


def zamjena_decorator(f):

    def w_b():
        return f().replace("A", "B")

    def w_c():
        return f().replace("A", "C")

    return w_b if 2>13 else  w_c





# funkcija r_a je dekorirana s "zamjena_decorator", dakle r_a se prosljeđuje u "zamjena_decor"
# te ju zamjenjuje wprapper fcija

@zamjena_decorator
def r_a():
    return "ovo je represija AAA"


b = r_a()

# print(b)





# def positive_input(func):
#     def wrapper(x):
#         if x <= 0:
#             raise ValueError("Input must be positive")
#         return func(x)
#     return wrapper
#
# @positive_input
# def square(x):
#     return x**2
#
# print( square(-3) )





def  provjera_pozitivne_stranice(function):
    def wrapper(x, natpis):
        print(natpis)
        if x <= 0:
            raise ValueError("Input must be positive")
        return function(x, natpis)

    return wrapper







@provjera_pozitivne_stranice
def square(x, natpis):
    print(natpis)
    return 4*x




a = square(3, natpis="ovo je represija")


print(a)



