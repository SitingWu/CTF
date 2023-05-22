

from Crypto.Util.number import *
hex ='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
first_hex= '73'
second_hex= '62'
first_char= 'c'
second_char= 'r'
end = 0 
flag_char='\0'
for secret in range(256):
    flag= bytes_to_long(bytes.fromhex(first_hex))^secret
    for o in chr(flag):
        if o!=first_char:
            print("probe")
            print(secret)
            print(long_to_bytes(flag))
            break
        else:
            # print(long_to_bytes(flag))
            # every Bytes has to XOR with secret
            flag= bytes_to_long(bytes.fromhex(second_hex))^secret
            for c in chr(flag):
                if c!=second_char:
                    print("second char")
                    print(c)
                    break
                else:     
                    print("second char")
                    print(c)
                    for i in range(len(hex)):
                        if i % 2 ==0:
                            flag= (bytes_to_long(bytes.fromhex(hex[i:i+2])))^secret
                            flag_char += chr(flag)
                            print(i)
                            print(flag_char)
                        # secret=secret<<8
                        

                    print("Here is your flag")
                    print(flag_char)
                    end = 1
                    break
    if end ==0:
        secret=secret+1
    else: 
        break  