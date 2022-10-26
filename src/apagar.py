from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'felipe.barros2600@gmail.com'
app.config['MAIL_PASSWORD'] = 'pgwmqsxxrrujizhd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def index():
   msg = Message('Hello', sender = 'felipe.barros2600@gmail.com', recipients = ['ttmaster@bol.com.br'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
   index()