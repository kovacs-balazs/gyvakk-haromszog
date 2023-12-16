import argparse
import triangle

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--nogui", action="store_true", help="konzol használata")
my_parser.add_argument("--noround", action="store_true", help="kerekítés kikapcsolása")
my_parser.add_argument("--round", action="store", default=3, type=int, help="kerekítési érték megadása")

def check_inputs(input: str) -> str | None:
    if input.lower() == "exit":
        exit()
    if input.lower() == "list":
        print(triangle.get_keruletek_sorted())
        return None
    else:
        # Bemenet ellenőrzés
        try:
            befogo: float = float(input)
            if befogo <= 0: # Nullával vagy nullánál kisebb értékkel nem lehet számolni.
                print("A beadott érték nullánál nagyobb kell legyen!")
                return None
        except ValueError: # Bármilyen error esetén nem érvényes a bemenet
            print("A beadott érték csak szám lehet!")
            return None
    return input

args = my_parser.parse_args()

if args.noround:
    triangle.round_tizedesjegy: int = -1
else:
    triangle.round_tizedesjegy: int = args.round

if args.nogui: # Konzol használata
    while True:
        try:
            a: float = float(check_inputs(input("Add meg az 'a' befogó méretét: ")))
            b: float = float(check_inputs(input("Add meg a 'b' befogó méretét: ")))
        except TypeError:
            continue
        
        triangle_: triangle.Triangle = triangle.Triangle(a, b)
        print(f"Kerület: {triangle_.get_kerulet_rounded()}")
        triangle.add(triangle_)
else: # GUI használata
    import gui
    gui.gui_open()