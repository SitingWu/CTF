#-Challenge from: https://siiiopenctf.uscybergames.com/challenges
# def encrypt(key, plaintext):
#     ciphertext = ""
#     for i in range(len(plaintext)):
#         newchar = (ord(plaintext[i]) - 97) + (ord(key[i]) - 97)
#         newchar %= 26
#         ciphertext += chr(newchar + 97)
#     return ciphertext
    
# key =  "<REDACTED>"
# flag = "<REDACTED>"

# for i in range(1000):
#     flag = encrypt(key, flag)
#     key = encrypt(flag, key)
# print(key)
# print(flag)

#--- Decrytion--------
flag_enc ="raaojpkaufmsrez"
key_enc = "tmjuefrwtvjirfx"
def decrypt(key, plaintext):
    ciphertext=""
    for i in range(len(plaintext)):
        newchr = (ord(plaintext[i]) + 97) - (ord(key[i]) + 97)
        newchr %= 26
        ciphertext += chr(newchr + 97)
    return ciphertext

for i in range(1000):
    flag_enc = decrypt(key_enc, flag_enc)
    key_enc = decrypt(flag_enc, key_enc)
print(key_enc)
print(flag_enc)

#flag: uscg{morerepetitionsdoesntmeansafer}