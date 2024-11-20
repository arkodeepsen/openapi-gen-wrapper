from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    """Returns a greeting message."""
    return "Hello, World!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    """Handles farewell requests."""
    return "Goodbye!"

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieves details for a specific user."""
    return f"User ID: {user_id}"
