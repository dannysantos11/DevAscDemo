# ----------------------------
# Flask imports and setup
# ----------------------------
# Flask → lightweight web framework to build APIs
# request → access incoming request data
# jsonify → easily send JSON responses
# Response → build custom HTTP responses (like authentication errors)
# Car → custom class (example object for API data)
# wraps → allows decorators (like requires_auth) to preserve function metadata
from flask import Flask, request, jsonify, Response
from classes.mycar import Car
from functools import wraps

# Initialize Flask app
app = Flask(__name__)


# ----------------------------
# Public API Endpoints
# ----------------------------

# Basic GET endpoint at /api
@app.route('/api', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from your Flask API'})

# POST endpoint at /api/car
# This demonstrates reading JSON from the request,
# validating required fields, creating an object, and returning JSON back.
@app.route('/api/car', methods=['POST'])
def handle_car_request():
    data = request.json   # get JSON body
    try:
        make = data.get('make')
        model = data.get('model')
        year = data.get('year')

        # Validation: require all three fields
        if not all([make, model, year]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create a Car object and return its attributes as JSON
        car = Car(make, model, year)
        return jsonify({'car': car.__dict__}), 201   # 201 = Created
    except Exception as e:
        return jsonify({'error': str(e)}), 500       # 500 = Internal Server Error


# ----------------------------
# Authentication Logic
# ----------------------------
# This block shows how to protect endpoints with Basic Auth.

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'secret'

# Helper function to validate credentials
def check_auth(username, password):
    return username == VALID_USERNAME and password == VALID_PASSWORD

# Sends a 401 Unauthorized response if auth fails
def authenticate():
    return Response('Could not validate your credentials.', 
                    401, 
                    {"WWW-Authenticate": 'Basic realm="Log in Required"'})

# Decorator that wraps protected routes with authentication checks
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization   # Flask parses "Authorization" header
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()      # If invalid, return 401
        return f(*args, **kwargs)      # If valid, proceed with original function
    return decorated

# Example protected route → requires valid username/password
@app.route('/protected')
@requires_auth
def protected():
    return jsonify({'message': 'You are authenticated.'})


# ----------------------------
# Run Flask Application
# ----------------------------
# debug=True → auto-reload server on file changes, detailed error messages
if __name__ == '__main__':
    app.run(debug=True)