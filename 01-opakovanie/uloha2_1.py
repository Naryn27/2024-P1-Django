max_bodov = 30

# funkcia na ziskanie validneho poctu bodov
def ziskaj_pocet_bodov():
    while True: # nekonecny cyklus
        try:
            pocet_bodov = int (input(f"zadaj pocet bodov (0 - {max_bodov})"))
            if 0 <= pocet_bodov <=max_bodov:
                return pocet_bodov
            else:
                print(f"pocet bodov musi byt v rozsahu 0 po {max_bodov}. daj este raz!")
        except ValueError:
            print("neplatny vstup zadaj cele cislo")

def vypocitaj_percenta(pocet_bodov):
    return (pocet_bodov / max_bodov) * 100

def klasifikacia(percenta):
    if percenta >= 90:
        return 'vynikajúci'
    elif percenta >= 80:
        return  'výborný'
    elif percenta >= 70:
        return 'dobrý'
    elif percenta >= 60:
        return 'dostatočný'
    else:
        return 'nedostatočný'

pocet_bodov = ziskaj_pocet_bodov()
percenta = vypocitaj_percenta(pocet_bodov)
hodnotenie = klasifikacia(percenta)

print(f"pocet bodov: {pocet_bodov}, percenta {percenta}%, hodnotenie: {hodnotenie}")02