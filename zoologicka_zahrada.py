# Trida Zvire
class Zvire:
    def __init__(self, jmeno:str, druh:str, vaha:int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self):
        return f'{self.jmeno} je {self.druh} a váží {self.vaha}kg.'
    
    def export_to_dict(self):
        return {
            'jmeno': self.jmeno,
            'druh': self.druh,
            'vaha': self.vaha
        }
    
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
pavouk_export = pavouk.export_to_dict()
assert pavouk_export['jmeno'] == 'Adolf'
assert pavouk_export['druh'] == 'Tarantule Velká'
assert pavouk_export['vaha'] == 0.1

# print(pavouk)
# print(pavouk_export)

zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

zvirata_list = []
for z in zvirata_dict:
    zvire = Zvire(z['jmeno'], z['druh'], z['vaha'])
    zvirata_list.append(zvire)

# kontrolni funkce pro vytisknutí listu zvirata:
def vytisknout_zvirata(seznam_zvirat):
    for jedno_zvire in seznam_zvirat:
        print(jedno_zvire)
vytisknout_zvirata(zvirata_list)

# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}


# Trida Zamestnanec
class Zamestnanec:
    def __init__(self, cele_jmeno:str, rocni_plat:int, pozice:str):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice
    
    def __str__(self):
        return f'{self.cele_jmeno} má roční plat {self.rocni_plat}Kč jako {self.pozice}.'

    def ziskej_inicialy(self):
        rozdelena_jmena = self.cele_jmeno.split()
        inicialy = (rozdelena_jmena[0][0].upper()) + '.' + (rozdelena_jmena[1][0].upper())+ '.'
        return inicialy


zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

zamestnanci_list = []
for z_l in zamestnanci_dict:
    jeden_zamestnanec = Zamestnanec(z_l['cele_jmeno'], z_l['rocni_plat'], z_l['pozice'])
    zamestnanci_list.append(jeden_zamestnanec)

# kontrolni funkce pro vytisknutí listu zamestnanci_list:
def vytisknout_zamestnance(seznam_zam):
    for jeden_zam_ze_seznamu in seznam_zam:
        print(jeden_zam_ze_seznamu)
vytisknout_zamestnance(zamestnanci_list)

# kontrolni asserty a printy u Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'
print(zamestnanec)
print(zamestnanec.ziskej_inicialy())

# Trida Reditel
class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno:str, rocni_plat:int, oblibene_zvire: Zvire):
        super().__init__(cele_jmeno,rocni_plat, 'Reditel')
        self.oblibene_zvire = oblibene_zvire

    def __str__(self):
        return super().__str__() + f' Jeho oblibené zvíře je {self.oblibene_zvire.druh}.'

# Priklad vytvoreni objektu (klidne zkopiruj)
zvire = Zvire('Láďa', 'Koala', 150)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)
print(reditel)

# Trida ZOO
class Zoo:
    def __init__(self, jmeno:str, adresa:str, reditel: Reditel, zamestnanci: list[Zamestnanec], zvirata: list[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

    def vaha_vsech_zvirat_v_zoo(self):
        vaha = int
        vaha = sum(zvire.vaha for zvire in self.zvirata)
        return vaha

    def mesicni_naklady_na_zamestnance(self):
        mzdy = sum(zamestnanec.rocni_plat for zamestnanec in self.zamestnanci)
        celkove_mzdy = mzdy + self.reditel.rocni_plat
        mesicni_celkove_mzdy = celkove_mzdy / 12
        return mesicni_celkove_mzdy

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci_list, zvirata_list)
print(zoo)
print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.jmeno, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
assert zoo.vaha_vsech_zvirat_v_zoo() == 150
assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12
