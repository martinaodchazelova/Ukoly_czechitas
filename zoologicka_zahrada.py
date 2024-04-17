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