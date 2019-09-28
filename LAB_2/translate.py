import config


def translate_to(value, base):
    int_part = int(float(value))
    float_part = float(value) - int_part
    res_int_part = ""
    while int_part != 0:
        res_int_part += config.enum_lit[int_part % base]
        int_part = int_part//base
    res_float_part = ""
    i = 0
    while float_part != 0 and i < 100:
        res_float_part += config.enum_lit[(int(float_part * base))]
        float_part = float_part * base - int(float_part * base)
        i += 1
    if res_int_part == "":
        res_int_part = "0"
    if float("0." + res_float_part) != 0:
        return res_int_part[::-1] + "." + res_float_part
    else:
        return res_int_part[::-1]


def translate_from(value, base):
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
    for number in float_part:
        res_float_part += config.enum[number] * pow(base, -i)
        i += 1
    return float(res_int_part + res_float_part)


def translate_to_hex(number):
    res_number = ""
    for i in range(0, len(number), 4):
        res_number += config.enum_lit[translate_from(number[i:i+4], 2)]
    return res_number
