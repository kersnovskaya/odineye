import requests

def send_to_telegram(text, token, chat):
    url = "https://api.telegram.org/bot" + token + "/sendMessage"  # 1388568494:AAFZCASLFx64WZnpQLyqmBjht66Y3LU9xEI 5156460237:AAEt1if6meaEGae-8lVWp20Egj4TnBdDdEs

    payload = {
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "chat_id": chat
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

def check_site(url):
    try:
        response = requests.get(url)
        print(response.status_code, response.content)
        # Проверяем, что код ответа равен 200
        if response.status_code != 200:
            return False
    except:
        # В случае ошибки также возвращаем False
        return False

    return True


# Список сайтов, которые нужно проверять
sites = [
    'https://bezlimit.ru',
    'https://bbezlimit.ru',
    'https://store-old.bezlimit.ru',
    'https://store.bezlimit.ru',
    'https://lk.bezlimit.ru'
]

for site in sites:
    if not check_site(site):
        # Отправляем сообщение на телеграм в случае ошибки
        send_to_telegram(f'Ошибка на сайте {site}', '6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588', '-1001820930885')
