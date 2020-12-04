import requests

endpoint = cx_local.get_api("text-generator")["endpoint"]
payload = {"text": "hello world"}
print(requests.post(endpoint, payload).text)
