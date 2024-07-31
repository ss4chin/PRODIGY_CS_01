letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, func, key):
    result = ''
    if func == 'd':
        key = -key
    
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                index2 = index + key
                if index2 >= num_letters:
                    index2 -= num_letters
                elif index2 < 0:
                    index2 += num_letters
                result += letters[index2]
    return result

print('Caesar Cypher')
print('Press e for encryption & d for decryption')
userip = input('e/d: ').lower()

if userip == 'e':
    print('Encryption Function Selected')
    key = int(input('Enter the key: '))
    text = input('Enter text for encryption: ')
    ciphertext = encrypt_decrypt(text, userip, key)
    print(f'CIPHERTEXT: {ciphertext}')


elif userip == 'd':
    print('Decryption Function Selected')
    key = int(input('Enter the key: '))
    text = input('Enter text for decryption: ')
    plaintext = encrypt_decrypt(text, userip, key)
    print(f'PLAINTEXT: {plaintext}')






