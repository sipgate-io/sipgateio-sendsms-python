<img src="https://www.sipgatedesign.com/wp-content/uploads/wort-bildmarke_positiv_2x.jpg" alt="sipgate logo" title="sipgate" align="right" height="112" width="200"/>

# sipgate.io python send sms example

To demonstrate how to send an SMS, we queried the `/sessions/sms` endpoint of the sipgate REST API.

For further information regarding the sipgate REST API please visit https://api.sipgate.com/v2/doc

### Prerequisites

- python3
- pip3

### How To Use

Install dependencies:

```bash
$ pip3 install -r requirements.txt
```

In order to run the code you have to set the following variables in [main.py](./main.py):

```python
username = 'YOUR_SIPGATE_EMAIL'
password = 'YOUR_SIPGATE_PASSWORD'

smsId = 'YOUR_SIPGATE_SMS_EXTENSION'

message = 'YOUR_MESSAGE'
recipient = 'RECIPIENT_PHONE_NUMBER'
```

The `smsId` uniquely identifies the extension from which you wish to send your message. Further explanation is given in the section [Web SMS Extensions](#web-sms-extensions).

> **Optional:**
> In order to send a delayed message uncomment the following line and set the desired date and time in the future (up to one month):
>
> ```python
> sendAt = datetime.datetime(day=24, month=7, year=2001, hour=13, minute=37)
> ```
>
> Additionally, in the `requestBody` object uncomment the `sendAt` property.
>
> ```python
> requestBody = {
> 	'smsId': smsId,
> 	'recipient': recipient,
> 	'message': message,
> 	'sendAt': sendAt.timestamp()
> }
> ```
>
> **Note:** The `sendAt` property in the request body is a [Unix timestamp](https://www.unixtimestamp.com/).

Run the application:

```bash
$ python3 main.py
```

##### How It Works

The sipgate REST API is available under the following base URL:

```python
baseURL = 'https://api.sipgate.com/v2'
```

The API expects request data in JSON format. Thus the `Content-Type` header needs to be set accordingly.

```python
headers = {
	'Content-Type': 'application/json'
}
```

The request body contains the `smsId`, `recipient`, and `message` specified above.

```python
requestBody = {
	'smsId': smsId,
	'recipient': recipient,
	'message': message
}
```

We use the python package 'requests' for request generation and execution. The `post` function takes as arguments the request URL, headers, an authorization header, and the request body. The request URL consists of the base URL defined above and the endpoint `/sessions/sms`. The function `HTTPBasicAuth` from the 'requests' package takes credentials and generates the required Basic Auth header (for more information on Basic Auth see our [code example](https://github.com/sipgate/sipgateio-basicauth-python)).

```python
response = requests.post(
	f'{baseURL}/sessions/sms',
	headers=headers,
	auth=requests.auth.HTTPBasicAuth(username, password),
	json=requestBody
)
```

### Web SMS Extensions

A Web SMS extension consists of the letter 's' followed by a number (e.g. 's0'). The sipgate API uses the concept of Web SMS extensions to identify devices within your account that are enabled to send SMS. In this context the term 'device' does not necessarily refer to a hardware phone but rather a virtual representation.

You can find out what your extension is as follows:

1. Log into your [sipgate account](https://app.sipgate.com/connections/sms)
2. Use the sidebar to navigate to the **Connections** (_Anschlüsse_) tab
3. Click **SMS** (if this option is not displayed you might need to book the **Web SMS** feature from the Feature Store)
4. The URL of the page should have the form `https://app.sipgate.com/{...}/connections/sms/{smsId}` where `{smsId}` is your Web SMS extension.

### Common Issues

#### SMS sent successfully but no message received

Possible reasons are:

- incorrect or mistyped phone number
- recipient phone is not connected to network
- long message text, delivery can take a little longer

#### HTTP Errors

| reason                                                                                                                                              | errorcode |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | :-------: |
| bad request (e.g. request body fields are empty or only contain spaces, timestamp is invalid etc.)                                                  |    400    |
| username and/or password are wrong                                                                                                                  |    401    |
| your account balance is insufficient                                                                                                                |    402    |
| no permission to use specified SMS extension (e.g. SMS feature not booked, user password must be reset in [web app](https://app.sipgate.com/login)) |    403    |
| wrong REST API endpoint                                                                                                                             |    404    |
| wrong request method                                                                                                                                |    405    |
| wrong or missing `Content-Type` header with `application/json`                                                                                      |    415    |
| internal server error or unhandled bad request (e.g. `smsId` not set)                                                                               |    500    |

### Related

- [datetime documentation](https://docs.python.org/3/library/datetime.html)
- [requests documentation](http://docs.python-requests.org/en/master/)

### Contact Us

Please let us know how we can improve this example.
If you have a specific feature request or found a bug, please use **Issues** or fork this repository and send a **pull request** with your improvements.

### License

This project is licensed under **The Unlicense** (see [LICENSE file](./LICENSE)).

### External Libraries

This code uses the following external libraries

- requests:
  Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
  Website: http://docs.python-requests.org/en/master/

---

[sipgate.io](https://www.sipgate.io) | [@sipgateio](https://twitter.com/sipgateio) | [API-doc](https://api.sipgate.com/v2/doc)