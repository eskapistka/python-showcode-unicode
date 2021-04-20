import re

"""
'The Archives' task from Showcode Unicode competition

Shortened description:

Calculating the check_digit (x) provided a string representation in format '0-00-000000-x'
If the provided string is in invalid format return -1

For example, to calculate the check digit (x) for 0-19-852663-x you would use the equation 
((0*1)+(1*2)+(9*3)+(8*4)+(5*5)+(2*6)+(6*7)+(6*8)+(3*9)) % 11.

Return calculated check digit.

"""

def get_check_digit(input):
    pattern = "^[0-9][-][0-9]{2}[-][0-9]{6}[-][x]$"
    if re.match(pattern, input):
        check_digit = 0
        digits = [int(x) for x in input.replace('-', '')[:-1]]

        for weigh, digit in enumerate(digits):
            check_digit += (digit * (weigh + 1))

        check_digit = check_digit % 11

        return check_digit
    else:
        return -1

class TestClass:
    def test_format(self):
        assert type(get_check_digit('0-19-852663-x')) is int
        assert type(get_check_digit('1-23-456789-x')) is int
        assert get_check_digit('1-23-456789-X') is -1
        assert get_check_digit('1-23-45x789-x') is -1
        assert get_check_digit('1--23-456789-x') is -1
        assert get_check_digit('00-00-000000-x') is -1
    def test_result(self):
        assert get_check_digit('0-19-852663-x') is 6
        assert get_check_digit('1-23-456789-x') is 10