# Note, see UDEMY 223 - Gmail, 2 way verification NEEDED

import smtplib  # protocol of communication through Simple Mail Transfer Protocol; gmail, hotmail, etc
from email.message import EmailMessage

email = 'Mari M'
email['to'] = 'm.sjls@gmail.com'
email['subject'] = 'You WON 1 000 000 000 dollars!'

email.set_content('I am a PYthon Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomastery@gmail.com', 'the password for this email')
    smtp.send_message(email)
    print('all good boss!')
