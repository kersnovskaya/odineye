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
        send_to_telegram('API Pay не отвечает!', '6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588', '-1001820930885')


def test_check_site():
    url = 'https://site-api.bezlimit.ru/v1/phones'
    headers = {
        'accept': 'application/json',
        'authorization': 'Basic c2l0ZS1hcGktcHJvZDpKQ2E3dndVMThEaVJHVjBV'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        send_to_telegram('API Site не отвечает!', '6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588', '-1001820930885')


def test_check_store():
    url = 'https://api.store.bezlimit.ru/v2/super-link/addresses'
    headers = {
        'accept': 'application/json',
        'authorization': 'Basic YXBpU3RvcmU6VkZ6WFdOSmhwNTVtc3JmQXV1dU0zVHBtcnFTRw=='
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        send_to_telegram('API Store не отвечает!', '6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588', '-1001820930885')


def test_check_lk():
    url = 'https://api.lk.bezlimit.ru/v1/system/translates'
    headers = {
        'accept': 'application/json',
        'authorization': 'Base bGstYXBpLXByb2Q6cFdDbTZzWUxMMWpKamUySA=='
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        send_to_telegram('API LK не отвечает!', '6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588', '-1001820930885')


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
        send_to_telegram('API Insurance не отвечает!', '6076174980:AAGxe5VXrRpSvoEvbdrCPfmA3_By7TM0588', '-1001820930885')
