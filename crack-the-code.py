def cipher(input, key):
    output_string = ''
    for char in input:
        # Checking whether it's a lowercase letter
        if ord(char) in range(ord('a'), ord('z')+1):
            if ((ord(char) + key) < ord('a')):
                output_string += chr((ord(char) + key) + 26)
            elif ((ord(char) + key) > ord('z')):
                output_string += chr((ord(char) + key) - 26)
            else:
                output_string += chr(ord(char)+key)
        # Checking whether it's an uppercase letter
        elif ord(char) in range(ord('A'), ord('Z')+1):
            if ((ord(char) + key) < ord('A')):
                output_string += chr((ord(char) + key) + 26)
            elif ((ord(char) + key) > ord('Z')):
                output_string += chr((ord(char) + key) - 26)
            else:
                output_string += chr(ord(char)+key)
        # If it's not a letter then we don't change it
        else:
            output_string += char
    return output_string



# Simple tests using pytest

class TestClass:
    def test_cipher(self):
        assert cipher("XYZpunctuation, 0123!,.", -5) == 'STUkpixopvodji, 0123!,.'
        assert cipher("abcdefghijklmnopqrstuvwxyz", 5) == 'fghijklmnopqrstuvwxyzabcde'
        assert cipher("ABCEFGHIJKLMNOPQRSTUVWXYZ", 5) == 'FGHJKLMNOPQRSTUVWXYZABCDE'

    def test_no_cipher(self):
        assert cipher('1234324 !12@@', 7) == '1234324 !12@@'
