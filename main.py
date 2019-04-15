import requests
import datetime


def main():
	baseURL = 'https://api.sipgate.com/v2'
	username = 'YOUR_SIPGATE_EMAIL'
	password = 'YOUR_SIPGATE_PASSWORD'

	smsId = 'YOUR_SIPGATE_SMS_EXTENSION'

	message = 'YOUR_MESSAGE'
	recipient = 'RECIPIENT_PHONE_NUMBER'

	# Only needed when sending a scheduled sms at a specific date and time
	# sendAt = datetime.datetime(day=9, month=4, year=2019, hour=15, minute=35)

	headers = {
		'Content-Type': 'application/json'
	}

	requestBody = {
		'smsId': smsId,
		'recipient': recipient,
		'message': message,
		# Only needed when sending a scheduled sms at a specific date and time
		# 'sendAt': sendAt.timestamp()
	}

	response = requests.post(
		f'{baseURL}/sessions/sms',
		headers=headers,
		auth=requests.auth.HTTPBasicAuth(username, password),
		json=requestBody
	)

	print(f'Status: {response.status_code}')
	print(f'Body: {response.content.decode("utf-8")}')


if __name__ == "__main__":
	main()
