from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

# open and load the file containing users info
with open('users.json', 'r') as users_json:
    users = json.load(users_json)


# this route is used to return the info about an user, by using it's "id".
@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    user_info = users.get(user_id, {'message': 'Użytkownik nie istnieje.'})
    return jsonify(user_info)

# function used to check if the password is complex enough
def is_complex_enough(password):
    if len(password) < 8:
        return False, "Password needs to be over 8 characters long"
    if not any(char.isdigit() for char in password):
        return False, "Password needs at least one digit"
    if not any(char.isupper() for char in password):
        return False, "Password needs at least one uppercase letter"
    if not any(char.islower() for char in password):
        return False, "Password needs at least one lowercase letter"
    return True, "The password is complex enough"

# this route is used to check the complexity of a password
@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.json.get('password')
    is_complex, message = is_complex_enough(password)

    if is_complex:
        return jsonify({'message': 'Password is complex enough'})
    else:
        return jsonify({'message': message}), 400

# this route is used to generate a random number
@app.route('/generate_random_number', methods=['POST', 'GET'])
def generate_random_number():
    # getting the max and min values using POST from the test app
    if request.method == 'POST':
        min_value = int(request.json.get('min_value'))
        max_value = int(request.json.get('max_value'))
    # getting the max and min values from the args in the link.
    else:
        min_value = int(request.args.get('min_value'))
        max_value = int(request.args.get('max_value'))
    random_number = random.randint(min_value, max_value)
    return jsonify({'random_number': random_number})

if __name__ == '__main__':
    app.run()
