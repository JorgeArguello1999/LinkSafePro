def binary_decimal(binary: int) -> int:
    decimal = 0
    power_of_two = 0

    for digit in reversed(binary):
        if digit == '1':
            decimal += 2**power_of_two
        power_of_two += 1

    return decimal

def decimal_binary(decimal: int) -> int:
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        decimal //= 2
        binary = str(remainder) + binary

    return binary