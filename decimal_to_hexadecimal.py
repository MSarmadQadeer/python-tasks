decimal = input(
    "Enter any Decimal number that you wanna convert to Hexa-Decimal: ")
quotient = int(decimal)
remainder = int(decimal)
hexadecimal = ""
while quotient > 0:
    remainder = quotient % 16
    quotient = quotient//16
    if remainder == 10:
        remainder = "A"
    elif remainder == 11:
        remainder = "B"
    elif remainder == 12:
        remainder = "C"
    elif remainder == 13:
        remainder = "D"
    elif remainder == 14:
        remainder = "E"
    elif remainder == 15:
        remainder = "F"
    hexadecimal = str(remainder)+hexadecimal
print("Hexa-Decimal of ", decimal, " is: ", hexadecimal)
