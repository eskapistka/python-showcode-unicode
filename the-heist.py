def calculate_capacity(input):
    volume = 0
    max_height = max(input)
    x_y_list = [[i, x] for i, x in enumerate(input)]
    x_y_list.sort(key= lambda x: x[1], reverse=1)

    if len(x_y_list) <= 255:
        for h in range(max_height, 1, -1):
            temp = []
            for t in x_y_list:
                if t[1] >= h:
                    temp.append(t)
            if len(temp) != 1:
                temp.sort()
                prev = temp[0]
                for tt in temp[1:]:
                    volume += (tt[0] - (prev[0] + 1))
                    prev = tt

    return volume


# This is a challenge in which I'm supposed to compute the volume of the material used to form a key
# The key is in a form where '#' means the key and '~' is the material which volume I have to compute:
"""
        #~#
 #~~~~~####
 ###~~#####
###########

"""
# This key would be passed to the programme as a following list - [1, 3, 2, 2, 1, 1, 2, 3, 4, 3, 4] (max length 255)
# And the output (volume) would be 8


# Simple tests using pytest
# I could assume input of len > 1 from the challenge

class TestClass:
    def test_capacity(self):
        assert calculate_capacity([1, 3, 2, 2, 1, 1, 2, 3, 4, 3, 4]) == 8
        assert calculate_capacity([1, 4, 2, 1, 1, 2, 5, 3, 4]) == 11
        assert calculate_capacity([1, 4, 1, 2, 3, 1]) == 3
    def test_incorrect_len(self):
        assert calculate_capacity(range(1, 300)) == 0
        assert calculate_capacity(range(1, 256)) == 0