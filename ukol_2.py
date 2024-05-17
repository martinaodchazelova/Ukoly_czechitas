import requests
import json

kocky_fakta_api = requests.get('https://cat-fact.herokuapp.com/facts')
info_o_kockach = kocky_fakta_api.json() 
print(info_o_kockach)

seznam_faktu_o_kockach = []

for fakt in info_o_kockach:
    #získání textu:
    text_faktu = fakt['text']
    # Přidání textu faktu do seznamu
    seznam_faktu_o_kockach.append(text_faktu)

# for text_faktu in seznam_faktu_o_kockach:
#     print(text_faktu)

print(seznam_faktu_o_kockach)

cislovani = 1
ocislovany_seznam_faktu_o_kockach = []

for text_faktu in seznam_faktu_o_kockach:
    ocislovany_fakt = f"{cislovani}. {text_faktu}"
    ocislovany_seznam_faktu_o_kockach.append(ocislovany_fakt)
    cislovani += 1

print(ocislovany_seznam_faktu_o_kockach)

# Výpis očíslovaného seznamu faktů
# for fakt in ocislovany_seznam_faktu_o_kockach:
#     print(fakt)


