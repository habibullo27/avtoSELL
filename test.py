import requests

login = input("Введите логин: ")
password = input("Введите пароль: ")

api_url = "http://127.0.0.1:8000"

login_url = api_url + "/user/login"
response = requests.post(url=login_url,
                         json={"identificator": login,
                               "password": password})
print(f"ответ запроса: {response.json()}")


