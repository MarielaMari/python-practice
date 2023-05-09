# Create Password
# At least 8 characters long
# can contain any sort letters, numbers $%#@
# hast to end with a number

import re

# email: pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# password validation: pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
password = re.compile(r"([a-zA-Z0-9$%#@]{8,}\d)")
mypass = 'klAAjsdjJ3425#$8'

check = password.fullmatch(mypass)
print(check)
