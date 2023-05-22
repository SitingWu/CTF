from Crypto.Util.number import *

hex='0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
key='\0'
empty_char=' '
first_char= 'c'
second_char= 'r'
third_char ='y'
fourth_char= 'p'
fifth_char='t'
sixth_char='o'
seventh_char='{'
flag='\0'
print(chr(bytes_to_long(bytes.fromhex(hex[0:2]))))
print(chr(bytes_to_long(bytes.fromhex(hex[2:4]))))
# for i in range(len(hex)):
#     if i%2 ==0:
for i in range(256):
    if bytes_to_long(bytes.fromhex(hex[0:2]))^i==ord(first_char):
         print(i)
         print(chr(bytes_to_long(bytes.fromhex(hex[0:2]))^i))
         key += chr(i)
         flag+= chr(bytes_to_long(bytes.fromhex(hex[0:2]))^i)
         print(flag)
         break
    # else:
    #     print(i)
    #     print
    
for i in range(256):
    if bytes_to_long(bytes.fromhex(hex[2:4]))^i==ord(second_char):
        print(i)
        key += chr(i)
        flag+= chr(bytes_to_long(bytes.fromhex(hex[2:4]))^i)
        print(flag)
        break

for i in range(256):
    if bytes_to_long(bytes.fromhex(hex[4:6]))^i==ord(third_char):
        print(i)
        key += chr(i)
        flag+= chr(bytes_to_long(bytes.fromhex(hex[4:6]))^i)
        break

for i in range(256):
    if bytes_to_long(bytes.fromhex(hex[6:8]))^i==ord(fourth_char):
        print(i)
        key += chr(i)
        flag+= chr(bytes_to_long(bytes.fromhex(hex[6:8]))^i)
        break

for i in range(256):
    if bytes_to_long(bytes.fromhex(hex[8:10]))^i==ord(fifth_char):
        print(i)
        key += chr(i)
        flag+= chr(bytes_to_long(bytes.fromhex(hex[8:10]))^i)
        break
for i in range(256):
    if bytes_to_long(bytes.fromhex(hex[10:12]))^i==ord(sixth_char):
        print(i)
        key += chr(i)
        flag+= chr(bytes_to_long(bytes.fromhex(hex[10:12]))^i)
        print(flag)
        break

for i in range(256):
    if bytes_to_long(bytes.fromhex(hex[12:14]))^i==ord(seventh_char):
        print(i)
        key += chr(i)
        flag+= chr(bytes_to_long(bytes.fromhex(hex[12:14]))^i)
        print(flag)
        break

flag+= chr(bytes_to_long(bytes.fromhex(hex[14:16]))^ord('y'))
print("key")
print(key)
for i in range(int(len(hex)/8)):
    if i%2==0:
        i=i*8+16
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('m')))
        print(i)
        print(flag)
        i=i+2
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('y')))
        i=i+2
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('X')))
        i=i+2
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('O')))
        i=i+2
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('R')))
        i=i+2 
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('k')))
        i=i+2
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('e')))
        i=i+2
        flag+=(chr(bytes_to_long(bytes.fromhex(hex[i:i+2]))^ord('y')))
        print(i)
        
print(flag)
    
