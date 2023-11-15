import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Ensure the SECRET_KEY environment variable is set
if 'SECRET_KEY' not in os.environ:
    raise ValueError("The environment variable SECRET_KEY is not set")

# Converting the secret key from hex to bytes
secret_key = bytes.fromhex(os.environ['SECRET_KEY'])

# File path
input_filename = 'input.txt'  # Replace with your file path
output_filename = 'output.txt'

STRINGS = []

# Reading and decrypting the data
with open(input_filename, 'r') as file:
    with open(output_filename, 'w') as outfile:
        while True:
            iv_line = file.readline().strip()
            ct_line = file.readline().strip()
            if not ct_line: break  # End of file
            iv = base64.b64decode(iv_line)
            ct = base64.b64decode(ct_line)
            cipher = AES.new(secret_key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
            STRINGS.append(pt.strip())

print(STRINGS)