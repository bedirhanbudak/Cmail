import imaplib
import smtplib
import email
from email.header import decode_header
from email.mime.text import MIMEText
import time
import re
import authenticator

# Variable Definitions
user_email_address = str()
user_password = str()
confirmation_codes = dict()
logs = {"email": False, "info": False, "cmail": False, "del_info": False}
imap_protocol = str()
smtp_protocol = str()
smtp_port = int()


# Start the program
def start():
    time.sleep(2)  # Delay to ensure connection

    # Connect and login to the e-mail server
    mail = imaplib.IMAP4_SSL(imap_protocol)
    mail.login(user_email_address, user_password)

    time.sleep(2)  # Delay to ensure connection

    # Select the inbox and search for new e-mails
    mail.select("inbox")
    status, messages = mail.search(None, "RECENT")
    messages = messages[0].split()  # Get the list of new e-mail IDs

    # Iterate through the new e-mails and send a response
    for email_id in messages:
        time.sleep(1)  # Delay to ensure connection

        # Get the e-mail data
        status, email_data = mail.fetch(email_id, "(RFC822)")

        # Assign the e-mail data to email_message
        email_message = email.message_from_bytes(email_data[0][1])

        # Extract the sender's e-mail address information
        sender_email = email_message["From"]
        sender_subject = email_message["Subject"]

        # Check the information e-mail
        if ": Confirmed Mail" in sender_subject:
            logs["info"] = True  # Log record for new information e-mail
            email_content = email_data[0][1].decode("utf-8")

            # Search for the confirmation code present if in the content
            for confirmed_key, confirmed_code in confirmation_codes.items():
                if confirmed_code in email_content:  # If code is matched
                    mail.store(confirmed_key, '+FLAGS', '\\Flagged')
                    logs["cmail"] = True  # Log record for new Confirmed Mail
                    if logs["del_info"]:  # If "Auto DEL" is checked
                        mail.store(email_id, '+FLAGS', '\\Deleted')
                        logs["info"] = False  # Log disabled for new info

        # Send the response e-mail
        else:
            logs["email"] = True  # Log record for new e-mail

            # Generate a confirmation code and add it to the dictionary
            confirmation_code = authenticator.create_code()
            confirmation_codes.update({email_id: confirmation_code})

            # Search for name and email pattern in the sender_email
            match = re.search(r"^(.*?)\s*<|([\w\.-]+)@([\w\.-]+)", sender_email)

            if match:
                # Extract the captured name or username
                username = match.group(1) or match.group(2)

                # Decode the username if it is encoded
                decoded_parts = decode_header(username)
                decoded_username = ""
                for part, encoding in decoded_parts:
                    if isinstance(part, bytes):
                        decoded_username += part.decode(encoding or "utf-8", errors="ignore")
                    else:
                        decoded_username += part

                # Remove leading and trailing whitespace from the username
                username = decoded_username.strip()

            else:
                # If no match is found, assign the username as "Unknown"
                username = "Unknown"

            # Extract the plain text part of the e-mail
            plain_text_part = None
            for part in email_message.walk():
                if part.get_content_type() == 'text/plain':
                    plain_text_part = part
                    break

            # Check if a plain text part was found and decode it
            if plain_text_part:
                original_content = plain_text_part.get_payload(decode=True).decode("utf-8", errors="ignore")
            else:
                original_content = "No plain text content found in the e-mail."

            # Response message content
            response_message = MIMEText("Hi " + username + ",\n\n"
                                        "This e-mail address is secured by Confirmed Mail system designed to prevent phishing attacks. "
                                        "Read more about Cmail: github.com/bedirhanbudak/Cmail\n\n"
                                        "(!) To confirm your identity, please reply to this e-mail with this code: " + confirmation_code + "\n"
                                        "(!) If you are not the sender of the e-mail shown below, DO NOT reply to this e-mail!\n\n"
                                        "Feel free to add any additional information.\n\n"
                                        "Sincerely yours,\n\n"
                                        "Confirmed Mail\n\n"
                                        "------------------------------------------\n\n"
                                        "The content of your e-mail to be confirmed:\n\n" +
                                        original_content, _charset="utf-8")

            # Settings for response e-Mail
            response_message["Subject"] = "Confirmed Mail"
            response_message["From"] = user_email_address
            response_message["To"] = sender_email

            # Send the response e-mail
            server = smtplib.SMTP(smtp_protocol, smtp_port)
            server.starttls()
            server.login(user_email_address, user_password)
            server.send_message(response_message)
            server.quit()


# Delete information e-mails
def del_info():
    # Create an IMAP4_SSL object and login to the e-mail server
    mail = imaplib.IMAP4_SSL(imap_protocol)
    mail.login(user_email_address, user_password)

    # Select the "inbox" folder
    mail.select("inbox")

    # Search for e-mails with the subject ": Confirmed Mail"
    status, emails = mail.search(None, 'Subject ": Confirmed Mail"')

    # Get the list of e-mail IDs from the search results
    email_ids = emails[0].split()

    # Iterate over the e-mail IDs and mark them for deletion
    for email_id in email_ids:
        mail.store(email_id, '+FLAGS', '\\Deleted')

    # Logout from the e-mail server
    mail.logout()


# Delete all e-mails except Confirmed Mails
def del_email():
    # Create an IMAP4_SSL object and login to the e-mail server
    mail = imaplib.IMAP4_SSL(imap_protocol)
    mail.login(user_email_address, user_password)

    # Select the "inbox" folder
    mail.select("inbox")

    # Search for emails that are marked as "UNFLAGGED"
    status, emails = mail.search(None, "UNFLAGGED")

    # Get the list of e-mail IDs from the search results
    email_ids = emails[0].split()

    # Iterate over the email IDs and mark them for deletion
    for email_id in email_ids:
        mail.store(email_id, '+FLAGS', '\\Deleted')

    # Logout from the e-mail server
    mail.logout()
