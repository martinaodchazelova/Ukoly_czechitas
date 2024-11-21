import sys
import requests
import json

# Spravne reseni!
# Dekuji za vcasne odevzdani.
# K zamysleni:
#   - Ktere hodnoty v kodu by bylo vhodne definovat jako konstanty?
#   - Seznam prochazime dvakrat (1. vytazeni 'text', 2. ocislovani); dalo by se zaridit, aby byl pruchod seznamem jen jeden?
#   - Pro ocislovani by bylo vhodne pouzit enumerate().

try:
    kocky_fakta_api = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=5)
    info_o_kockach = kocky_fakta_api.json() 
except requests.exceptions.Timeout:
    print(f'Jste příliš nedočkaví.')
    # V pripade, ze dojde k vyjimce a my vypiseme chybove hlaseni,
    # zrejme nechceme pokracovat s kodem nize; dostaneme:
    #   NameError: name 'info_o_kockach' is not defined
    # Proto program radsi ukoncime.
    sys.exit(1)


seznam_faktu_o_kockach = []

for fakt in info_o_kockach:
    # Získání textu:
    text_faktu = fakt['text']
    # Přidání textu faktu do seznamu
    seznam_faktu_o_kockach.append(text_faktu)

cislovani = 1
ocislovany_seznam_faktu_o_kockach = []

for text_faktu in seznam_faktu_o_kockach:
    ocislovany_fakt = f"{cislovani}. {text_faktu}"
    ocislovany_seznam_faktu_o_kockach.append(ocislovany_fakt)
    cislovani += 1
    # Podminka neni nutna. Seznam by mel mit delku 10 a i kdyby byl delsi,
    # pak je asi lepsi ocislovat ho cely.
    # if cislovani > 10:
    #     break

print(ocislovany_seznam_faktu_o_kockach)

with open('kocici_fakta.json', mode= 'w', encoding='utf-8') as output_file:
    json.dump(ocislovany_seznam_faktu_o_kockach, output_file, indent=4, ensure_ascii=False)