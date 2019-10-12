import config


def translate_to(value, base, count_sign):
    int_part = int(float(value))
    float_part = float(value) - int_part
    res_int_part = ""
    while int_part != 0:
        res_int_part += config.enum_lit[int_part % base]
        int_part = int_part//base
    res_float_part = ""
    i = 0
    while float_part != 0 and i < count_sign:
        res_float_part += config.enum_lit[(int(float_part * base))]
        float_part = float_part * base - int(float_part * base)
        i += 1
    if res_int_part == "":
        res_int_part = "0"
    if float("0." + res_float_part) != 0:
        return res_int_part[::-1] + "." + res_float_part
    else:
        return res_int_part[::-1]


def translate_from(value, base, count_sign):
    value = value.split(".")
    int_part = value[0]
    if len(value) > 1:
        float_part = value[1]
    else:
        float_part = ""
    i = 0
    res_int_part = 0
    for number in int_part[::-1]:
        res_int_part += config.enum[number] * pow(base, i)
        i += 1
    res_float_part = 0
    i = 1
    for number in float_part[:count_sign]:
        res_float_part += config.enum[number] * pow(base, -i)
        i += 1
    return float(res_int_part + res_float_part)


def translate_to_hex(number, byte):
    res_number = ""
    for i in range(0, len(number), 4):
        res_number += config.enum_lit[translate_from(number[i:i+4], 2, byte * 8)]
    return res_number


def to_hexadecimal(number, byte):
    sign = "0"
    if number < 0:
        sign = "1"
    number = translate_to(abs(number), 2, byte * 8)
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
    order = translate_to(p + 2**(bit - 1) - 1, 2, byte * 8)
    order = "0"*(bit - len(order)) + order
    mantissa = number[number.find("1") + 1:number.find(".")] + number[number.find(".") + 1:(byte * 8 - bit + 1)]
    mantissa += "0"*((byte * 8 - bit - 1) - len(mantissa))
    return translate_to_hex(sign + order + mantissa, byte)


def from_hexadecimal(hex_number, byte):
    binary_number = translate_to(translate_from(hex_number, 16, byte * 8), 2, byte * 8)
    if len(binary_number) < byte * 8:
        binary_number = "0"*(byte * 8 - len(binary_number)) + binary_number
    if byte == 8:
        bit = 11
    elif byte == 4:
        bit = 8
    p = translate_from(binary_number[1:bit + 1], 2, byte * 8) - (2**(bit - 1) - 1)
    res_number = translate_from("1." + binary_number[bit + 1:],  2, byte * 8) * 2**p
    if binary_number[0] == "0":
        return res_number
    else:
        return -res_number
