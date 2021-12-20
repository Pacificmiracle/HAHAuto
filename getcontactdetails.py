import requests
# from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth2

code = requests.post("http://18.136.220.168:1000/api/", auth=OAuth2(client_id=r'3', client_secret=
r'TJGBPvHd6Zd2vmDR8DpwUZfXcAiOX5SuzHabS7ZO',username='sabin.maharjan@logicabeans.com',
password='abcdqwerty'))
resp = requests.get("http://18.136.220.168:1000/api/contact-us")
print(resp)
json_response = resp.json()
print(resp.json())
print(resp.headers.get("Content-Type"))
