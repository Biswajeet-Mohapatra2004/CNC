key=5
def encrypt(word):
    encrypted=""
    for letter in word:
        if letter.isalpha():
            if letter.islower():
                encrypted+=chr((ord(letter)-ord('a')+key)%26+ord('a'))
            else:
                encrypted+=chr((ord(letter)-ord('A')+key)%26+ord('A'))     
        elif letter.isnumeric():
            encrypted+=chr((ord(letter)-48+key)%10+48)
        else:
            if ord(letter)>=58 and ord(letter)<=64:
                encrypted+=chr((ord(letter)-58+key)%7+58)
            elif ord(letter)>=32 and ord(letter)<=47:
                encrypted+=chr((ord(letter)-32+key)%15+32) 
            else:
                print("Invalid character")
    return encrypted
       
def decrypt(word):
    decrypted=""
    for letter in word:
        if letter.isalpha():
            if letter.islower():
                decrypted+=chr((ord(letter)-ord('a')-key)%26+ord('a'))
            else:
                decrypted+=chr((ord(letter)-ord('A')-key)%26+ord('A'))     
        elif letter.isnumeric():
            decrypted+=chr((ord(letter)-48-key)%10+48)
        else:
            if ord(letter)>=58 and ord(letter)<=64:
                decrypted+=chr((ord(letter)-58-key)%7+58)
            elif ord(letter)>=32 and ord(letter)<=47:
                decrypted+=chr((ord(letter)-32-key)%15+32) 
            else:
                print("Invalid character")
    return decrypted
word=str(input("Enter a word: "))
encrypted_word=encrypt(word)
print("Encrypted:",encrypted_word)
decrypted_word=decrypt(encrypted_word) 
print("Decrypted:",decrypted_word)           
