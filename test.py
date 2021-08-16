import requests
url = 'https://api.notion.com/v1/databases'  
headers={'Authorization': 'Bearer "secret_3QBnug0Ol1rc2zwirDm4wpPhrbiLxvruAzjek2rmH6U"','Notion-Version': '2021-07-27'}
print('Cum 1')
resp = requests.get(url, headers=headers)
print(resp.status_code)