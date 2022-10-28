import requests

url = "https://mca-api.issart.com/auth/token/login"

payload='username=rodion&password=12345678'
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
