import requests

url = "https://reqres.in/api/users"
payload = {"name": "Alice", "job": "Engineer"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print("Status code:", response.status_code)
print("Response body:", response.text)
