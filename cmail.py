import imaplib
import smtplib
import email
import time
from email.mime.text import MIMEText
import authenticator

# Definitions
my_mail = "project.confirmedmail@gmail.com"
my_password = "oqpdhimwwadhbzqe"
confirmation_codes = dict()
logs = {"mail": False, "info": False, "cmail": False, "del_info": False}

# Connect to the email server
imap_protocol = "imap.gmail.com"
smtp_protocol = "smtp.gmail.com"
smtp_port = 587
mail = imaplib.IMAP4_SSL(imap_protocol)
mail.login(my_mail, my_password)


def start():
    time.sleep(0)  # Change it
    # Select the inbox and search for new emails
    mail.select("inbox")
    status, messages = mail.search(None, "UNSEEN")
    messages = messages[0].split()

    # Iterate through the new emails and send a response
    for email_id in messages:
        time.sleep(0)  # Change it
        # Get the email and parse it
        status, email_data = mail.fetch(email_id, "(RFC822)")
        email_message = email.message_from_bytes(email_data[0][1])

        # Extract the sender's email address information
        sender_email = email_message["From"]
        sender_subject = email_message["Subject"]

        # Send the response email
        if sender_subject != "Re: Confirmed Mail":
            logs["mail"] = True
            auth_code = authenticator.create_code()
            confirmation_codes.update({email_id: auth_code})
            body = (email_message.get_payload()[0]).get_payload()
            response_message = MIMEText("The email address is secured by the Confirmed Mail system.\n" +
                                        "Cmail system is designed to prevent phishing attacks by confirming that incoming mails are from the original source.\n"
                                        "Reply to this mail to confirm your identity.\n\n" +
                                        "(!) Do NOT change the header of this email.\n" +
                                        "(!) Do NOT delete this code: " + auth_code + "\n\n" +
                                        "You can add any information if you wish.\n\n" +
                                        "- Creator of Cmail\n\n"
                                        "-----------------------\n\n"
                                        "Content of your mail is:\n\n" + body
                                        )
            response_message["Subject"] = "Confirmed Mail"
            response_message["From"] = my_mail
            response_message["To"] = sender_email
            server = smtplib.SMTP(smtp_protocol, smtp_port)
            server.starttls()
            server.login(my_mail, my_password)
            server.send_message(response_message)
            server.quit()

        if sender_subject == "Re: Confirmed Mail":
            logs["info"] = True
            email_content = email_data[0][1].decode("utf-8")
            for confirmed_key, confirmed_code in confirmation_codes.items():
                if confirmed_code in email_content:
                    mail.store(confirmed_key, '+FLAGS', '\\Flagged')
                    logs["cmail"] = True
                    if logs["del_info"]:
                        mail.store(email_id, '+FLAGS', '\\Deleted')
                        logs["cmail"] = False


def exit_app():
    mail.close()
    mail.logout()


def del_info():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(my_mail, my_password)

    mail.select("inbox")
    status, emails = mail.search(None, 'Subject "Confirmed Mail"')
    email_ids = emails[0].split()

    for email_id in email_ids:
        mail.store(email_id, '+FLAGS', '\\Deleted')


def del_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(my_mail, my_password)

    mail.select("inbox")
    status, emails = mail.search(None, "UNFLAGGED")
    email_ids = emails[0].split()

    for email_id in email_ids:
        mail.store(email_id, '+FLAGS', '\\Deleted')
