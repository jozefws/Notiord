import requests
import constants

def getDatabase(message, dbid):

    if(dbid == "" or message == ""):
        raise Exception("Missing Database ID or Discord Message in getDatabase")
    else:
        databaseid = dbid
        url = 'https://api.notion.com/v1/databases/'
        headers={
            'Authorization': 'Bearer ' + constants.NOTION_API_KEY,
            'Notion-Version': '2021-07-27',
        }
        data = {
            "parent": {"type": "Workspace", "workspace": "true"},
            "title":[{
                "type": "text",
                "text": {
                    "content": "Aleds mam",
                    "link": ""
                }
            }],
            "properties": {
                "Name": {
                    "title": {}
                },
                "Description": {
                    "rich_text": {}
                },
                "In stock": {
                    "checkbox": {}
                },
                "Food group": {
                    "select": {
                        "options": [
                            {
                                "name": "🥦Vegetable",
                                "color": "green"
                            },
                            {
                                "name": "🍎Fruit",
                                "color": "red"
                            },
                            {
                                "name": "💪Protein",
                                "color": "yellow"
                            }
                        ]
                    }
                }
            }
        }
        resp = requests.get(url, headers=headers, data=data)
        if(resp.status_code == 200):
            return resp.content
        else:
            raise Exception("Could not connect to database, error code: " + str(resp.status_code) + " \nContent:  ```" + str(resp.content) + "```")
             
