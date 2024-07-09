import struct

def dec_to_iee(num):
    float_to_bytes = struct.pack('>f', num)
    print(f'float_to_bytes: {float_to_bytes}\n')

    byte_to_int = struct.unpack('>I', float_to_bytes)[0]
    print(f'byte_to_int: {byte_to_int}\n')

    int_to_binary = f'{byte_to_int:032b}'
    print(f'Binary string: {int_to_binary}\n')

    sign = int_to_binary[0]
    print(f'Sign: {sign}\n')

    exponent = int_to_binary[1:9]
    print(f'Exponent: {exponent}\n')

    mantissa = int_to_binary[9:]
    print(f'Mantissa: {mantissa}\n')

    ieee_754 = f"{sign}{exponent}{mantissa}"
    return ieee_754

print(dec_to_iee(85.125))  

