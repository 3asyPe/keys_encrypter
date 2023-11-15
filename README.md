# keys encrypter

Encrypts any strings in input.txt file to output.txt with generated secret_key

**How to install**
```
pip install -r requirements.txt
```
**How to run**

1) Input your strings to input.txt file

2) To encrypt run

```
python encrypt.py
```

3) Get your encrypted strings in output.txt

4) Save secret_key printed during the encryption and use it when you need to decrypt it by setting it as an environment variable

5) (Optional) Input your encrypted strings to input.txt and run decrypt.py file to test that it's working

**How to decrypt it in code**
If you need these strings to use in your script decrypt them in such way:
```
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
```
