#Handle the auth tokens
import requests
from app.secret_token import token

url = "https://www.warcraftlogs.com/api/v2/client"

headers = {
    'Authorization' : f'Bearer {token}'
}

query = '''query gameData {
	gameData {
		ability(id: 115310){name,icon}
	}
}'''

data = {
    'query' : query
}
response = requests.get(url, headers=headers, json=data)