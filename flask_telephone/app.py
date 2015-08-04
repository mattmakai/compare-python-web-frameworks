from flask import Flask, render_template
from twilio.rest import TwilioRestClient

app = Flask(__name__)
client = TwilioRestClient()


@app.route('/')
def phone():
    return render_template('phone.html')


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
