import inflect
p = inflect.engine()

class Calculator:

    def __validate_delimiter(self, delimiter):
        # We assume that the delimiter length is 1
        if len(delimiter) > 1 or delimiter.isdigit() or delimiter in ('-', '.', ''):
            raise Exception(f"Invalid delimiter type - the delimiter must be a single non-digit character that doesn't belong in the character set ('-', '.', '')")
        else:
            return delimiter

    def __extract_numbers(self, input_string, delimiter):
        input_string = self.__check_overflow(input_string)
        return input_string.split(delimiter)

    def __validate_numbers(self, input_string, extracted_numbers):
        valid_numbers = []
        if input_string == "null" or input_string == "":
            valid_numbers.append(0.0)
        else:
            #print(extracted_numbers)
            for i in range(0, len(extracted_numbers)):
                # test the block
                try:
                    number = float(extracted_numbers[i])
                # handle the exception
                except ValueError:
                    if i == 0:
                        raise ValueError(f"Invalid Entry - the input contains a non-digit character at the {p.ordinal(i)} position")
                    raise ValueError(f"Invalid Entry - the input contains a non-digit character after the {p.ordinal(i)} delimiter")
                # execute the block if no error occurs
                else:
                    if number < 0:
                        if i == 0:
                            raise Exception(f"Invalid Entry - the input contains a negative value at the {p.ordinal(i)} position")
                        raise Exception(f"Invalid Entry - the input contains a negative value after the {p.ordinal(i)} delimiter")
                    if number <= 100:
                        valid_numbers.append(number)
        return valid_numbers

    def __check_overflow(self, value):
        try:
            value
        except OverflowError:
            raise OverflowError(f"Memory error - the value of interest is larger than the maximum size of the declared data type")
        else:
            return value

    def add_numbers(self, input_string, delimiter):
        sum = 0.0
        valid_delimiter = self.__validate_delimiter(delimiter)
        extracted_numbers = self.__extract_numbers(input_string, valid_delimiter)
        valid_numbers = self.__validate_numbers(input_string, extracted_numbers)
        for n in valid_numbers:
            sum = self.__check_overflow(sum + n)
        # We assume that the calculator can output numbers greater than 100
        return sum