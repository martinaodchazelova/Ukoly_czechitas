import requests
import json

try:
#kocky_fakta_api = requests.get('https://cat-fact.herokuapp.com/facts')
# endpoint: requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10')
    kocky_fakta_api = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout = 0.3)
    info_o_kockach = kocky_fakta_api.json() 
    print(info_o_kockach)
except requests.exceptions.Timeout: #HTTPSConnectionPool(host='cat-fact.herokuapp.com', port=443): 
    print(f'Jste přílič nedočkaví.')

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
    if cislovani > 10:
        break 

print(ocislovany_seznam_faktu_o_kockach)

with open ('kocici_fakta.json', mode= 'w', encoding='utf-8') as output_file:
    json.dump(ocislovany_seznam_faktu_o_kockach, output_file, indent=4,ensure_ascii=False)