#KEY1 = 5ec91664dc988854d1078d7b31b0a1a62cdb709ba41d9748319819ad3cd17a53df673c2fcd
#KEY2 ^ KEY1 = 30a85e52740840c47c61cd51170da8a0063b1ef164de6d714ebeebfd7feabaeb47e7be80d6
#KEY2 ^ KEY3 = 1474df95152ddc3500ee4f43e677e3674b2274c0dacd8d3f7a05ed20d6a6739def986be10f
#SECRET ^ KEY1 ^ KEY3 ^ KEY2 = 0fc5aa9dbcc63d17b4c9ad4af7a830e1028167370ba373012ebd90e4991d7ca0538b3ea1ac

from Crypto.Util.number import *

KEY1 = bytes.fromhex('5ec91664dc988854d1078d7b31b0a1a62cdb709ba41d9748319819ad3cd17a53df673c2fcd')
KEY1 = bytes_to_long(KEY1)

KEY2 = KEY1 ^ bytes_to_long(bytes.fromhex('30a85e52740840c47c61cd51170da8a0063b1ef164de6d714ebeebfd7feabaeb47e7be80d6'))
KEY3 = KEY2 ^ bytes_to_long(bytes.fromhex('1474df95152ddc3500ee4f43e677e3674b2274c0dacd8d3f7a05ed20d6a6739def986be10f'))
SECRET = KEY1 ^ KEY2 ^ KEY3 ^ bytes_to_long(bytes.fromhex('0fc5aa9dbcc63d17b4c9ad4af7a830e1028167370ba373012ebd90e4991d7ca0538b3ea1ac'))

print(long_to_bytes(SECRET))