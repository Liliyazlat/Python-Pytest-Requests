import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '18aeed4cbe5d0105088906e0a3c6e53f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "liliya11samira@gmail.com",
    "password": "@Ramil24Samira"
}
body_confirmation = {
   "trainer_token": TOKEN,
}

body_create = {
    "name": "Zorro",
     "photo_id": 92
}

body_rename = {
    "pokemon_id": "45473",
    "name": "Zorrito",
    "photo_id": 94
}
body_catch = {
    "pokemon_id": "45473"
}


''' response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)