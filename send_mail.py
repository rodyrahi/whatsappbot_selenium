import smtplib

def send_mail(validity):
    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login( 'rodyrahi126@gmail.com' , 'wkwbgqatbkqxcjgc')
        subject = 'pass'
        body = validity
        msg = f'Subject:{subject}\n\n{body}'
        smtp.sendmail('rodyrahi126@gmail.com' , 'rajvendrarahi126@gmail.com' , msg)