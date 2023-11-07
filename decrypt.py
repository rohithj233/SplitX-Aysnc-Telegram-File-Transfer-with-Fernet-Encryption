from cryptography.fernet import Fernet
import os

key_parts_dir = "key_parts"

key_part_files = [os.path.join(key_parts_dir, filename) for filename in os.listdir(key_parts_dir) if filename.endswith(".txt")]

#Merge the content of key part files into a single key
def merge_key_parts(key_part_files):
    key_parts = []
    for key_part_file in key_part_files:
        with open(key_part_file, 'rb') as f:
            key_part = f.read()
            key_parts.append(key_part)
    merged_key = b''.join(key_parts)
    return merged_key

#Load the merged key
merged_key = merge_key_parts(key_part_files)
cipher_suite = Fernet(merged_key)

#Decrypt the encrypted file
def decrypt_file(encrypted_file, decrypted_file):
    with open(encrypted_file, 'rb') as f:
        ciphertext = f.read()
        plaintext = cipher_suite.decrypt(ciphertext)
    with open(decrypted_file, 'wb') as f:
        f.write(plaintext)

#Specify the paths for the encrypted and decrypted files
encrypted_file = "encrypted.txt"
decrypted_file = "decrypted.txt"

#Decrypt the encrypted file and save the result
decrypt_file(encrypted_file, decrypted_file)

print("Decryption complete. The result is saved in decrypted.txt.")
