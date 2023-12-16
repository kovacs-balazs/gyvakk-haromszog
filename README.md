# Háromszög kerület kalkulátor

A szoftver a felhasználó által megadott [derékszögű háromszögek](https://hu.wikipedia.org/wiki/Der%C3%A9ksz%C3%B6g%C5%B1_h%C3%A1romsz%C3%B6g) két befogójának hosszából kiszámolja az átfogót, a [Pitagorasz-tétel](https://hu.wikipedia.org/wiki/Pitagorasz-t%C3%A9tel) alkalmazásával. A kapott eredménnyel tovább számolva a háromszög kerületét egy szótárban tárolja három tizedesjegyre kerekítve. A kalkulátor mértékegység független, és támogatja mind a grafikus, mind a konzolos bemeneteket. Az összegyűjtött kerületeket kiíratáskor mindig a gyakoriság szerint csökkenő sorrendben írja ki.

## Használat

### Grafikus Felhasználói Felület
#### Indítóparancs:
```
python main.py
```
</br>
A szoftver elindítása után a megnyíló grafikus felületben kell megadni a két befogó hosszúságát. A bemeneti szövegekhez csak számok írhatóak. A "Felvétel" gombra kattintva felveszi a szótárba a háromszög kerületét. A "Listázás" gombra kattintva kiírja a háromszögek kerületeinek szótárát.

### Konzol
#### Indítóparancs:
```
python main.py --nogui
```
</br>
A szoftver elindítása után először meg kell adni az 'a' befogó, majd a 'b' befogó hosszát. A program a háromszög kerületét kiírja a konzolba, és rögzíti a szótárba. Továbbiakban a bemenetekhez olyan parancsokat írhatóak, amelyek a megadott eseménysort fogják végrehajtani.

**Bemenetekhez írható parancsok:**

| Parancs | Esemény |
| :-------: | :-------: |
| `exit` | Program megállítása |
| `list` | Felvett kerületek kilistázása |

## Beállítások

Az indítóparancs utáni argumentumok segítségével egyszerűen konfigurálhatóak a szoftver beállításai. Több argumentum is megadható egyszerre az indítóparancsban. A kerekítés kikapcsolása felülírja a kerekítési értéket, így nem ajánlott egyszerre mindkét argumentum használata.

| Argumentum | Beállítás | Példa |
| :---: | :---: | :---: |
| `--nogui` | Konzol használata | `python main.py --nogui` |
| `--noround` | Kerekítés kikapcsolása | `python main.py --noround` |
| `--round <szám>` | Kerekítési érték beállítása | `python main.py --round 5` |

**További példák:**
```
python main.py --nogui -noround
python main.py --nogui --round 2
python main.py --noround
python main.py --round 4
```

