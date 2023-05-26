import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Cesar Borja Ruiz'
email['to'] = 'cborjaruiz@gmail.com'
email['subject'] = 'Email Sender Test'

email.set_content('Testing Email Message built in library')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Application Password.
    smtp.login('borjaruizcesar@gmail.com','bufcbtiolnhqkktq')
    smtp.send_message(email)
    print("Completed")
