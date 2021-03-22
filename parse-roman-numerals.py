def parse_roman_numerals(input):
    numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    number = 0
    num_list = []
    for numeral in input:
        num_list.append(numerals[numeral])

    for i in range(0, len(num_list)-1):
        if num_list[i+1] > num_list[i]:
            number -= num_list[i]
        else:
            number += num_list[i]
    number += num_list[-1]
    return number


# Simple tests using pytest
# I could assume correct input from the challenge

class TestClass:
    def test_numerals(self):
        assert parse_roman_numerals('X') == 10
        assert parse_roman_numerals('XLIX') == 49
        assert parse_roman_numerals('XCIX') == 99
        assert parse_roman_numerals('DCCCXLVII') == 847
        assert parse_roman_numerals('MLIII') == 1053
        assert parse_roman_numerals('MDCCLXXVI') == 1776
