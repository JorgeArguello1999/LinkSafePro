def encrypt(text:str, password:str):
    all_text = [ord(value) for value in text] 
    password = sum([ord(value) for value in password])

    cipher = [value+password for value in all_text]
    new_text = [chr(value) for value in cipher]
    return ''.join(new_text)

def decrypt(text:str, password:str) -> str:
    all_text = [ord(value) for value in text]
    password = sum([ord(value) for value in password])

    descipher = [value-password for value in all_text]
    text_decrypt = [chr(value) for value in descipher]
    return ''.join(text_decrypt)

if __name__ == '__main__':
    encrypt_text = encrypt("@JorgeArguellojñ", "@jorgearguello")
    decrypt_text = decrypt("ײ׼ءؤؙؗ׳ؤؙاؗ؞؞ء؜ڣ", "@jorgearguello")

    print(encrypt_text)
    print(decrypt_text)