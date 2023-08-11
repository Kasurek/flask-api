import requests

# use the url, where your validation is located
url = 'http://127.0.0.1:5000/generate_random_number'

min_value = int(input("Please enter the lowest value: \n"))

max_value = int(input("Please enter the max value: \n"))

data = {
        'min_value': min_value,
        'max_value': max_value
        }

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(result['random_number'])
else:
    print('There was a problem with getting a random number')
