print("Lista zakupow: ")

lista_zakupow = {
    'piekarnia': ['chleb', 'bułki', 'paczek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

new_list = {k.title():[s.capitalize() for s in v] for k,v in lista_zakupow.items()}
for k, v in new_list.items():
    print(f"Idę do {k}, kupuję tu następujące rzeczy: {v}.")
    
total_items = len(lista_zakupow['piekarnia']) + len(lista_zakupow['warzywniak'])
print(f'W sumie w koszyku mam {total_items} produktow. I ide do kasy...')
