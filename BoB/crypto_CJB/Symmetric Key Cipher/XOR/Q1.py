enc_str = "41564b39706a396a76397c786a60383838"

byte_str = bytes.fromhex(enc_str)

for i in range(30):
    p = ''
    for c in byte_str:
        p = p + chr(c^i)
    
    print(i, p)