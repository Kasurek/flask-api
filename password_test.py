import requests

# use the url, where your validation is located
url = 'http://127.0.0.1:5000/check_password'

password = input("Please put in your password: \n")

data = {'password': password}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(result['message'])
else:
    print('There was a problem with veryfing the password, try using another one...')
