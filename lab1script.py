import requests
url = "https://raw.githubusercontent.com/filippociandy10/404lab1/main/lab1script.py"
r = requests.get(url)
print(r.content)
# print(requests.get("https://www.google.com").text)