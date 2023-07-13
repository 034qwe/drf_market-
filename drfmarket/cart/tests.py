from django.test import TestCase


import requests

TOKEN = '6068566463:AAGzmuIKI5CWjgld7jh0_QhYJFkv5MJ2IxE'

def send_notification_to_telegram(chat_id):
    

    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())


def trytoken():
    url = f" https://api.telegram.org/bot{TOKEN}/getUpdates "
    print(requests.get(url).json())

    
# send_notification_to_telegram(chat_id=5512193079)
