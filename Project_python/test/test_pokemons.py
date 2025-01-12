import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='273b07238da04932d286473b9ab3aa5a'
HEADER={'Content-type':'application/json','trainer_token' : TOKEN}
TRAINER_ID='25592'

def test_status_code():
    response=requests.get(url= f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response.status_code==200

def test_part_of_response():
    response_get=requests.get(url= f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"]=="Бульбазавр"

def test_part_of_respons():
    response_get=requests.get(url= f'{URL}/me', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"]=="Брооо"

@pytest.mark.parametrize('key,value', [('name','Бульбазавр'),('trainer_id',TRAINER_ID),('id','189035')])

def test_parametrize(key,value):
    response_parametrize=requests.get(url= f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key]==value