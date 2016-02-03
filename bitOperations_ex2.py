def operations(number1, number2):

    and_operator = number1 & number2
    or_operator = number1 | number2
    xor_operator = number1 ^ number2

    print format(and_operator, 'b')
    print format(or_operator, 'b')
    print format(xor_operator, 'b')

# format hex: 0x.., oct: 0o.., bin: 0b..
operations(0xef, 0xf0)
operations(0xef, 0x0f)
operations(0xaa, 0xee)
operations(0o777, 0o377)
operations(0b11110011, 0xf3)
operations(0b01011111, 0xf0)
operations(0b01000101, 0b00000100)
