#round_tizedesjegy: int = 3
keruletek: dict[float, int] = {}

def set_round(round: int):
    global round_tizedesjegy
    round_tizedesjegy = round

def disable_round():
    global round_tizedesjegy
    round_tizedesjegy = -1

# Felvétel a dictionarybe
def add(triangle):
    key: float = triangle.get_kerulet_rounded()
    if not key in keruletek:
        keruletek[key] = 0
    keruletek[key] += 1

def get_keruletek():
    return keruletek

def get_keruletek_sorted():
    return dict(sorted(keruletek.items(), key = lambda item: -item[1]))

class Triangle:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def get_atfogo(self) -> float:
        return (self.a**2 + self.b**2) ** 0.5
    
    def get_kerulet(self):
        return self.a + self.b + self.get_atfogo()
    
    def get_kerulet_rounded(self):
        if round_tizedesjegy == -1:
            return self.a + self.b + self.get_atfogo()
        
        return round(self.a + self.b + self.get_atfogo(), 0 if round_tizedesjegy < 0 else round_tizedesjegy)

    def is_pitagoraszi_szamharmas(self):
        return self.get_atfogo() % 1 == 0
