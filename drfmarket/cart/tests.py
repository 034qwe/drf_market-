from django.test import TestCase


import requests



def send_notification_to_telegram(chat_id):
    TOKEN = '6068566463:AAGzmuIKI5CWjgld7jh0_QhYJFkv5MJ2IxE'

    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())


    
# send_notification_to_telegram(chat_id=5512193079)

# send_notification_to_telegram(telegram_user=order.user)