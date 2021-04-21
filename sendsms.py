import requests
# Only needed when sending a scheduled sms at a specific date and time
# import datetime


def send_sms():
    base_url = 'https://api.sipgate.com/v2'
    tokenId = 'YOUR_SIPGATE_TOKEN_ID'
    token = 'YOUR_SIPGATE_TOKEN'

    sms_id = 'YOUR_SIPGATE_SMS_EXTENSION'

    message = 'YOUR_MESSAGE'
    recipient = 'RECIPIENT_PHONE_NUMBER'

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
