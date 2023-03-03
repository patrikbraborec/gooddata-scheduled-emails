from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg.attach(MIMEText(body))

    with open(Path("./src/visualization.csv"), "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name="visualization.csv"
        )
    part['Content-Disposition'] = 'attachment; filename="%s"' % "visualization.csv"
    msg.attach(part)

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()