import requests
import json


# url = "https://free-nba.p.rapidapi.com/stats"

# querystring = {"page":"0","per_page":"100","player_ids":"1043"}

# headers = {
#     'x-rapidapi-key': "59aba308e6msh85019965c5ae5aap1e13cbjsn114e29b1e51c",
#     'x-rapidapi-host': "free-nba.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)



headers = {
    'x-rapidapi-key': "59aba308e6msh85019965c5ae5aap1e13cbjsn114e29b1e51c",
    'x-rapidapi-host': "free-nba.p.rapidapi.com"
    }

page=1
results = []
while True:

    url = "https://free-nba.p.rapidapi.com/stats"

    querystring = {"page":page,"per_page":"100","player_ids":"1043"}
    response = requests.request("GET", url, headers=headers, params = querystring)

    if response.status_code != 200:
        continue

    data = response.json()
    
    if len(data['data']) <= 0:
        break

    print(data.get('meta', None))
    results += data['data']
    
    page += 1

    # print(response.json())


with open("data.json", "w") as data_file: 
    json.dump(results, data_file, indent=2)
    data_file.close()