from random import randint, shuffle


class Password:
    """
    Secure password consisting of 14 randomly generated characters.
    """
    UPPERCASE_RANGE = (65, 90)
    LOWERCASE_RANGE = (97, 122)
    DIGIT_RANGE = (0, 9)
    SPECIAL_CHARS = ((33, 64), (91, 96), (123, 126))

    @staticmethod
    def get_character(letter_range):
        """
        Generates a random letter by converting a random integer to its
        corresponding unicode character.
        :param letter_range: Range of integers that correspond to unicode
        characters.
        :return: The unicode character converted from the random integer.
        """
        num = randint(letter_range[0], letter_range[1])
        uppercase_letter = chr(num)
        return uppercase_letter

    def get_digit(self):
        """
        Generates a random integer within DIGIT_RANGE.
        :return: The random integer.
        """
        return randint(self.DIGIT_RANGE[0], self.DIGIT_RANGE[1])

    def get_special_char(self):
        """
        Generates a random special character from the SPECIAL_CHARS list of
        permitted characters.
        :return: A random character pulled from the SPECIAL_CHARS list.
        """
        index = randint(0, len(self.SPECIAL_CHARS) - 1)
        char = self.SPECIAL_CHARS[index]

        return char

    def generate(self):
        """
        Generates the password with randomly generated letters, numbers and special
        characters.
        :return: The complete password.
        """
        num_chars = 4
        num_spec_chars = 2
        chars = []

        for num in range(0, num_chars):
            chars.append(self.get_character(self.UPPERCASE_RANGE))
            chars.append(self.get_character(self.LOWERCASE_RANGE))
            chars.append(str(self.get_digit()))

        for num in range(0, num_spec_chars):
            char_range = self.get_special_char()
            chars.append(self.get_character(char_range))

        shuffle(chars)

        return ''.join(chars)


if __name__ == '__main__':
    password = Password().generate()
    print(password)
