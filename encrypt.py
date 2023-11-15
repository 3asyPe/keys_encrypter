from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64


# Function to encrypt a string using AES
def encrypt_string(input_string, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(input_string.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct


# Generating a random 256-bit (32 bytes) key
secret_key = get_random_bytes(32)

# File paths
input_filename = 'input.txt'  # Replace with your input file path
output_filename = 'output.txt'

# Reading strings from the input file and encrypting them
with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        iv, encrypted_string = encrypt_string(line.strip(), secret_key)
        outfile.write(iv + '\n' + encrypted_string + '\n')

# Display the secret key in hexadecimal format
print("Secret Key (hex):", secret_key.hex())

# Instructions for setting the environment variable
print("\nTo set the secret key as an environment variable, use the following command:")
print("On Windows (Command Prompt): set SECRET_KEY=" + secret_key.hex())
print("On Linux/macOS (Terminal): export SECRET_KEY=" + secret_key.hex())