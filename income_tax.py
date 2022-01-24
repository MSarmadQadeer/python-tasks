print("'0' for single")
print("'1' for Married Filing Jointly")
print("'2' for Married Filing Separately")
print("'3' for Head of Household")
status = int(input("Enter 0-3 for your Status:"))
income = int(input("Enter your Income:"))
if status == 0:
    if income <= 8350:
        income_tax = income*(10/100)
        print("your Income tax is ", income_tax)
    elif income > 8350 and income <= 33950:
        income_tax = income*(15/100)
        print("your Income tax is ", income_tax)
    elif income > 33950 and income <= 82250:
        income_tax = income*(25/100)
        print("your Income tax is ", income_tax)
    elif income > 82250 and income <= 171550:
        income_tax = income*(28/100)
        print("your Income tax is ", income_tax)
    elif income > 171550 and income <= 372950:
        income_tax = income*(33/100)
        print("your Income tax is ", income_tax)
    else:
        income_tax = income*(35/100)
        print("your Income tax is ", income_tax)
elif status == 1:
    if income <= 16700:
        income_tax = income*(10/100)
        print("your Income tax is ", income_tax)
    elif income > 16700 and income <= 67900:
        income_tax = income*(15/100)
        print("your Income tax is ", income_tax)
    elif income > 67900 and income <= 137050:
        income_tax = income*(25/100)
        print("your Income tax is ", income_tax)
    elif income > 137050 and income <= 208850:
        income_tax = income*(28/100)
        print("your Income tax is ", income_tax)
    elif income > 208850 and income <= 372950:
        income_tax = income*(33/100)
        print("your Income tax is ", income_tax)
    else:
        income_tax = income*(35/100)
        print("your Income tax is ", income_tax)
elif status == 2:
    if income <= 8350:
        income_tax = income*(10/100)
        print("your Income tax is ", income_tax)
    elif income > 8350 and income <= 33950:
        income_tax = income*(15/100)
        print("your Income tax is ", income_tax)
    elif income > 33950 and income <= 68525:
        income_tax = income*(25/100)
        print("your Income tax is ", income_tax)
    elif income > 68525 and income <= 104425:
        income_tax = income*(28/100)
        print("your Income tax is ", income_tax)
    elif income > 104425 and income <= 186475:
        income_tax = income*(33/100)
        print("your Income tax is ", income_tax)
    else:
        income_tax = income*(35/100)
        print("your Income tax is ", income_tax)
elif status == 3:
    if income <= 11950:
        income_tax = income*(10/100)
        print("your Income tax is ", income_tax)
    elif income > 11950 and income <= 45500:
        income_tax = income*(15/100)
        print("your Income tax is ", income_tax)
    elif income > 45500 and income <= 117450:
        income_tax = income*(25/100)
        print("your Income tax is ", income_tax)
    elif income > 117450 and income <= 190200:
        income_tax = income*(28/100)
        print("your Income tax is ", income_tax)
    elif income > 190200 and income <= 372950:
        income_tax = income*(33/100)
        print("your Income tax is ", income_tax)
    else:
        income_tax = income*(35/100)
        print("your Income tax is ", income_tax)
