import requests
import telebot

bot = telebot.TeleBot('6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588')

methods = {
    'https://api.store.bezlimit.ru/v2/super-link/addresses': ['YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw==', ''],
    'https://api.lk.bezlimit.ru/v1/system/translates': ['bGstYXBpLXByb2Q6cFdDbTZzWUxMMWpKamUySA==', ''],
    'https://api-insure.bezlimit.ru/v1/': ['', ''],
    'https://pay.bezlimit.ru/v1/': ['cGF5LXByb2Q6ZER3azJUQWlUQTVmY0ZsYg==', ''],
    'https://site-api.bezlimit.ru/v1/phones': ['c2l0ZS1hcGktcHJvZDpKQ2E3dndVMThEaVJHVjBV', '']
}


def test_check_pay():
    url = 'https://pay.bezlimit.ru/v1/payment/fail'
    headers = {
        'accept': '*/*',
        'authorization': 'Base cGF5LXByb2Q6ZER3azJUQWlUQTVmY0ZsYg=='
    }
    response = requests.get(url=url, headers=headers)
    if response.json() != {
                      "name": "PaymentAcceptanceError",
                      "message": "Платёж не принят",
                      "code": 0,
                      "status": 402
                    }:
        bot.send_message('-1001820930885', 'API Pay не отвечает!')


def test_check_site():
    url = 'https://site-api.bezlimit.ru/v1/phones'
    headers = {
        'accept': 'application/json',
        'authorization': 'Basic c2l0ZS1hcGktcHJvZDpKQ2E3dndVMThEaVJHVjBV'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        bot.send_message('-1001820930885', 'API Site не отвечает!')


def test_check_store():
    url = 'https://api.store.bezlimit.ru/v2/super-link/addresses'
    headers = {
        'accept': 'application/json',
        'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw=='
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        bot.send_message('-1001820930885', 'API Store не отвечает!')


def test_check_lk():
    url = 'https://api.lk.bezlimit.ru/v1/system/translates'
    headers = {
        'accept': 'application/json',
        'authorization': 'Base bGstYXBpLXByb2Q6cFdDbTZzWUxMMWpKamUySA=='
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        bot.send_message('-1001820930885', 'API LK не отвечает!')


def test_check_ins():
    url = 'https://api-insure.bezlimit.ru/v1/users/login'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'login': 'autotest',
        'password': 'QualityAssurance'
    }
    response = requests.post(url=url, headers=headers, data=data)
    if response.status_code != 200:
        bot.send_message('-1001820930885', 'API Insurance не отвечает!')
