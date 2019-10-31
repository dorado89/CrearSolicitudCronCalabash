import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Settings
# set up the SMTP server


class Email:
    @staticmethod
    def send_email(name, tittle, email):
        s = smtplib.SMTP(host=Settings.EMAIL_SMTP_HOST, port=Settings.EMAIL_SMTP_PORT)
        s.starttls()
        s.login(Settings.EMAIL_USERNAME, Settings.EMAIL_PASSWORD)
        msg = MIMEMultipart()  # create a message
        message = "Gracias por usar la aplicación " + name + "\n Su prueba" + tittle +  " ya fue ejecutada"

        msg['From'] = Settings.EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Pruebas Automaticas"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
        s.quit()
