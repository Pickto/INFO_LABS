import translate


def main():
    num = to_hexadecimal(-123.5, 8)
    print(num)
    num = from_hexadecimal(num, 8)
    print(num)


def to_hexadecimal(number, byte):
    sign = "0"
    if number < 0:
        sign = "1"
    number = translate.translate_to(abs(number), 2, byte * 8)
    if number[0] == "0":
        p = -number.find("1") + 1
        number = number[number.find("1")] + "." + number[number.find("1") + 1:]
    elif number.find(".") != -1:
        p = number.find(".") - 1
    else:
        p = len(number) - 1
        number += ".0"
    if byte == 8:
        bit = 11
    else:
        bit = 8
    order = translate.translate_to(p + 2**(bit - 1) - 1, 2, byte * 8)
    order = "0"*(bit - len(order)) + order
    mantissa = number[1:number.find(".")] + number[number.find(".") + 1:(byte * 8 - bit)]
    mantissa += "0"*((byte * 8 - bit - 1) - len(mantissa))
    return translate.translate_to_hex(sign + order + mantissa, byte)


def from_hexadecimal(hex_number, byte):
    binary_number = translate.translate_to(translate.translate_from(hex_number, 16, byte * 8), 2, byte * 8)
    if len(binary_number) < byte * 8:
        binary_number = "0"*(byte * 8 - len(binary_number)) + binary_number
    if byte == 8:
        bit = 11
        p = translate.translate_from(binary_number[1:12], 2, byte * 8) - 1023
    elif byte == 4:
        bit = 8
        p = translate.translate_from(binary_number[1:9], 2, byte * 8) - 127
    res_number = translate.translate_from("1." + binary_number[bit + 1:],  2, byte * 8) * 2**p
    if binary_number[0] == "0":
        return res_number
    else:
        return -res_number


if __name__ == "__main__":
    main()
