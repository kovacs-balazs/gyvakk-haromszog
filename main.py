import argparse
from triangle import *

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--nogui", action="store_true", help="konzol használata")
my_parser.add_argument("--noround", action="store_true", help="kerekítés kikapcsolása")
my_parser.add_argument("--round", action="store", dest="INT", default=3, type=int, help="kerekítési érték megadása")

def check_inputs(input: str):
    if input == "exit":
        exit()
    if input == "list":
        print(get_keruletek_sorted())
        return None
    else:
        # Bemenet ellenőrzés
        try:
            befogo = float(input)
            if befogo <= 0: # Nullával vagy nullánál kisebb értékkel nem lehet számolni.
                print("A beadott érték nullánál nagyobb kell legyen!")
                return None
        except ValueError: # Bármilyen error esetén nem érvényes a bemenet
            print("A beadott érték csak szám lehet!")
            return None
    return input

args = my_parser.parse_args()

if args.noround:
    disable_round()
else:
    set_round(args.round)

if args.nogui:
    while True:
        try:
            a = float(check_inputs(input("Add meg az 'a' befogó méretét: ")))
            b = float(check_inputs(input("Add meg a 'b' befogó méretét: ")))
        except TypeError:
            continue
        
        triangle = Triangle(a, b)
        print(f"Kerület: {triangle.get_kerulet_rounded()}")
        add(triangle)
else:
    import gui
    gui.gui_open()