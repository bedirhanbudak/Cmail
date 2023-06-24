# Confirmed Mail

Confirmed Mail (Cmail) is basically an e-mail security system developed to prevent phishing attacks by confirming that incoming e-mails are actually coming from the sender.

## How Does Cmail Work?

Cmail seeks the user’s e-mail address to check for recent e-mails. If a new e-mail arrives or if there is a new unread e-mail in the inbox, Cmail automatically sends a response e-mail to the sender of the incoming e-mail with a unique confirmation code. Once the sender replies to this e-mail with the unique code, Cmail checks it and if the confirmation code in the reply matches the code in the sent response, the first incoming e-mail is marked, so that this e-mail is called "*Confirmed Mail*".

## Simple Guide:

#### `Required` Set protocol addresses: "*Settings*" -> "*Service Adjustment*"

<img src="https://github.com/bedirhanbudak/Cmail/blob/main/readme/service_adjustment.png" alt="Service Adjustment" width="320"/>

* You can find the appropriate protocol addresses for your e-mail address provider by looking on the internet.
* A few sample protocol configurations are provided under the “*Information*” heading.
* If you make a mistake during this adjustment, the application will terminate without reporting any error.

#### `Optional` Delete redundant e-mails: "*Settings*" -> "*Inbox Cleaning*"

<img src="https://github.com/bedirhanbudak/Cmail/blob/main/readme/inbox_cleaning.png" alt="Inbox Cleaning" width="320"/>

* **DEL information:** Delete all information (reply) e-mails from the sender in your inbox.
* **DEL not confirmed:** Delete all e-mails in your inbox except confirmed (marked) ones.

#### `Optional` Preferences: "*Settings*" -> "*Show notifications*" & “*Auto DEL info*”

<img src="https://github.com/bedirhanbudak/Cmail/blob/main/readme/preferences.png" alt="Preferences" width="200"/>

* **Show notifications:** If you disable it, you do not receive any message box notifications.

* **Auto DEL info:** If you enable it, information (reply) e-mails are automatically deleted after reading.

#### `Required` Enter your e-mail address and password, then start: “*Cmail*” -> “*Start*”

<img src="https://github.com/bedirhanbudak/Cmail/blob/main/readme/cmail_main.png" alt="Cmail" width="320"/>

#### `Attention` Cmail may send responses to all unread e-mail.

* It is advisable to mark all e-mails in your inbox as read before using Cmail.

#### `Attention` Cmail may crash.

* Please make sure that you fill in the required fields with the correct information.

#### `Attention` If you use Gmail, you need to create an “application password” to use Cmail.

* Creating application passwords: https://support.google.com/mail/answer/185833

#### `Information` Sample protocol configurations for various e-mail address provider:

|  | Gmail  | Hotmail & Outlook | MSN | Yahoo |
| :--- | :---: | :---: | :---: | :---: |
| `IMAP Server` | imap.gmail.com | outlook.office365.com | imap-mail.outlook.com | imap.mail.yahoo.com |
| `SMTP Server` | smtp.gmail.com | smtp.office365.com | smtp-mail.outlook.com | smtp.mail.yahoo.com |
| `SMTP Port` | 587 | 587 | 587 | 465 |

## Phishing E-mail Prevention System: Confirmed Mail

Read the project's thesis for all the details: [Confirmed Mail](https://raw.githubusercontent.com/posquit0/link)

## Contact Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin.svg)](https://www.linkedin.com/in/bedirhan-budak) [![LinkedIn](https://img.shields.io/badge/Telegram-blue?logo=telegram.svg)](https://t.me/bedirhanb)

## License & Copyright

**Cmail © 2023 Bedirhan BUDAK**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)



