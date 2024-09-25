def je_parne(cislo):
    return cislo % 2 == 0

def main():
    cislo1 = float(input("Zadaj prvé číslo: "))
    cislo2 = float(input("Zadaj druhé číslo: "))

    sucet = cislo1 + cislo2
    rozdiel = cislo1 - cislo2
    soucin = cislo1 * cislo2
    podiel = cislo1 / cislo2 if cislo2 != 0 else "Nedefinované (deliteľstvo nulou)"

    print(f"Súčet: {sucet}")
    print(f"Rozdiel: {rozdiel}")
    print(f"Súčin: {soucin}")
    print(f"Podiel: {podiel}")

    for cislo in [cislo1, cislo2]:
        if je_parne(cislo):
            print(f"{cislo} je párne.")
        else:
            print(f"{cislo} je nepárne.")

if __name__ == "__main__":
    main()
