def delitele(n):
    delitele = [i for i in range(1, n + 1) if n % i == 0]
    return delitele

def jePrvocislo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prvocislaMensieNez(n):
    prvocisla = [i for i in range(2, n) if jePrvocislo(i)]
    return prvocisla


cislo = int(input("Zadaj cislo: "))

delitele = delitele(cislo)
print(f"Delitele cisla {cislo}: {delitele}")

if jePrvocislo(cislo):
    print(f"{cislo} je prvocislo.")
else:
    print(f"{cislo} nie je prvocislo.")


prvocisla = prvocislaMensieNez(cislo)
print(f"Prvocisla mensie nez cislo {cislo}: {prvocisla}")
