import translate


def main():
    num = to_hexadecimal(123.5, 8)
    print(num)
    num = from_hexadecimal(num, 8)
    print(num)


def to_hexadecimal(number, byte):
    sign = "0"
    if number < 0:
        sign = "1"
    number = translate.translate_to(abs(number), 2)
    if number.find(".") != -1:
        p = number.find(".") - 1
    else:
        p = len(number) - 1
        number += ".0"
    if byte == 8:
        bit = 11
    else:
        bit = 8
    order = translate.translate_to(p + 2**(bit - 1) - 1, 2)
    mantissa = number[1:number.find(".")] + number[number.find(".") + 1:]
    mantissa += "0"*(52 - len(mantissa))
    return translate.translate_to_hex(sign + order) + translate.translate_to_hex(mantissa)


def from_hexadecimal(hex_number, byte):
    binary_number = translate.translate_to(translate.translate_from(hex_number, 16), 2)
    if len(binary_number) < 64:
        binary_number = "0" + binary_number
    if byte == 8:
        p = translate.translate_from(binary_number[1:12], 2) - 1023
    elif byte == 4:
        p = translate.translate_from(binary_number[1:12], 2) - 127
    res_number = translate.translate_from("1." + binary_number[12:],  2) * 2**p
    if binary_number[0] == "0":
        return res_number
    else:
        return -res_number


if __name__ == "__main__":
    main()
