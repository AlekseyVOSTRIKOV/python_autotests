import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='273b07238da04932d286473b9ab3aa5a'
HEADER={'Content-type':'application/json','trainer_token' : TOKEN}

body_registration={
    "trainer_token": TOKEN,
    "email":"eshka87@mail.ru",
    "password": "Vostrik5571346"
}

'''response=requests.post(url=f'{URL}/trainers/reg',headers=HEADER,json=body_registration)
print(response.text)'''

body_confirmation={

    "trainer_token": TOKEN
}

body_create={
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change={
    "pokemon_id": "189029",
    "name": "New Name",
    "photo_id": 211
}

body_add_pokeball={
    "pokemon_id": "189029"
}

'''response=requests.post(url= f'){URL}/trainers/reg',headers=HEADER,json=body_registration)
print(response_confirmation.text)'''

'''response_confirmation=requests.post(url= f'){URL}/trainers/confirm_email',headers=HEADER,json=body_confirmation)
print(response_confirmation.text)'''

'''response_create=requests.post(url= f'{URL}/pokemons',headers=HEADER,json=body_create)
print(response_create.text)'''

'''response_change=requests.put(url= f'{URL}/pokemons',headers=HEADER,json=body_change)
print(response_change.text)'''

response_add_pokeball=requests.post(url= f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_add_pokeball)
print(response_add_pokeball.text)


pokemon_id=response_add_pokeball.json()['id']