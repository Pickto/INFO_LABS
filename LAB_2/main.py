import translate


def main():
    num = hexadecimal(-53.734487, 8)
    print(num)


def hexadecimal(number, byte):
    res_number = "0"
    if number < 0:
        res_number = "1"
    number = translate.translate_to(abs(number), 2)
    p = number.find(".") - 1
    if byte == 8:
        bit = 11
    else:
        bit = 8
    order = translate.translate_to(p + 2**(bit - 1) - 1, 2)
    mantissa = number[1:number.find(".")] + number[number.find(".") + 1:]
    mantissa += "0"*(52 - len(mantissa))
    return translate.translate_to_hex(res_number + order) + translate.translate_to_hex(mantissa)


if __name__ == "__main__":
    main()
