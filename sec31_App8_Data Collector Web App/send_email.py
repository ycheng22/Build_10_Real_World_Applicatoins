from email.mime.text import MIMEText
import smtplib

def send_email(email, height, ave_height, count):
    from_email = "mygmail@gmail.com"
    from_passowrd = "mypassword"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. \
        Average height of all is <strong>%s</strong> and that is calculated out \
        <strong>%s</strong> of people." % (height, ave_height, count)
    
    msg = MIMEText(message, 'html')
    msg['subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_passowrd)
    gmail.send_message(msg)

