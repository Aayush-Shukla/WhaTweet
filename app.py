
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.secret_key='ayush'

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    session['phone_no'] = ''
    msg = request.form.get('Body')
    if(msg=='*'):
        session['phone_no']=request.form.get('From')
    # Create reply
    resp = MessagingResponse()
    if(msg==69):
        resp.message("Session is {}".format(session['phone_no']))
    else:

        resp.message("You said: {} ".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
