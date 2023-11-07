from cryptography.fernet import Fernet
import os

#Generate a random key
key = Fernet.generate_key()

#Initialize the Fernet cipher with the key
cipher_suite = Fernet(key)

#Encrypt the text from a file
def encrypt_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
        ciphertext = cipher_suite.encrypt(plaintext)

    with open(output_file, 'wb') as f:
        f.write(ciphertext)

#Split the key into parts
def split_key(key, num_parts):
    if num_parts < 2:
        print("Key parts should be more than 2.")
        return None

    key_parts = [key[i * (len(key) // num_parts):(i + 1) * (len(key) // num_parts)] for i in range(num_parts)]
    return key_parts

#Save key parts to separate files
def save_key_parts(key_parts, output_dir):
    for i, key_part in enumerate(key_parts):
        with open(f'{output_dir}/key_part_{i + 1}.txt', 'wb') as f:
            f.write(key_part)


#Delete existing text files in the key_parts directory
def delete_existing_key_parts(output_dir):
    for filename in os.listdir(output_dir):
        if filename.endswith(".txt"):
            os.remove(os.path.join(output_dir, filename))

if __name__ == "__main__":
    input_file = "file.txt"
    output_file = "encrypted.txt"

    num_key_parts = int(input("Enter the number of key parts: "))

    output_dir = "key_parts"

    if num_key_parts < 2:
        print("Key parts should be more than 2.")
    else:
        #Delete existing key parts files
        delete_existing_key_parts(output_dir)

        #Encrypt the text from the input file
        encrypt_file(input_file, output_file)

        #Split the key into parts
        key_parts = split_key(key, num_key_parts)

        if key_parts:
            #Save key parts to separate files
            save_key_parts(key_parts, output_dir)

            print("Encryption complete.")
