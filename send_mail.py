import random
import smtplib
validity_code = int(random.randint(0,1000000000000))
def send_mail(validity_code):
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login( 'rodyrahi126@gmail.com' , 'wkwbgqatbkqxcjgc')
        subject = 'pass'
        body = validity_code
        msg = f'Subject:{subject}\n\n{body}'
        smtp.sendmail('rodyrahi126@gmail.com' , 'rajvendrarahi126@gmail.com' , msg)