def ziskaj_znamku(pocet_bodov, max_bodov=30):
    percento = (pocet_bodov / max_bodov) * 100

    if percento >= 90:
        znamka = 'vynikajúci'
    elif percento >= 80:
        znamka = 'výborný'
    elif percento >= 70:
        znamka = 'dobrý'
    elif percento >= 60:
        znamka = 'dostatočný'
    else:
        znamka = 'nedostatočný'

    return znamka, percento

pocet_bodov = int(input("Zadaj počet bodov koľko si dostal: "))
znamka, percento = ziskaj_znamku(pocet_bodov)

print(f"Tvoja známka je: {round(percento, 2)}")
