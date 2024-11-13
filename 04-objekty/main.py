import datetime

class osoba:
    def __init__(self,meno,priezvisko,rok): # konstrukcia ktora sa spusti pri vytvoreni objektu 
        self.meno = meno 
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok
    
    def pozdrav(self):
        print(F"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek}rokov")

class Student(osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno,priezvisko,rok)
        self.trieda = trieda

    def pozdrav(self):
        osoba.pozdrav(self)
        print(f"Som študent {self.trieda} triedy")   

class Ucitel(osoba):
    def __init__(self, meno, priezvisko, rok, titul="", trieda=""):
        super().__init__(meno, priezvisko, rok)
        self.titul = titul
        self.trieda = trieda
    def pozdrav(self):
        print(f"Dobry den, volam sa  {self.titul} {self.meno} {self.priezvisko} a mam {self.vek} ")
        if self.trieda != "":
            print(f"som triedny ucitel {self.trieda} triede")

jano = osoba("Jano","Kanak",2000)
jano.pozdrav()
jano = osoba("Fero","Lakatos",2000)
jano.pozdrav()
ondrej = Student("Ondrej", "Šarlina", 2007, "3.AT")
ondrej.pozdrav()

sutek = Ucitel("MIchal", "Sutek", 1978,"Mgr","3.AT")
palica = Ucitel("MIchal", "Palica", 1985)
sutek.pozdrav()
palica.pozdrav()
