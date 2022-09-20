import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('sender_mail@gmail.com', 'Password')

server.sendmail('sender_mail@gmail.com', 'shivay2aab@gmail.com', 'Hi there mail sent from jyoti')
print('Mail sent')