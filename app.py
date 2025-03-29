from flask import Flask, jsonify, render_template

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

USERS = {
    "1": {
        "id": "1",
        "username": "johndoe",
        "email": "john@example.com",
        "full_name": "John Doe",
        "address": "123 Main St, Anytown, USA",
        "phone": "555-123-4567",
        "date_joined": "2023-01-15T08:30:00Z",
        "last_login": "2025-03-28T14:22:10Z",
        "premium_status": True,
        "profile_picture": "https://example.com/profiles/johndoe.jpg",
        "preferences": {
            "theme": "dark",
            "language": "en-US",
            "notifications": {
                "email": True,
                "sms": False,
                "push": True
            }
        },
        "payment_info": {
            "card_type": "Visa",
            "last_four": "4242",
            "expiry": "12/27"
        },
        "order_history": [
            {"id": "ord-123", "date": "2025-03-12T10:24:00Z", "total": 89.99},
            {"id": "ord-117", "date": "2025-02-28T15:16:32Z", "total": 42.50},
            {"id": "ord-098", "date": "2025-01-15T12:03:45Z", "total": 125.00}
        ]
    },
    "2": {
        "id": "2",
        "username": "janedoe",
        "email": "jane@example.com",
        "full_name": "Jane Doe",
        "address": "456 Oak Ave, Somewhere, USA",
        "phone": "555-987-6543",
        "date_joined": "2023-02-20T10:15:00Z",
        "last_login": "2025-03-27T09:10:05Z",
        "premium_status": False,
        "profile_picture": "https://example.com/profiles/janedoe.jpg",
        "preferences": {
            "theme": "light",
            "language": "en-GB",
            "notifications": {
                "email": True,
                "sms": True,
                "push": False
            }
        },
        "payment_info": {
            "card_type": "Mastercard",
            "last_four": "9876",
            "expiry": "08/26"
        },
        "order_history": [
            {"id": "ord-145", "date": "2025-03-20T16:42:00Z", "total": 23.99},
            {"id": "ord-132", "date": "2025-03-05T13:27:14Z", "total": 67.25}
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

# All users
@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in USERS:
        return jsonify(USERS[user_id])
    return jsonify({"error": "User not found"}), 404

# for profile page
@app.route('/api/users/<user_id>/profile', methods=['GET'])
def get_user_profile(user_id):
    if user_id in USERS:
        return jsonify(USERS[user_id])
    return jsonify({"error": "User not found"}), 404

#  for settings page
@app.route('/api/users/<user_id>/settings', methods=['GET'])
def get_user_settings(user_id):
    if user_id in USERS:
        return jsonify(USERS[user_id])
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)