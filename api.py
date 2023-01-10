import requests

response = requests.get("https://github.com/purnimakumarirai")
print(response.text)
print(type(response.text))
#request to git
