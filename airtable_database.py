from datetime import datetime
import requests

from config import AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY

AIRTABLE_BASE_ID = AIRTABLE_BASE_ID
AIRTABLE_TABLE_NAME = AIRTABLE_TABLE_NAME
AIRTABLE_API_KEY = AIRTABLE_API_KEY

url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

logins = set()

data = {
    "records":
        [
            {
                "fields": {
                    "username": "1w",
                    "login": "2w",
                    "password": "3w",
                    "telegramID": "4w",
                    "telegramlink": "5w",
                    "regdate": ""
                }
            }
        ]
}


def post_data(username, login, password, user_id, link):
    global data
    s = data['records'][0]['fields']
    s['username'] = username
    s['login'] = login
    s['password'] = password
    s['telegramID'] = user_id
    s['telegramlink'] = link
    s['regdate'] = datetime.today().strftime('%Y-%m-%d')
    requests.post(url, json=data, headers=headers)
