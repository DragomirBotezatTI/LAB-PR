# Importing smtplib for stmp protocol
import smtplib, ssl
# Importing getpass for hinding password
from getpass import getpass
# Importing pop lib for POP protocol
import poplib

# Setting up the protocol and the gmail server
port = 465  # For SSL
smtp_server = "smtp.gmail.com"

def list_emeal(user, password):
    ''' Get the last 3 email from the email '''
    # Create the mail box object
    Mailbox = poplib.POP3_SSL('pop.googlemail.com', '995')
    # Log in the mail box
    Mailbox.user(user)
    Mailbox.pass_(password)
    # Get the number of messages.
    NumofMessages = len(Mailbox.list()[1])
    # Print the last 3 email.
    for i in range(3):
        for msg in Mailbox.retr(NumofMessages - i)[1]:
            print(msg)

def send_email(user, password):
    ''' Sending a email '''
    # Get the revicer email and the message to send.
    receiver_email = input("Introduce the reciver email:")
    message = input("Introducet the email content:")
    context = ssl.create_default_context()
    # Login into the account and send the email.
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver_email, message)
# getting the user email and password to login
print("Please login in your email:")
user = input("Your email:")
password = getpass("Password:")

while True:
    # Choosing the action to perform.
    choose = int(input("Choose your desired action (0= send email, 1 = see last 3 emails):"))
    # Sending an email.
    if choose == 0:
        send_email(user, password)
    # getting the last 3 emails.
    elif choose == 1:
        list_emeal(user, password)
    # Breaking the infinite loop.
    else:
        break


