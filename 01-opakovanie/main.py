import random

teplota = [random.randint(15, 40) for _ in range(30)]

najmensia_teplota = min(teplota)
najchladnejsi_den = teplota.index(najmensia_teplota) 

najvacsia_teplota = max(teplota)
najhorucejsi_den = teplota.index(najvacsia_teplota)  

priemerna_teplota = sum(teplota) / len(teplota)

nadpriemerne_dni = [i + 1 for i, t in enumerate(teplota) if t > priemerna_teplota]
podpriemerne_dni = [i + 1 for i, t in enumerate(teplota) if t < priemerna_teplota]

print("Teplota za 30 dní:")
for den, t in enumerate(teplota, start=1):
    print(f"Deň {den}: {t}°C")

print(f"Najmenšia teplota bola {najmensia_teplota}°C v {najchladnejsi_den}. dni.")
print(f"Najväčšia teplota bola {najvacsia_teplota}°C v {najhorucejsi_den}. dni.")
print(f"Priemerná teplota bola {priemerna_teplota:.2f}°C.")

if nadpriemerne_dni:
    print(f"Nadpriemerné teploty boli v dňoch: {', '.join(map(str, nadpriemerne_dni))}.")
else:
    print("Neboli dni s nadpriemernou teplotou.")

if podpriemerne_dni:
    print(f"Podpriemerné teploty boli v dňoch: {', '.join(map(str, podpriemerne_dni))}.")
else:
    print("Neboli dni s podpriemernou teplotou.")
