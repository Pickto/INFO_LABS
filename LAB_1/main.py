import config


def main():
    value = input()
    base = int(input())
    print(translate_from(value, base))


def translate_to(value, base):
    int_part = int(value)
    float_part = value - int_part
    res_int_part = ""
    while int_part != 0:
        res_int_part += str(int_part % base)
        int_part = int_part//base
    res_float_part = ""
    i = 0
    while float_part != 0 and i < 7:
        res_float_part += str(int(float_part * base))
        float_part = float_part * base - int(float_part * base)
        i+=1
    if float("0."+res_float_part) != 0:
        return int(res_int_part[::-1]) + float("0."+res_float_part)
    else:
        return int(res_int_part[::-1])


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
    for number in float_part[:7]:
        res_float_part += config.enum[number] * pow(base, -i)
        i += 1
    return res_int_part + res_float_part


if __name__ == "__main__":
    main()
