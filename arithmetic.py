
import struct

def dec_to_iee(num):
    float_to_bytes = struct.pack('>f', num)
    bytes_to_int = struct.unpack('>I', float_to_bytes)[0]
    int_to_binary = f'{bytes_to_int:032b}'
    return int_to_binary

add = 0.1 + 0.2
divide = 1.0 / 3.0

res1 = dec_to_iee(add)
res2 = dec_to_iee(divide)

print(f'Add: {add}')
print(f'IEE: {res1}')

print()

print(f'Divide: {divide}')
print(f'IEE: {res2}')











