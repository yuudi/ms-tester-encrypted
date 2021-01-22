import os
import sys

import requests

import encrypt

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
aes_key = os.environ['AES_KEY']

if client_id and client_secret and aes_key:
    print('read virables from environment')
else:
    print('the environment are not set correctly')
    sys.exit(1)

apiroot = 'https://graph.microsoft.com/v1.0'
endpoints = [
    '/me/drive/root',
    '/me/drive',
    '/drive/root',
    '/users',
    '/me/messages',
    '/me/mailFolders/inbox/messageRules',
    '/me/mailFolders/Inbox/messages/delta',
    '/me/drive/root/children',
    '/me/mailFolders',
    '/me/outlook/masterCategories',
]


def get_access_token():
    refresh_token = encrypt.load(aes_key)
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': 'http://localhost:53682/'
    }
    req = requests.post(
        'https://login.microsoftonline.com/common/oauth2/v2.0/token',
        data=data,
    )
    body = req.json()
    if body.get('error'):
        print(body)
        sys.exit(1)
    new_refresh_token = body['refresh_token']
    encrypt.save(new_refresh_token, aes_key)
    return body['access_token']


def main():
    access_token = get_access_token()
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    for endpoint in endpoints:
        try:
            res = requests.get(apiroot+endpoint, headers=headers)
            if res.status_code == 200:
                print(f'call {endpoint} successed')
            else:
                print(f'::error::call {endpoint} failed')  # github action error format
                print(f'call {endpoint} failed')
                print(res.text)
        except Exception as e:
            print(f'::error::call {endpoint} exception catched')  # github action error format
            print(f'call {endpoint} exception catched')
            print(e)

main()
