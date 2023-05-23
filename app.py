from flask import Flask
from controllers.home_controller import home_controller

app = Flask(__name__)

# Register the blueprint for the home-related routes
app.register_blueprint(home_controller)

if __name__ == '__main__':
    app.run(debug=True)