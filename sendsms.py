import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
# Only needed when sending a scheduled sms at a specific date and time
# import datetime

load_dotenv()

token = os.environ.get("token")
tokenId = os.environ.get("tokenId")
sms_id = os.environ.get("sms_id")
recipient = os.environ.get("recipient")

def send_sms():
    base_url = 'https://api.sipgate.com/v2'

    message = 'YOUR_MESSAGE'

    # Only needed when sending a scheduled sms at a specific date and time
    # send_at = datetime.datetime(day=9, month=4, year=2019, hour=15, minute=35)

    headers = {
        'Content-Type': 'application/json'
    }

    request_body = {
        'smsId': sms_id,
        'recipient': recipient,
        'message': message,
        # Only needed when sending a scheduled sms at a specific date and time
        # 'sendAt': send_at.timestamp()
    }

    response = requests.post(
        base_url + '/sessions/sms',
        headers=headers,
        auth=requests.auth.HTTPBasicAuth(tokenId, token),
        json=request_body
    )

    print('Status:', response.status_code)
    print('Body:', response.content.decode("utf-8"))


if __name__ == "__main__":
    send_sms()
