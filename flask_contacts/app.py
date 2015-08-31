from flask import Flask, render_template
from twilio.rest import TwilioRestClient

app = Flask(__name__)
client = TwilioRestClient()


contacts = [{'first_name': 'matt', 'last_name': 'makai'}]

@app.route('/')
def list_contacts():
    return render_template('contacts.html', contacts=contacts)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
