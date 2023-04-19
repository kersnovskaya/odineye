import requests
import telebot

bot = telebot.TeleBot('6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588')


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
        bot.send_message('-1001820930885', f'Ошибка на сайте {site}')
