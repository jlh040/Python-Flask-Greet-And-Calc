"""Set up four routes, in which each one returns a simple message"""

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Return 'welcome.'"""

    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    """Return 'welcome home.'"""

    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    """Return 'welcome back.'"""

    return 'welcome back'

