import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Cesar Borja Ruiz'
email['to'] = 'cborjaruiz@gmail.com'
email['subject'] = 'Email Sender Test'

email.set_content(html.substitute(name='Ñordel'),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Application Password.
    smtp.login('borjaruizcesar@gmail.com','bufcbtiolnhqkktq')
    smtp.send_message(email)
    print("Completed")
