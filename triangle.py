round_tizedesjegy: int = 3
keruletek: dict[float, int] = {}

# Felvétel a dictionarybe
def add(triangle) -> None:
    key: float = triangle.get_kerulet_rounded()
    if not key in keruletek:
        keruletek[key] = 0
    keruletek[key] += 1

def get_keruletek() -> dict[float, int]:
    return keruletek

def get_keruletek_sorted() -> dict[float, int]:
    return dict(sorted(keruletek.items(), key = lambda item: -item[1]))

class Triangle:
    def __init__(self, a: float, b: float):
        self.a: float = a
        self.b: float = b

    def get_atfogo(self) -> float:
        return (self.a**2 + self.b**2) ** 0.5
    
    def get_kerulet(self) -> float:
        return self.a + self.b + self.get_atfogo()
    
    def get_kerulet_rounded(self) -> float:
        if round_tizedesjegy == -1:
            return self.get_kerulet()
        
        return round(self.a + self.b + self.get_atfogo(), 0 if round_tizedesjegy < 0 else round_tizedesjegy)

    def is_pitagoraszi_szamharmas(self) -> bool:
        return self.get_atfogo() % 1 == 0