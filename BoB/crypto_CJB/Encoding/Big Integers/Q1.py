from Crypto.Util.number import *

msg_long = 229230565147107295406317740353514954249435561690958924067043717850269744563177085303284685733404307298563548749673190674163244330490346617736881523

byte_data = long_to_bytes(msg_long)
print(byte_data)