import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '18aeed4cbe5d0105088906e0a3c6e53f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6665'

def test_status_code():
    response = requests.get(url = f'{URL}/poremons',params = {'trainer_id' : TRAINER_ID})
assert response.status_code == 200
