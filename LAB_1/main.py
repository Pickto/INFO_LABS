import config


def main():
    while True:
        command = input().split(" ")
        if command[0] == "to":
            print(translate_to(command[1], int(command[2])))
        elif command[0] == "from":
            print(translate_from(command[1], int(command[2])))
        elif command[0] == "calc":
            print(calc(command[1], command[3], int(command[4]), command[2]))
        elif command[0] == "quit":
            break


def translate_to(value, base):
    int_part = int(float(value))
    float_part = float(value) - int_part
    res_int_part = ""
    while int_part != 0:
        res_int_part += config.enum_lit[int_part % base]
        int_part = int_part//base
    res_float_part = ""
    i = 0
    while float_part != 0 and i < 7:
        res_float_part += config.enum_lit[(int(float_part * base))]
        float_part = float_part * base - int(float_part * base)
        i += 1
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
    for number in float_part[:7]:
        res_float_part += config.enum[number] * pow(base, -i)
        i += 1
    return float(res_int_part + res_float_part)


def calc(first_value, second_value, base, sign):
    if sign == '+':
        return sum(first_value, second_value, base)
    elif sign == '*':
        return mult(first_value, second_value, base)
    elif sign == '-':
        return diff(first_value, second_value, base)
    else:
        return "Unexpected sign"


def diff(first_value, second_value, base):
    if base == 10:
        return int(first_value) - int(second_value)
    first_value = translate_from(first_value, base)
    second_value = translate_from(second_value, base)
    return translate_to(str(first_value - second_value), base)


def mult(first_value, second_value, base):
    if base == 10:
        return int(first_value) * int(second_value)
    first_value = translate_from(first_value, base)
    second_value = translate_from(second_value, base)
    return translate_to(str(first_value * second_value), base)

  
def sum(first_value, second_value, base):
    if base == 10:
        return int(first_value) + int(second_value)
    first_value = translate_from(first_value, base)
    second_value = translate_from(second_value, base)
    return translate_to(str(first_value + second_value), base)


if __name__ == "__main__":
    main()
