
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.secret_key='ayush'
num=0


@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    global num
    session['phone_no']=request.form.get('From')
    msg = request.form.get('Body')
    if(msg=='*'):

        num=10
    # Create reply
    resp = MessagingResponse()

    # session.permanent = True
    if(msg=='69'):
        resp.message("Session is {}".format(num))
    else:

        resp.message("You said: {} ".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
