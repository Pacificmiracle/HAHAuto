import requests
import json

payload = {
  "email": "prashant.test1@yopmail.com",
  "full_name": "Prashant",
  "message": "Hello this is message from Automated API Test. The information provided should not be relied upon "
             "NEW Line Message",
  "mobile": "9801880297"
}


# print(type(payload))
resp = requests.post("http://18.136.220.168:1000/api/contact-us", data=payload)
print(resp)
print(resp.json())
# assert (resp.json())["mobile"] == "9801880297"
print(resp.headers.get("Content-Type"))
